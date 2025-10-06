# \# 🎮 ML Prep Starter – Steam Reviews Analysis

# 

# \## 🧰 1. Environment Setup

# \- \*\*IDE:\*\* Visual Studio Code with GitHub Copilot (Agent Mode enabled)

# \- \*\*Version Control:\*\* \[GitHub Repository](https://github.com/CalebSessoms/ml-prep-starter)

# \- \*\*Python:\*\* 3.13 (virtual environment: `.venv`)

# \- \*\*Key Packages:\*\* `transformers`, `torch`, `pandas`, `sqlite3`, `urllib`

# \- \*\*Database:\*\* SQLite (`data/iris.db`)

# 

# ---

# 

# \## 💡 2. Project Overview

# \*\*Topic:\*\* Player sentiment and behavior analysis for \*Stardew Valley\* (Steam AppID \*\*413150\*\*).  

# 

# This project demonstrates:

# \- AI-assisted development (GitHub Copilot)

# \- Data retrieval from real-world APIs

# \- Database schema design and ingestion

# \- Exploratory data analysis (EDA)

# \- Basic text analytics on player sentiment

# 

# ---

# 

# \## 🔗 3. Data Source

# Data was pulled directly from the \*\*Steam Reviews API\*\*:

https://store.steampowered.com/appreviews/413150?json=1\&num\_per\_page=100





Each entry includes fields such as:

\- `review` (text)

\- `voted\_up` (positive/negative)

\- `playtime\_forever`

\- `num\_games\_owned`

\- `timestamp\_created`



---



\## 🧱 4. Database Schema



| Column | Type | Description |

|---------|------|-------------|

| `id` | INTEGER | Auto-incremented primary key |

| `recommendationid` | TEXT | Unique Steam review ID |

| `review\_text` | TEXT | Player’s review |

| `voted\_up` | INTEGER | 1 = Positive, 0 = Negative |

| `playtime` | INTEGER | Total minutes played |

| `num\_games\_owned` | INTEGER | Number of games owned by reviewer |

| `timestamp` | INTEGER | Unix timestamp |

| `language` | TEXT | Review language |



---



\## 📊 5. Statistical Analysis Results



| Metric | Positive | Negative |

|---------|-----------|-----------|

| \*\*% of Reviews\*\* | 99.3% | 0.7% |

| \*\*Average Playtime (minutes)\*\* | 8743.9 | 489.0 |

| \*\*Average Games Owned\*\* | 40.6 | 43.0 |



\*\*Interpretation:\*\*

\- Stardew Valley enjoys \*overwhelmingly positive\* sentiment.

\- Positive reviewers have significantly higher playtimes.

\- Negative reviewers tend to quit early.



---



\## ✏️ 6. Text Analysis Results



\*\*Most Common Positive Words:\*\*

`good`, `fun`, `love`, `cozy`, `best`, `farming`, `life`, `ever`, `valley`



\*\*Most Common Negative Words:\*\*

`boring`, `unplayable`, `bad`



\*\*Interpretation:\*\*

\- Positive reviews emphasize comfort and enjoyment.

\- Negative reviews focus on core issues like boredom or bugs.



---



\## 🧠 7. Tools \& Process

1\. \*\*Fetch Reviews:\*\* Used Steam API and saved JSON locally (`data/steam\_413150\_reviews.json`).

2\. \*\*Ingest Data:\*\* Parsed and stored reviews in SQLite (`steam\_reviews` table).

3\. \*\*Statistical Analysis:\*\* Queried with SQL + `pandas`.

4\. \*\*Text Analysis:\*\* Tokenized words and compared frequency by sentiment.



---



\## 🔮 8. Future Enhancements

\- Pull more review pages for larger samples.

\- Track sentiment over time (by `timestamp`).

\- Visualize results with `matplotlib` or `seaborn`.

\- Compare player `voted\_up` with AI-predicted sentiment (using Hugging Face).



---



\## 📘 9. Reflection

This project demonstrates:

\- Competency with AI-assisted development tools.

\- Practical data pipeline creation.

\- Integration of \*\*real-world data\*\* with analytics.

\- Insight generation relevant to \*\*game development and player engagement\*\*.



---



© 2025 Caleb Sessoms



