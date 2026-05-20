import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# Connect Database
# -----------------------------
conn = sqlite3.connect("ipl.db")

# -----------------------------
# Load CSV Files
# -----------------------------
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

# -----------------------------
# Save DataFrames as SQL Tables
# -----------------------------
matches.to_sql(
    "matches",
    conn,
    if_exists="replace",
    index=False
)

deliveries.to_sql(
    "deliveries",
    conn,
    if_exists="replace",
    index=False
)

print("Tables imported successfully!\n")

# =========================================================
# QUERY 1 — Top Winning Teams
# =========================================================

query_1 = """
WITH team_wins AS
(
    SELECT
        winner,
        COUNT(*) AS total_wins
    FROM matches
    GROUP BY winner
)

SELECT *
FROM team_wins
ORDER BY total_wins DESC;
"""

result_1 = pd.read_sql(query_1, conn)

print("=== TOP WINNING TEAMS ===")
print(result_1)

# -----------------------------
# Visualization
# -----------------------------

plt.figure(figsize=(10,6))

sns.barplot(
    x="total_wins",
    y="winner",
    data=result_1.head(10)
)

plt.title("Top IPL Teams by Wins")
plt.xlabel("Wins")
plt.ylabel("Teams")

plt.show()

# =========================================================
# QUERY 2 — Top Batters
# =========================================================

query_2 = """
WITH batter_runs AS
(
    SELECT
        batter,
        SUM(batsman_runs) AS total_runs
    FROM deliveries
    GROUP BY batter
)

SELECT *
FROM batter_runs
ORDER BY total_runs DESC
LIMIT 10;
"""

result_2 = pd.read_sql(query_2, conn)

print("\n=== TOP BATTERS ===")
print(result_2)

# -----------------------------
# Visualization
# -----------------------------

plt.figure(figsize=(10,6))

sns.barplot(
    x="total_runs",
    y="batter",
    data=result_2
)

plt.title("Top IPL Batters")
plt.xlabel("Runs")
plt.ylabel("Batters")

plt.show()

# =========================================================
# QUERY 3 — Season Wise Wins
# =========================================================

query_3 = """
WITH season_wins AS
(
    SELECT
        season,
        winner,
        COUNT(*) AS wins
    FROM matches
    GROUP BY season, winner
)

SELECT *
FROM season_wins
ORDER BY season, wins DESC;
"""

result_3 = pd.read_sql(query_3, conn)

print("\n=== SEASON WISE TEAM WINS ===")
print(result_3.head(20))

# =========================================================
# QUERY 4 — Biggest Match Wins Ranking
# =========================================================

query_4 = """
SELECT
    season,
    winner,
    win_by_runs,
    RANK() OVER (
        ORDER BY win_by_runs DESC
    ) AS win_rank
FROM matches;
"""

result_4 = pd.read_sql(query_4, conn)

print("\n=== BIGGEST MATCH WINS ===")
print(result_4.head(20))

# =========================================================
# QUERY 5 — Batters Above Average
# =========================================================

query_5 = """
WITH batter_scores AS
(
    SELECT
        batter,
        SUM(batsman_runs) AS total_runs
    FROM deliveries
    GROUP BY batter
)

SELECT *
FROM batter_scores
WHERE total_runs >
(
    SELECT AVG(total_runs)
    FROM batter_scores
)
ORDER BY total_runs DESC;
"""

result_5 = pd.read_sql(query_5, conn)

print("\n=== BATTERS ABOVE AVERAGE ===")
print(result_5.head(20))

# =========================================================
# QUERY 6 — Team + Batter Combined Analysis
# =========================================================

query_6 = """
SELECT
    m.winner,
    d.batter,
    SUM(d.batsman_runs) AS runs_scored
FROM matches m
INNER JOIN deliveries d
ON m.id = d.match_id
GROUP BY m.winner, d.batter
ORDER BY runs_scored DESC
LIMIT 20;
"""

result_6 = pd.read_sql(query_6, conn)

print("\n=== TEAM + BATTER ANALYSIS ===")
print(result_6)

# =========================================================
# Final Insight Message
# =========================================================

print("\n=== KEY INSIGHTS ===")

print("- Mumbai Indians and Chennai Super Kings are among the most successful teams.")
print("- Virat Kohli appears among the highest run scorers.")
print("- SQL can be combined with Python for powerful analytics workflows.")
print("- Window functions and CTEs make analytical SQL much more powerful.")

# -----------------------------
# Close Database Connection
# -----------------------------
conn.close()