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

toss_match_win = matches[matches["toss_winner"] == matches["winner"]]

toss_win_percentage = (toss_match_win.shape[0]/matches.shape[0])*100
print("Toss Win Match Win %:", toss_win_percentage)

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

#Most Six Hitters

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

#Strike Rate Analysis
batter_stats = deliveries.groupby("batsman").agg({"batsman_runs" : "sum", "ball" : "count"})
batter_stats["Strike_rate"] = (batter_stats["batsman_runs"]/batter_stats["ball"])*100

print(batter_stats.head())

#Best Strike Rates (With Minimum Filter)
filtered_batters = batter_stats[batter_stats["ball"]>500]

top_sr = filtered_batters.sort_values(by="Strike_rate", ascending=False).head(10)
print("\n Batsmen with Highest Strike Rate \n",top_sr)

#Visualising Strike Rates
plt.figure(figsize=(12,6))
sns.barplot(x=top_sr["Strike_rate"], y=top_sr.index)
plt.title("Batsmen with Higher Strike Rate")
plt.xlabel("Strike Rate")
plt.ylabel("Players")
plt.show()

#Bowling Economy
bowler_stats = deliveries.groupby("bowler").agg({"total_runs":"sum", "ball":"count"})
bowler_stats["overs"] = bowler_stats["ball"] / 6
bowler_stats["economy"]=(bowler_stats["total_runs"]/bowler_stats["overs"])

print(bowler_stats.head())

#Best Economy Bowlers
filtered_bowlers = bowler_stats[bowler_stats["ball"]>500]

best_economy = filtered_bowlers.sort_values(by="economy").head(10)
print(best_economy)

#Visualize economy
plt.figure(figsize=(12,6))
sns.barplot(x=best_economy["economy"], y=best_economy.index)
plt.title("Best Economy Bowlers")
plt.xlabel("Economy")
plt.ylabel("Players")
plt.show()

#Over-wise score trending
over_runs = deliveries.groupby("over")["total_runs"].sum()
print(over_runs)

#Visualizing Overs trend
plt.figure(figsize=(12,6))

sns.lineplot(x=over_runs.index, y=over_runs.values)
plt.title("Runs Scored Per Over")
plt.xlabel("Over")
plt.ylabel("Total Runs")
plt.show()

#Bat First vs Chase
matches["win_type"] = matches["win_by_runs"].apply(lambda x: "Bat First" if x > 0 else "Chasing")
print(matches["win_type"].value_counts())

#Visualizing Winning Style
plt.figure(figsize=(12,6))

sns.countplot(x="win_type", data=matches)
plt.title("Bat First vs Chasing Wins")
plt.xlabel("Winning Style")
plt.ylabel("Matches Won")
plt.show()

#Venue analysis
top_venues = matches["venue"].value_counts().head(10)
print(top_venues)

#Visualize Venues
plt.figure(figsize=(12,6))

sns.barplot(x=top_venues.values, y=top_venues.index)
plt.title("Top IPL Venues by Matches Hosted")
plt.xlabel("Matches")
plt.ylabel("Venue")
plt.show()

#Highest team scores
team_scores = deliveries.groupby(["match_id", "inning", "batting_team"])["total_runs"].sum()
highest_scores = team_scores.sort_values(ascending=False).head(10)

print(highest_scores)

#Over Phase Analysis

def over_phase(over):
    if over<=6:
        return "Powerplay"
    elif over <=15:
        return "Middle Overs"
    else:
        return "Death Overs"

deliveries["phase"] = deliveries["over"].apply(over_phase)

#Runs by Phase
phase_runs = deliveries.groupby("phase")["total_runs"].sum()
print(phase_runs)

#Visualize Phases
plt.figure(figsize=(12,6))

sns.barplot(x = phase_runs.index, y = phase_runs.values)
plt.title("Runs Scored Across Match Phases")
plt.xlabel("Match Phase")
plt.ylabel("Total Runs")

plt.show()