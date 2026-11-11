# KPI – motor quote tracking

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

## Slim down by 27 Nov tracker

Source: the "Slim down by 27 Nov" dashboard (Claude artifact), exported as of 11 Nov 2026.

- `slimdown/index.html`: the tracker page (daily calorie targets vs eaten, weight chart, day-by-day table). Like the motor dashboard, it is a fragment for the artifact dashboard runtime and will not render standalone.
- `slimdown/data/slimdown-log.csv`: the plan and daily log (target kcal by day, eaten kcal, protein, steps, weight, notes). Calories and protein are estimates.

The log contains personal health data (weight).
