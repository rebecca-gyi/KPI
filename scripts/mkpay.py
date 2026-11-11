from data import S
import csv,re,datetime as D
w=csv.writer(open('payouts.csv','w',newline=''))
w.writerow(['sn','item','plate','quoted_date','quote_month','week_start','settled','amount','remarks','type'])
for s in S:
    dd,mm,yy=s[2].split('/');d=D.date(2026,int(mm),int(dd));wk=d-D.timedelta(d.weekday())
    a=float(s[4]);st=s[3] or 'Unsettled'
    t='Commission' if s[5]=='Commission' else ('Correction' if 'Paid previously' in s[5] else ('Quote (error)' if s[5]=='Errors' else 'Quote (verified)'))
    item=s[1].title() if s[1].startswith(('TRAV','TRIU')) else s[1]
    plate='ABC1234D' if s[1].startswith('TRIU') else ('' if t=='Commission' else ('SNR5368X' if s[1]=='SDV6660S' else re.sub(r'\s*\(\d+\)$','',s[1])))
    w.writerow([s[0],item,plate,d.isoformat(),d.isoformat()[:7],wk.isoformat(),st,f'{a:.2f}',s[5],t])
