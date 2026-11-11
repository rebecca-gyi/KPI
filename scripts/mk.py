from data import R,S
import csv,re
ver={}
for s in S:
    pl=re.sub(r'\s*\(\d+\)$','',s[1])
    v='Wrong' if s[5].startswith('Errors') else 'Right'
    if v=='Wrong' or pl not in ver: ver[pl]=v
ver['ABC1234D']='Right'
if 'SDV6660S' in ver: ver['SNR5368X']=ver['SDV6660S']
special={('GBJ220C','27/08/2026'):('Not paid','Plate typo; same car as GBJ8220C'),('GBM35H','26/08/2026'):('Not paid','Duplicate with mixed-up plate; paid once on 27 Aug'),('WC9469J','18/09/2026'):('Not paid','Not on payout sheet; awaiting Income to lift block'),('SJE3885Z','04/11/2026'):('Right','First quote, paid $18'),('SJE3885Z','05/11/2026'):('Wrong','Requote; payout sheet $6 (Errors)')}
notes={'SLN3705P':'Payout sheet $6','SNS3275M':'Payout sheet $6','XD7945Y':'Payout sheet $6','GBE2714K':'Paid $18, later -$12 (Errors)','GBM9327G':'Paid $18, later -$12 (Errors)','GBG9286Y':'Paid $18, later -$12 (Errors)','SJE3885Z':'Quoted twice (4 & 5 Nov), paid each time','GBM7786C':'Payout sheet $6','GBH1069E':'Payout sheet $6','ABC1234D':'Paid as Triumph (NEW)','SNR5368X':'Paid on Sheet1 as SDV6660S'}
w=csv.writer(open('quotes.csv','w',newline=''))
w.writerow(['no','plate','category','quote_date','month','result','note'])
for r in R:
    if not r[3]: continue
    dd,mm,yy=r[3].split('/'); iso=f'2026-{mm}-{dd}'
    res,note=special.get((r[1],r[3]),(ver.get(r[1]),notes.get(r[1],'')))
    if res is None: res,note='Not paid','Not on payout sheet yet'
    w.writerow([r[0],r[1],r[2].strip() or 'Unspecified',iso,iso[:7],res,note])
