"""Tính lịch đề xuất từ dữ liệu quản lý dự án; chỉ dùng thư viện chuẩn Python.

Chạy: python chuong-3/lap-lich.py
Không triển khai chức năng WMS. Các ngày nghỉ và ước lượng nằm trong JSON.
"""
import argparse
import csv
import json
from collections import defaultdict
from datetime import date, datetime, time, timedelta
from pathlib import Path
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

HERE = Path(__file__).resolve().parent

def read_data():
    return json.loads((HERE/'du-lieu-lich.json').read_text(encoding='utf-8'))

def calendar(data):
    first=date.fromisoformat(data['start']); last=date(2028,6,30)
    exceptions=set(map(date.fromisoformat,data['calendar']['exceptions']))
    return [first+timedelta(days=i) for i in range((last-first).days+1)
            if (first+timedelta(days=i)).weekday() in data['calendar']['weekdays']
            and first+timedelta(days=i) not in exceptions]

def month_bounds(n):
    # Tháng dự án: ngày 03 đến hết ngày 02 tháng sau, không đổi sang tháng lịch.
    absolute=2027*12+5+n-1
    y,m=divmod(absolute,12); m+=1
    next_y,next_m=divmod(absolute+1,12)
    return date(y,m,3),date(next_y,next_m+1,2)

def on_or_after(days,dt):
    return next(i for i,d in enumerate(days) if d>=dt)

def boundary_date(days,i):
    return days[max(0,i-1)]

