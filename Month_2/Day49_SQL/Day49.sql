#Instead of df[df["runs"]>50]

SELECT * FROM players # " * " Selects all players. [players is Database here]
WHERE runs > 50;   # Condition.

# To Select Specific Columns

SELECT name, runs
FROM players; 

# Filtering with WHERE

SELECT * FROM players
WHERE wickets > 15;


#SORTING with ORDER BY

SELECT * FROM players
ORDER BY runs DESC;

#Setting LIMIT

SELECT * FROM players
ORDER BY runs DESC
LIMIT 5;

# Count - Counts the objects
SELECT COUNT(*)
FROM players;

# DISTINCT - UNIQUE objects from DataBase
SELECT DISTINCT team
FROM players;
