\# 🎮 ML Prep Starter – Steam Reviews Analysis



An introductory ML project analyzing real \*\*Steam player reviews\*\* for \*Stardew Valley\* (AppID \*\*413150\*\*) using Python, SQLite, and AI-assisted development. Repo: https://github.com/CalebSessoms/ml-prep-starter



---



\## Environment

\- \*\*IDE:\*\* VS Code + GitHub Copilot

\- \*\*Python:\*\* 3.13 (virtual env `.venv`)

\- \*\*DB:\*\* SQLite (`data/iris.db`)

\- \*\*Key libs:\*\* `transformers`, `torch`, `pandas`



---



\## Project Overview

This project demonstrates:

\- Real-world data retrieval from the \*\*Steam Reviews API\*\* (JSON).

\- Data cleaning + ingestion into SQLite (`steam\_reviews` table).

\- Statistical analysis (sentiment split, averages).

\- Lightweight text analysis (top words by sentiment).



\*\*Data source:\*\* Steam Reviews API for Stardew Valley — `https://store.steampowered.com/appreviews/413150?json=1\&num\_per\_page=100`



---



\## Database Schema (`steam\_reviews`)

| column | type | notes |

|---|---|---|

| id | INTEGER | auto-increment |

| recommendationid | TEXT | unique per review |

| review\_text | TEXT | raw user review |

| voted\_up | INTEGER | 1=Positive, 0=Negative |

| playtime | INTEGER | minutes played |

| num\_games\_owned | INTEGER | reviewer’s library size |

| timestamp | INTEGER | Unix epoch |

| language | TEXT | filtered to English |



---



\## Results



\### Statistical findings

| Metric | Positive | Negative |

|---|---:|---:|

| % of reviews | \*\*99.3%\*\* | 0.7% |

| Avg. playtime (min) | \*\*8743.9\*\* | 489.0 |

| Avg. games owned | 40.6 | 43.0 |



\*\*Insight:\*\* Reviews are overwhelmingly positive; positive reviewers play dramatically longer (strong engagement signal).



\### Text findings

\*\*Top positive words:\*\* `good`, `fun`, `love`, `cozy`, `best`, `farming`, `life`, `ever`, `valley`  

\*\*Top negative words:\*\* `boring`, `unplayable`, `bad`



\*\*Interpretation:\*\* Positive language emphasizes comfort/enjoyment (“cozy,” “love”), while negatives focus on core issues.



---



\## Process Summary

1\. \*\*Fetch\*\*: Save raw JSON (`data/steam\_413150\_reviews.json`) via `scripts/fetch\_reviews.py`.  

2\. \*\*Ingest\*\*: Parse → `steam\_reviews` table via `scripts/ingest\_reviews.py`.  

3\. \*\*Analyze\*\*:  

&nbsp;  - Stats: `scripts/analyze\_reviews\_stats.py`  

&nbsp;  - Text: `scripts/analyze\_reviews\_text.py`



---



\## Future Work

\- Pull more pages (bigger sample).  

\- Trend analysis over time (`timestamp`).  

\- Visualize with matplotlib/seaborn.  

\- Compare `voted\_up` vs. model-predicted sentiment.



---



\## Reflection

This project shows practical AI-assisted development and data analysis aligned with game-dev analytics: real API integration, clean ingestion, and meaningful insights about player behavior.