def solve(data):
    days=calendar(data); tasks=data['activities']; ids=[t['id'] for t in tasks]
    if len(ids)!=len(set(ids)): raise ValueError('Trùng mã hoạt động')
    by_id={t['id']:t for t in tasks}
    ordered=[]; pending=tasks.copy()
    while pending:
        ready=[t for t in pending if all(p in {x['id'] for x in ordered} for p in t['predecessors'])]
        if not ready: raise ValueError('Chu trình hoặc mã tiền nhiệm không tồn tại')
        for t in ready: ordered.append(t); pending.remove(t)
    spans={}
    for k,r in data['roles'].items():
        lo,hi=month_bounds(r['month_start'])[0],month_bounds(r['month_finish'])[1]
        spans[k]=(lo,hi)
    ongoing=defaultdict(float)
    for a in data['ongoing']: ongoing[a['resource']]+=a['units']
    load={r:[ongoing[r] if spans[r][0]<=d<=spans[r][1] else 0 for d in days] for r in spans}
    logical={}; scheduled={}; successors=defaultdict(list)
    def offset(task,pred):
        relation=task.get('relations',{}).get(pred,{'type':'FS','lag':0})
        kind=relation['type']; lag=relation['lag']
        if kind=='FS': return by_id[pred]['duration']+lag
        if kind=='SS': return lag
        raise ValueError('Quan hệ chưa hỗ trợ: '+kind)
    for t in ordered:
        rid=t['id']; d=t['duration']
        if d<0 or int(d)!=d: raise ValueError('Thời lượng phải là ngày nguyên không âm')
        if t.get('triple'):
            import math
            mo,ml,mp=t['triple']
            if not 0<=mo<=ml<=mp or math.ceil((mo+4*ml+mp)/6)!=d: raise ValueError('Sai ước lượng ba điểm')
        release=on_or_after(days,date.fromisoformat(t['release'])) if t['release'] else 0
        for r,u in t['resources'].items():
            if r not in spans or u<=0 or u>1: raise ValueError('Sai nguồn lực/đơn vị phân công')
            release=max(release,on_or_after(days,spans[r][0]))
        es=max([release]+[logical[p]['es']+offset(t,p) for p in t['predecessors']])
        logical[rid]=dict(es=es,ef=es+d,release=release)
        for p in t['predecessors']: successors[p].append(rid)
        start=max([release]+[scheduled[p]['start']+offset(t,p) for p in t['predecessors']])
        while d and any(
            not(spans[r][0]<=days[j]<=spans[r][1]) or load[r][j]+u>data['roles'][r]['capacity']+1e-9
            for r,u in t['resources'].items() for j in range(start,start+d)):
            start+=1
            if start+d>=len(days): raise ValueError('Không tìm được lịch trong kỳ nguồn lực: '+rid)
        scheduled[rid]=dict(start=start,end=start+d,
            start_date=str(days[start] if d else boundary_date(days,start)),
            finish_date=str(days[start+d-1] if d else boundary_date(days,start)),
            shifted=start-es)
        for r,u in t['resources'].items():
            for j in range(start,start+d): load[r][j]+=u
    finish=max(v['ef'] for v in logical.values())
    # Backward pass trên mạng logic có release và giới hạn các mốc hợp đồng.
    for t in reversed(ordered):
        rid=t['id']; limits=[logical[s]['ls']-offset(by_id[s],rid)+t['duration'] for s in successors[rid]] or [finish]
        if rid in data['milestones']:
            dl=date.fromisoformat(data['milestones'][rid])
            limits.append(sum(d<=dl for d in days))
        lf=min(limits); ls=lf-t['duration']
        logical[rid].update(ls=ls,lf=lf,total_float=ls-logical[rid]['es'])
    milestone=[]
    for id,deadline in data['milestones'].items():
        actual=date.fromisoformat(scheduled[id]['finish_date']); limit=date.fromisoformat(deadline)
        milestone.append(dict(id=id,finish=str(actual),deadline=deadline,
            margin_workdays=sum(actual<d<=limit for d in days),on_time=actual<=limit))
    closure=date.fromisoformat(scheduled['M6']['finish_date'])
    for r in load:
        for j,day in enumerate(days):
            if day>closure and spans[r][0]<=day<=spans[r][1]: load[r][j]-=ongoing[r]
    phase_cpm={}
    for target in data['milestones']:
        ancestors=set()
        def visit(id):
            if id in ancestors: return
            ancestors.add(id)
            for p in by_id[id]['predecessors']: visit(p)
        visit(target); late={}; target_finish=logical[target]['ef']
        for t in reversed(ordered):
            rid=t['id']
            if rid not in ancestors: continue
            nxt=[s for s in successors[rid] if s in ancestors]
            ls=min([late[s]-offset(by_id[s],rid) for s in nxt] or [target_finish-t['duration']])
            late[rid]=ls
        phase_cpm[target]=dict(finish_index=target_finish,
            critical_activities=[t['id'] for t in ordered if t['id'] in ancestors and late[t['id']]==logical[t['id']]['es']],
            float={id:late[id]-logical[id]['es'] for id in late})
    # LoE duy trì đến M6; không cộng phần nỗ lực này như chuỗi công việc FS.
    resource=[]
    for r,rd in data['roles'].items():
        eligible=[j for j,d in enumerate(days) if spans[r][0]<=d<=spans[r][1]]
        resource.append(dict(id=r,name=rd['name'],start=str(spans[r][0]),finish=str(spans[r][1]),
            available_days=len(eligible),planned_person_days=round(sum(load[r][j] for j in eligible),2),
            peak_units=round(max(load[r][j] for j in eligible),3)))
    return dict(days=days,ordered=ordered,logical=logical,scheduled=scheduled,load=load,
                milestones=milestone,resources=resource,logical_finish=finish,phase_cpm=phase_cpm)

