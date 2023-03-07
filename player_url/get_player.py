import requests
from bs4 import BeautifulSoup
import pandas as pd


df = pd.read_excel("./regions/la-s_teams.xlsx")
links = []
nick = []
for url in df["url"]:

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # links listesini oluştur
 
    for link in soup.select('a[href^="/player/"]'):
        href = link.get("href")
        nicks = href.split("/")[-1]
        links.append(href)
        nick.append(nicks)
    print(links)

team = pd.DataFrame({'url': links, 'nick': nick})

team.to_excel("la-s_player_url.xlsx", index=False)

