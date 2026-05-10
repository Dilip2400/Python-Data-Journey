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
print(matches.info())

print(deliveries.head())
print(deliveries.info())

#Finding Missing Values
print(matches.isnull().sum())
print(deliveries.isnull().sum())

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