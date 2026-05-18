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
"""

result_x = pd.read_sql(query,conn)
print(result_x)

query = """
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

""" 