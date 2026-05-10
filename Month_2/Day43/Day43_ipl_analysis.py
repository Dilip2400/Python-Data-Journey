#Import libraries
import pandas as pd  
import seaborn as sns  
import matplotlib.pyplot as plt 

#Load Dataset
matches = pd.read_csv("data\matches.csv")
deliveries = pd.read_csv("data\deliveries.csv")

sns.set_style("whitegrid")

#Understanding dataset
print(matches.head())
#print(matches.info())

print(deliveries.head())
#print(deliveries.info())

"""
#Finding Missing Values
print(matches.isnull().sum())
print(deliveries.isnull().sum())
"""
#Total Matches Played
print("Total Matches: ", matches.shape[0])  #shape[0] - Number of rows

#Most Successful teams
team_wins = matches["winner"].value_counts()
print(team_wins)

#Visualizations of team wins

plt.figure(figsize=(12,6))

sns.barplot(x=team_wins.index, y=team_wins.values)
plt.title("Most Successful IPL Teams")
plt.xlabel("Teams")
plt.ylabel("Wins")

plt.xticks(rotation=90)
plt.show()

# Toss impact analysis
toss_win_match_win = matches[matches["toss_winner"]==matches["winner"]]
print("Matches won after winning toss:", toss_win_match_win.shape[0])

#Top Player of the Match winners
top_players = matches["player_of_match"].value_counts().head(10)
print(top_players)

#Visualizing TOP PLAYERS
plt.figure(figsize=(10,5))

sns.barplot(x=top_players.values, y=top_players.index)
plt.title("Top 10 Player of the Match Winners")
plt.xlabel("Awards Won")
plt.ylabel("Players")

plt.show()

#Top Run Scorers
top_batsmen = deliveries.groupby("batsman")["batsman_runs"].sum()

top_batsmen = top_batsmen.sort_values(ascending=False).head(10)
print("\n Top Batsmen: ", top_batsmen)

#Visualize top batsmen
plt.figure(figsize=(12,6))
sns.barplot(x=top_batsmen.values, y=top_batsmen.index)
plt.title("Top 10 IPL run Scorers")
plt.xlabel("Runs")
plt.ylabel("Players")

plt.show()

#Most Wickets
wickets = deliveries[deliveries["player_dismissed"].notna()]
top_bowlers = wickets["bowler"].value_counts().head(10)
print(top_bowlers)

#Visualize Top Bowlers
plt.figure(figsize=(12,6))

sns.barplot(x=top_bowlers.values, y=top_bowlers.index)
plt.title("Top 10 IPL Wicket Takers")
plt.xlabel("Wickets")
plt.ylabel("Bowlers")
plt.show()


#Boundary Analysis
boundaries = deliveries[(deliveries["batsman_runs"] == 4) | (deliveries["batsman_runs"] == 6)]
print("Total Boundaries: ", boundaries.shape[0])

#Most Siz Hitters

sixes = deliveries[deliveries["batsman_runs"] == 6]

top_six_hitters = sixes["batsman"].value_counts().head(10)
print("Top 10 Six Hitters in IPL", top_six_hitters)

#Visualize Six Hitters
plt.figure(figsize=(12,6))

sns.barplot(x=top_six_hitters.values, y=top_six_hitters.index)
plt.title("Top 10 Six Hitters in IPL")
plt.xlabel("Number of Sixes")
plt.ylabel("Players")

plt.show()