def emit_tables(data,result):
    ts=result['ordered']; s=result['scheduled']; c=result['logical']
    headers=['Mã','WBS','Hoạt động','MO','ML','MP','PERT','Ngày dùng','Tiền nhiệm','Nguồn lực','Bắt đầu','Kết thúc','ES','EF','LS','LF','TF','Dịch do nguồn lực']
    rows=[]
    for t in ts:
        tri=t['triple'] or ['','','']; mean=round((tri[0]+4*tri[1]+tri[2])/6,2) if t['triple'] else ''
        v=s[t['id']]; cp=c[t['id']]
        predecessors=', '.join(p+(' SS+1d' if t.get('relations',{}).get(p,{}).get('type')=='SS' else ' FS') for p in t['predecessors'])
        rows.append([t['id'],', '.join(t['wbs']),t['name'],*tri,mean,t['duration'],predecessors or '—',
                     '; '.join(f'{r} {u:.0%}' for r,u in t['resources'].items()) or '—',v['start_date'],v['finish_date'],
                     cp['es'],cp['ef'],cp['ls'],cp['lf'],cp['total_float'],v['shifted']])
    with (HERE/'bang-hoat-dong.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(headers); w.writerows(rows)
    text='# Bảng hoạt động và lịch đề xuất\n\n'
    text+='Ngày dùng là ngày làm việc. MO/ML/MP là ba điểm ước lượng; ô trống dùng căn cứ trực tiếp. ES/EF/LS/LF/TF là chỉ số ngày của mạng logic có release và hạn mốc, **chưa xét cạnh tranh nguồn lực**; cột ngày bắt đầu/kết thúc là lịch sau phân bổ nguồn lực. Biên thời gian là khoảng [ES, EF), ngày đầu dự án có chỉ số 0. TF toàn mạng không thay biên dự phòng riêng của từng mốc.\n\n'
    text+='| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'
    text+='\n'.join('| '+' | '.join(map(str,row))+' |' for row in rows)+'\n'
    text+='\n## Căn cứ từng hoạt động\n\n| Mã | Căn cứ/điều kiện |\n| --- | --- |\n'
    text+='\n'.join(f"| {t['id']} | {t['basis'] or 'Mốc không thời lượng; đạt khi các công việc tiền nhiệm đáp ứng tiêu chí.'} |" for t in ts)+'\n'
    text+='\n## Công việc quản lý xuyên kỳ\n\nĐây là phân bổ Level of Effort (LoE) – nỗ lực xuyên kỳ; không kéo dài đường găng mạng bàn giao. Dành tỷ lệ năng lực trung bình cố định mỗi ngày trong kỳ huy động, bao gồm trong bảng nguồn lực. Họp thực tế được bố trí vào khoảng năng lực này.\n\n| Mã | WBS | Công việc | Nguồn lực | Phân bổ |\n| --- | --- | --- | --- | --- |\n'
    text+='\n'.join(f"| {a['id']} | {a['wbs']} | {a['name']} | {a['resource']} | {a['units']:.0%} |" for a in data['ongoing'])+'\n'
    (HERE/'bang-hoat-dong.md').write_text(text,encoding='utf-8')
    plain={k:v for k,v in result.items() if k not in ['days','ordered','load']}
    (HERE/'ket-qua-lich.json').write_text(json.dumps(plain,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (HERE/'tai-nguon-luc.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(['Ngày',*data['roles']])
        for i,day in enumerate(result['days']):
            if str(day)>data['finish_deadline']: break
            w.writerow([str(day),*[round(result['load'][r][i],3) for r in data['roles']]])

def emit_gantt(data,result):
    ts=result['ordered']; first=date.fromisoformat(data['start']); last=date.fromisoformat(data['finish_deadline']); scale=4
    left=570; width=left+(last-first).days*scale+70; height=100+len(ts)*25
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<style>text{font-family:Arial,sans-serif;font-size:12px}.title{font-size:20px;font-weight:bold}.small{font-size:11px}</style>',
        '<text x="20" y="28" class="title">WMS Tân Cương – lịch đề xuất theo nguồn lực</text>',
        '<text x="20" y="49">Ngày làm việc: thứ Hai–thứ Sáu; ngoại lệ nghỉ và các ước lượng là giả định lập kế hoạch.</text>']
    for n in range(1,9):
        d=month_bounds(n)[0]; x=left+(d-first).days*scale
        svg.extend([f'<line x1="{x}" y1="65" x2="{x}" y2="{height}" stroke="#cbd5e1"/>',f'<text x="{x+3}" y="77">Tháng {n}</text>'])
    for i,t in enumerate(ts):
        y=95+i*25; v=result['scheduled'][t['id']]; start=date.fromisoformat(v['start_date']); end=date.fromisoformat(v['finish_date']); x=left+(start-first).days*scale
        label=f"{t['id']} · {t['name']}"
        if len(label)>78: label=label[:76]+'…'
        svg.append(f'<text x="20" y="{y+12}">{escape(label)}</text>')
        if t['kind']=='milestone':
            svg.append(f'<polygon points="{x},{y} {x+7},{y+7} {x},{y+14} {x-7},{y+7}" fill="#b45309"/>')
        else:
            w=max(4,((end-start).days+1)*scale); color='#d97706' if t['kind']=='reserve' else '#2563eb'
            svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="15" rx="3" fill="{color}"/>')
        svg.append(f'<text x="{x+10}" y="{y+24}" class="small">{start:%d/%m}–{end:%d/%m}</text>')
    svg.append('</svg>'); (HERE/'gantt.svg').write_text('\n'.join(svg),encoding='utf-8')

def emit_xml(data,result):
    ns='http://schemas.microsoft.com/project'; ET.register_namespace('',ns)
    def node(parent,tag,value=None):
        e=ET.SubElement(parent,'{'+ns+'}'+tag)
        if value is not None: e.text=str(value)
        return e
    def stamp(day,end=False): return day+'T'+('17:00:00' if end else '08:00:00')
    def duration(days):
        seconds=round(days*8*3600); hours,seconds=divmod(seconds,3600); minutes,seconds=divmod(seconds,60)
        return f'PT{hours}H{minutes}M{seconds}S'
    p=ET.Element('{'+ns+'}Project')
    for k,v in [('SaveVersion',14),('Name',data['project']),('Title','Lịch đề xuất WMS Tân Cương'),('ScheduleFromStart',1),('StartDate',stamp(data['start'])),('FinishDate',stamp(data['finish_deadline'],True)),('CalendarUID',1),('DefaultStartTime','08:00:00'),('DefaultFinishTime','17:00:00'),('MinutesPerDay',480),('MinutesPerWeek',2400),('DaysPerMonth',20)]: node(p,k,v)
    cs=node(p,'Calendars')
    def add_cal(uid,name,base,exceptions):
        c=node(cs,'Calendar'); node(c,'UID',uid); node(c,'Name',name); node(c,'IsBaseCalendar',1 if base else 0); node(c,'BaseCalendarUID',-1 if base else 1)
        wd=node(c,'WeekDays')
        for dt in range(1,8):
            day=node(wd,'WeekDay'); node(day,'DayType',dt)
            working=dt in [2,3,4,5,6]; node(day,'DayWorking',int(working))
            if working:
                times=node(day,'WorkingTimes')
                for a,b in [('08:00:00','12:00:00'),('13:00:00','17:00:00')]:
                    w=node(times,'WorkingTime'); node(w,'FromTime',a); node(w,'ToTime',b)
        # Exceptions theo MSPDI; ProjectLibre 1.9.8 cần chế độ mở tại HUONG-DAN.md.
        ex=node(c,'Exceptions')
        for lo,hi,name in exceptions:
            day=node(ex,'Exception'); node(day,'EnteredByOccurrences',0)
            tp=node(day,'TimePeriod'); node(tp,'FromDate',lo+'T00:00:00'); node(tp,'ToDate',hi+'T23:59:00')
            node(day,'Occurrences',(date.fromisoformat(hi)-date.fromisoformat(lo)).days+1)
            node(day,'Name',name); node(day,'Type',1); node(day,'DayWorking',0)
        return c
    add_cal(1,'BTL 5 ngày x 8 giờ',True,[(d,d,'Ngoại lệ giả định') for d in data['calendar']['exceptions']])
    resources=node(p,'Resources'); resource_ids={}
    for uid,(r,rd) in enumerate(data['roles'].items(),1):
        resource_ids[r]=uid; lo=month_bounds(rd['month_start'])[0]; hi=month_bounds(rd['month_finish'])[1]
        exc=[(d,d,'Ngoại lệ giả định') for d in data['calendar']['exceptions']]
        if str(lo)>data['start']: exc.append((data['start'],str(lo-timedelta(days=1)),'Chưa huy động'))
        if str(hi)<data['finish_deadline']: exc.append((str(hi+timedelta(days=1)),data['finish_deadline'],'Kết thúc huy động'))
        add_cal(uid+1,r+' – kỳ huy động',False,exc)
        e=node(resources,'Resource')
        for k,v in [('UID',uid),('ID',uid),('Name',r+' – '+rd['name']),('Type',1),('MaxUnits',1),('CalendarUID',uid+1)]: node(e,k,v)
    tx=node(p,'Tasks'); assignments=node(p,'Assignments'); ai=0
    tasks=result['ordered']; tids={t['id']:i+1 for i,t in enumerate(tasks)}
    for t in tasks:
        id=t['id']; v=result['scheduled'][id]; e=node(tx,'Task'); d=t['duration']
        constrained=bool(t['release'])
        for k,val in [('UID',tids[id]),('ID',tids[id]),('Name',id+' '+t['name']),('Type',1),('IsNull',0),('WBS',','.join(t['wbs'])),('OutlineNumber',tids[id]),('OutlineLevel',1),('Start',stamp(v['start_date'],not d)),('Finish',stamp(v['finish_date'],True)),('Duration',duration(d)),('DurationFormat',7),('Work',duration(d*sum(t['resources'].values()))),('EffortDriven',0),('Milestone',int(d==0)),('Summary',0),('CalendarUID',1),('ConstraintType',4 if constrained else 0),('PercentComplete',0),('Notes',t['basis']+' | WBS: '+','.join(t['wbs']))]: node(e,k,val)
        if constrained: node(e,'ConstraintDate',stamp(str(result['days'][result['logical'][id]['release']])))
        if id in data['milestones']: node(e,'Deadline',stamp(data['milestones'][id],True))
        for pred in t['predecessors']:
            rel=t.get('relations',{}).get(pred,{'type':'FS','lag':0})
            link=node(e,'PredecessorLink'); node(link,'PredecessorUID',tids[pred]); node(link,'Type',3 if rel['type']=='SS' else 1); node(link,'LinkLag',rel['lag']*4800); node(link,'LagFormat',7)
        for r,u in t['resources'].items():
            ai+=1; a=node(assignments,'Assignment')
            for k,val in [('UID',ai),('TaskUID',tids[id]),('ResourceUID',resource_ids[r]),('Units',u),('Start',stamp(v['start_date'])),('Finish',stamp(v['finish_date'],True)),('Work',duration(d*u))]: node(a,k,val)
    # Quản lý xuyên kỳ được đưa vào công cụ để tài nguyên không bỏ sót phần tải nền.
    for j,a in enumerate(data['ongoing'],len(tasks)+1):
        rd=data['roles'][a['resource']]; lo=month_bounds(rd['month_start'])[0]; hi=month_bounds(rd['month_finish'])[1]
        closure=date.fromisoformat(result['scheduled']['M6']['finish_date'])
        active=[d for d in result['days'] if lo<=d<=min(hi,closure)]; e=node(tx,'Task')
        for k,val in [('UID',j),('ID',j),('Name',a['id']+' '+a['name']),('Type',1),('WBS',a['wbs']),('OutlineNumber',j),('OutlineLevel',1),('Start',stamp(str(active[0]))),('Finish',stamp(str(active[-1]),True)),('Duration',duration(len(active))),('DurationFormat',7),('EffortDriven',0),('Milestone',0),('Summary',0),('CalendarUID',resource_ids[a['resource']]+1),('ConstraintType',4),('ConstraintDate',stamp(str(active[0]))),('PercentComplete',0),('Notes','Nỗ lực xuyên kỳ theo năng lực trung bình; không thuộc chuỗi bàn giao. Không lấy đường đỏ tự động của dòng này làm đường găng sản phẩm.')]: node(e,k,val)
        ai+=1; ass=node(assignments,'Assignment')
        for k,val in [('UID',ai),('TaskUID',j),('ResourceUID',resource_ids[a['resource']]),('Units',a['units']),('Start',stamp(str(active[0]))),('Finish',stamp(str(active[-1]),True)),('Work',duration(len(active)*a['units']))]: node(ass,k,val)
    ET.indent(p,space='  '); ET.ElementTree(p).write(HERE/'lich-wms.xml',encoding='utf-8',xml_declaration=True)

def main():
    data=read_data(); result=solve(data)
    emit_tables(data,result); emit_gantt(data,result); emit_xml(data,result)
    print(json.dumps(dict(milestones=result['milestones'],resources=result['resources'],logical_finish_index=result['logical_finish'],activities=len(data['activities'])),ensure_ascii=False,indent=2))

if __name__=='__main__': main()
