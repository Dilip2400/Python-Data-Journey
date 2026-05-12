"""
IPL Data Analysis Dashboard

This project analyzes IPL match and player data
to identify team trends, batting performance,
bowling impact, and match-winning strategies.

Tools Used:
- Python
- Pandas
- Matplotlib
- Seaborn
"""

#Import libraries
import pandas as pd  
import seaborn as sns  
import matplotlib.pyplot as plt 

#Load Dataset
matches = pd.read_csv("data\matches.csv")
deliveries = pd.read_csv("data\deliveries.csv")

sns.set_style("whitegrid")

fig,axes = plt.subplots(2,2, figsize=(16,12))

#Understanding dataset
#print(matches.head())
#print(matches.info())

#print(deliveries.head())
#print(deliveries.info())

"""
#Finding Missing Values
print(matches.isnull().sum())
print(deliveries.isnull().sum())
"""
#Total Matches Played
#print("Total Matches: ", matches.shape[0])  #shape[0] - Number of rows

#Most Successful teams
team_wins = matches["winner"].value_counts()

sns.barplot(x=team_wins.values, y=team_wins.index, ax=axes[0,0])
axes[0,0].set_title("Most Successful IPL Teams")
 #axes[0,0] - Puts the Graph in top left postion
 
 #Top Batsmen
top_batsmen = deliveries.groupby("batsman")["batsman_runs"].sum().sort_values(ascending=False).head(5)
sns.barplot(x=top_batsmen.values, y=top_batsmen.index, ax=axes[0,1])
axes[0,1].set_title("Top IPL Run Scorers") 

#Top Wicket Takers
wickets = deliveries[deliveries["player_dismissed"].notna()]
top_bowlers=wickets["bowler"].value_counts().head(5)

sns.barplot(x=top_bowlers.values, y=top_bowlers.index, ax=axes[1,0])
axes[1,0].set_title("Top IPL Wicket Takers") 

#Runs by Over Phase
def phase(over):
    if over<=6:
        return "Powerplay"
    elif over<=15:
        return "Middle"
    else:
        return "Death"
    
deliveries["phase"] = deliveries["over"].apply(phase)
phase_runs = deliveries.groupby("phase")["total_runs"].sum()

sns.barplot(x = phase_runs.index, y=phase_runs.values, ax=axes[1,1])

axes[1,1].set_title("Runs Across Match Phases")

plt.suptitle("IPL Analytics Dashboard", fontsize=20)
plt.tight_layout()
plt.savefig("ipl_dashboard.png")
plt.show()

print("\n=== KEY INSIGHTS ===\n")

print("- Mumbai Indians and CSK are among the most successful IPL teams.")
print("- Virat Kohli is among the top run scorers.")
print("- Death overs contribute the highest scoring rates.")
print("- Certain bowlers consistently dominate wicket charts.")