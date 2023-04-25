import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

def get_map_stats(url:str):

    splitted_url = url.split("team/")
    url = f"{splitted_url[0]}team/stats/{splitted_url[1]}"
    print(url)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

   
    map_names = []
    for m_name in soup.find_all("div", class_="mod-first mod-highlight"):
        map_names.append(m_name.text.split())
    
    #print(map_names)

    map_Stats = {"Bind":{"Oynanan Maç":map_names[0][1], "Winrate": map_names[1], "Attack WR": map_names[2], "Def WR": map_names[3]},
                 "Haven":{"Oynanan Maç":map_names[4][1], "Winrate": map_names[5], "Attack WR": map_names[6], "Def WR": map_names[7]},
                 "Split":{"Oynanan Maç":map_names[8][1], "Winrate": map_names[9], "Attack WR": map_names[10], "Def WR": map_names[11]},
                 "Ascent":{"Oynanan Maç":map_names[12][1], "Winrate": map_names[13], "Attack WR": map_names[14], "Def WR": map_names[15]},
                 "Icebox":{"Oynanan Maç":map_names[16][1], "Winrate": map_names[17], "Attack WR": map_names[18], "Def WR": map_names[19]},
                 "Breeze":{"Oynanan Maç":map_names[20][1], "Winrate": map_names[21], "Attack WR": map_names[22], "Def WR": map_names[23]},
                 "Fracture":{"Oynanan Maç":map_names[24][1], "Winrate": map_names[25], "Attack WR": map_names[26], "Def WR": map_names[27]},
                 "Pearl":{"Oynanan Maç":map_names[28][1], "Winrate": map_names[29], "Attack WR": map_names[30], "Def WR": map_names[31]},
                 "Lotus":{"Oynanan Maç":map_names[32][1], "Winrate": map_names[33], "Attack WR": map_names[34], "Def WR": map_names[35]}}
    
    
    
    return map_Stats
 
    
# df = pd.read_csv("all_region.csv")
# url = df.loc[df["team_name"].str.contains("fnatic"), "url"].values[0]
# get_map_stats(url)