import requests
import json
from bs4 import BeautifulSoup
from get_stat_url import get_stat_url
import pandas as pd


# Get Roster of team
def get_roster(url:str):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    #team = soup.find("div", class_="team-roster-item")
    takım = []
    for team in soup.find_all("div", class_="team-roster-item"):
        member = {}
        nick = team.text.split()[0]

        name = " ".join(team.text.split()[1:])
        
        full_name = nick + " " + name
        member["Member"] = full_name
        takım.append(member)
        
    print(takım)
    return takım

# Get W/L of team
def winrate(url:str):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    win = soup.find("span", class_="win").text
    lose = soup.find("span", class_="loss").text

    win_loss = [win,lose]
    return win_loss




# df = pd.read_csv("all_region.csv")
# url = df.loc[df["team_name"].str.contains("bbl"), "url"].values[0]
# winrate(url)