# KPI – work performance (motor quote tracking)

- `data/rraw.txt` – Rabies Reference quotes: `No|PLATE|Category|DD/MM/YYYY` joined by `;`
- `data/s1.txt` – Sheet1 payouts: `SN|PLATE|Quoted|Settled|Amount|Remarks` joined by `;`
- `data/row_order.txt` – plates in Rabies Reference row order (used for the No column)
- `data/quotes.csv`, `data/payouts.csv`, `data/emails.csv` – generated dashboard data
- `scripts/mk.py` → builds `quotes.csv`; `scripts/mkpay.py` → builds `payouts.csv`
- `dashboard/index.html` – the dashboard page (runs inside the Claude Dashboard artifact, reads the three CSVs)

## Rebuild
```
cd data
python3 -c "R=[x.split('|') for x in open('rraw.txt').read().strip().split(';')]+[['']*4];S=[x.split('|') for x in open('s1.txt').read().strip().split(';')];open('data.py','w').write(f'R={R!r}\nS={S!r}\n')"
PYTHONPATH=. python3 ../scripts/mk.py && PYTHONPATH=. python3 ../scripts/mkpay.py
```
Live dashboard: https://claude.ai/artifact/NxmKTdQGKoNTuY51FrGsYD
See CLAUDE.md for all the rules.
