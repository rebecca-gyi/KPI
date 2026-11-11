# KPI

## Motor quote submissions dashboard

Source: the "Motor quote submissions" dashboard (Claude artifact), exported as of 11 Nov 2026.

- `dashboard/index.html`: the dashboard page (HTML, CSS and the calculations/charts). It is a fragment for the artifact dashboard runtime (`dash.calc`, `dash.onData`, `d3`), so it will not render standalone in a browser.
- `dashboard/datasets.json`: which data file feeds which dataset id used by the page.
- `dashboard/data/*.csv`: the three data snapshots (`quotes`, `payouts`, `emails`).

What it tracks: quotes per day/week/month against a target of 10 a day, accuracy (right vs wrong), income from the payout sheet ($18 per verified quote, $6 with errors, -$12 clawbacks, plus commission), split by vehicle type, plus reply speed to Keith's requests.

The data files contain plate numbers and payout amounts.
