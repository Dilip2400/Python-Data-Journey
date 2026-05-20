import sqlite3
import pandas as pd  

#Connect Database
conn = sqlite3.connect("ipl.db")

#Load CSV into DataFrame
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

#Save DataFrame as SQL table
matches.to_sql("matches", conn, if_exists="replace", index=False)
deliveries.to_sql("deliveries", conn, if_exists="replace",index=False)

#Run SQL Query
query = """
SELECT winner, COUNT(*) AS wins
FROM matches
GROUP BY winner
ORDER BY wins DESC

SELECT * FROM matches
INNER JOIN deliveries
ON matches.id = deliveries.match_id;


SELECT 
deliveries.batter, matches.winner, deliveries.batsman_runs
FROM deliveries
INNER JOIN matches
ON deliveries.match_id = matches.id
LIMIT 10;

#LEFT JOIN

SELECT * FROM matches
LEFT JOIN deliveries
ON matches.id = deliveries.match_id;

SELECT deliveries.batter, matches.winner, deliveries.batsman_runs
FROM deliveries INNER JOIN matches
ON deliveries.match_id = matches_id
LIMIT 10;

SELECT matches.winner, SUM(deliveries.batsman_runs) AS total_runs
FROM matches
INNER JOIN deliveries
ON matches.id = deliveries.match_id
GROUP BY matches.winner
ORDER BY total_runs DESC;

SELECT m.winner,SUM(d.batsman_runs) AS total_runs
FROM matches m
INNER JOIN deliveries d
ON m.id=d.match_id
GROUP BY m.winner;

SELECT d.batter. m.winner, d.batsman_runs
FROM deliveries d
INNER JOIN matches m ON d.match_id = m.id
LIMIT 20;

SELECT m.winner, SUM(d.batsman_runs) AS total_runs
FROM matches m
INNER JOIN deliveries d
ON m.id = d.match_id
GROUP BY m.winner
ORDER BY total_runs DESC;

SELECT * FROM matches
WHERE win_by_runs > (
    SELECT AVG(win_by_runs) 
    FROM matches);

SELECT winner, COUNT(*) AS wins
FROM matches
GROUP BY winner
HAVING wins>
(
    SELECT AVG(win_count)
    FROM(
        SELECT COUNT(*) AS win_count
        FROM matches
        GROUP BY winner
    )
);

SELECT * FROM matches
WHERE winner IN (
    SELECT winner
    FROM matches
    GROUP BY winner
    HAVING COUNT(*) > 50
);

SELECT DISTINCT winner
FROM matches m
WHERE EXISTS
(
    SELECT 1
    FROM deliveries d
    WHERE m.id = d.match_id
);

SELECT * FROM matches
WHERE season BETWEEN 2012 AND 2015;

SELECT * FROM matches
WHERE winner LIKE '%Mumbai%';

SELECT
    winner,
    CASE 
        WHEN win_by_runs > 50 THEN 'Big Win'
        ELSE 'Close match'
    END AS match_type
FROM matches;

#Day 53
SELECT winner, win_by_runs, ROW_NUMBER() OVER(
    ORDER BY win_by_runs DESC
) AS row_num

FROM matches;

SELECT
    winner, win_by_runs,
    RANK() OVER(
        ORDER BY win_by_runs DESC
    ) AS team_rank
FROM matches;

SELECT
    winner,
    win_by_runs,
    DENSE_RANK() OVER (
        ORDER BY win_by_runs DESC
    ) AS dense_rank_num
FROM matches;

SELECT
    season,
    winner,
    win_by_runs,
    RANK() OVER (
        PARTITION BY season
        ORDER BY win_by_runs DESC
    ) AS season_rank
FROM matches;

SELECT
    id,
    win_by_runs,
    SUM(win_by_runs) OVER (
        ORDER BY id
    ) AS running_total
FROM matches;

SELECT
    id,
    win_by_runs,
    AVG(win_by_runs) OVER (
        ORDER BY id
    ) AS moving_avg
FROM matches;

SELECT
    winner,
    win_by_runs,
    NTILE(4) OVER (
        ORDER BY win_by_runs DESC
    ) AS quartile
FROM matches;

#DAY 54
SELECT winner, total_wins
FROM
(
    SELECT winner, COUNT(*) AS total_wins
    FROM matches
    GROUP BY winner
)
WHERE total_wins > 50;

WITH team_wins AS
(
    SELECT
        winner,
        COUNT(*) AS total_wins
    FROM matches
    GROUP BY winner
)

SELECT * FROM team_wins
WHERE team_wins >50;

WITH batter_runs AS
(
    SELECT batter, SUM(batsman_runs) AS total_runs
    FROM deliveries
    GROUP BY batter
)

SELECT *
FROM batter_runs
ORDER BY total_runs DESC
LIMIT 10;

#Multiple CTEs

WITH batter_runs AS
(
    SELECT batter, SUM(batsman_runs) AS total_runs
    FROM deliveries
    GROUP BY batter
),
avg_runs AS
(
    SELECT AVG(total_runs) AS avg_score
    FROM batter_runs
)

SELECT * FROM batter_runs
WHERE total_runs>
(
    SELECT avg_score
    FROM avg_runs
);


# Top 3 teams with Highest wins

WITH team_wins AS
(
    SELECT
        winner,
        COUNT(*) AS wins
    FROM matches
    GROUP BY winner
)

SELECT * FROM team_wins
ORDER BY wins DESC
LIMIT 3;

#Players scoring above average total runs

WITH player_scores AS
(
    SELECT
        batter,
        SUM(batsman_runs) AS total_runs
    FROM deliveries
    GROUP BY batter
)

SELECT *
FROM player_scores
WHERE total_runs >
(
    SELECT AVG(total_runs)
    FROM player_scores
);

# Top player per season
WITH season_runs AS
(
    SELECT
        m.season,
        d.batter,
        SUM(d.batsman_runs) AS total_runs
    FROM deliveries d
    INNER JOIN matches m
    ON d.match_id = m.id
    GROUP BY m.season, d.batter
)

SELECT *
FROM season_runs
ORDER BY season, total_runs DESC;
""" 

result_x = pd.read_sql(query,conn)
print(result_x)