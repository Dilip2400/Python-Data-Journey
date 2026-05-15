import sqlite3
import pandas as pd  

#Connect Database
conn = sqlite3.connect("ipl.db")

#Load CSV into DataFrame
matches = pd.read_csv("matches.csv")

#Save DataFrame as SQL table
matches.to_sql("matches", conn, if_exists="replace", index=False)

#Run SQL Query
query = """
SELECT winner, COUNT(*) AS wins
FROM matches
GROUP BY winner
ORDER BY wins DESC
"""

result = pd.read_sql(query,conn)
print(result) 