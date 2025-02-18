import pandas as pd
import numpy as np
import  plotly.express as px
import plotly.graph_objects as go
Data=pd.read_csv(r"https://raw.githubusercontent.com/Shivmalge/IPL-2022-Data-Analysis/refs/heads/main/IPL.csv")
print(Data)
print(Data.info())

# NUMBER OF MATCHES WON BY EACH TEAM IN IPL 2022:
import plotly.express as px
# Customizing the bar graph
fig = px.bar(
    Data, 
    x="match_winner", 
    title="🏏 IPL 2022: Matches Won by Each Team", 
    labels={"match_winner": "Teams", "count": "Number of Matches Won"},
    color="match_winner",  # Color bars based on teams
    template="plotly_dark"  # Dark theme for better aesthetics
)
# Show figure
fig.show()

# Match Winners by Venue:
# 💡 Purpose: See which teams dominated at specific venues:
fig1=px.bar(Data,x=Data["venue"],
            title="🏟️ IPL 2022: Match Winners by Venue",
             color="match_winner",
             labels={"venue": "Venue", "match_winner": "Winning Team"},
             template="plotly_dark",
    barmode="group"
      )
fig1.show()
#Helps analyze home advantage & team performance at different grounds.

# Toss Decisions & Match Outcomes:
# 💡 Purpose: Check if winning the toss influences match results:
fig2=px.histogram(Data,x=Data["toss_decision"],
                  color="match_winner",
                  labels={"toss_decision": "Toss Decision", "match_winner": "Winning Team"},
                  template="plotly_dark",
                  barmode="group")
fig2.show()
# Reveals whether teams preferring batting first or chasing had an edge.

# Top Scorers & Their Highest Scores:
# 💡 Purpose: Identify top-performing batsmen in IPL 2022:
fig3=px.bar(Data,x=Data["top_scorer"],
            y=Data["highscore"],
            color="highscore",
            labels={"top_scorer": "Player", "highscore": "Highest Score"},
            template="plotly_dark")
fig3.show()
# Highlights big innings & star performers.

# Best Bowling Figures
fig = px.bar(
    Data, 
    x="best_bowling", 
    title="🎯 IPL 2022: Best Bowling Performances",
    labels={"best_bowling": "Bowler", "best_bowling_figure": "Best Bowling Figure"},
    color="best_bowling_figure",
    template="plotly_dark"
)
fig.show()
# Helps recognize impactful bowlers.

# 🏆 IPL 2022: Matches Won by Each Team:
team_wins=Data["match_winner"].value_counts().reset_index()
print(team_wins)
team_wins.columns = ["Team", "Wins"]
print(team_wins)
import plotly.express as px

# Count the number of wins per team
team_wins = Data["match_winner"].value_counts().reset_index()
team_wins.columns = ["Team", "Wins"]

# Create bar chart
fig = px.bar(
    team_wins, 
    x="Team", 
    y="Wins", 
    title="🏆 IPL 2022: Matches Won by Each Team", 
    labels={"Team": "Teams", "Wins": "Number of Matches Won"},
    color="Wins",  # Color intensity based on wins
    template="plotly_dark"
)

# Show figure
fig.show()











