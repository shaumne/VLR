import requests
import json
from bs4 import BeautifulSoup
from get_url import main
import pandas as pd
from datetime import datetime
def get_matches(args:str):

    url = args

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    # turnuva bilgilerini tutacak boş bir liste oluşturuyoruz
    turnuvalar = []

    # İlk maç
    turnuva_div = soup.find("div", class_="m-item-event text-of")
    turnuva = {"1. Oyun": turnuva_div.find("div").text.strip()}
    turnuvalar.append(turnuva)

   
    # 1.Rakip takım'ın ve BBl'in ismini çekiyoruz
    all_teams = soup.find_all("span", class_="m-item-team-tag")

    bbl = all_teams[0].text.split()
    rakip = all_teams[1].text.split()

    # 2. rakip takım
    rakip2_div = soup.find_all("a", class_="wf-card fc-flex m-item")[1].find_all("span", class_="m-item-team-tag")[1]
    rakip2_div_text = rakip2_div.text.split()

    if bbl:
        team1 = {}
        if len(bbl) >= 2:
            bbl = f"{bbl[0]} {bbl[1]}"
        team1["BBl"] = bbl[-1]
        turnuvalar.append(team1)

    if rakip:
        team2 = {}
        if len(rakip) >= 2:
            rakip = f"{rakip[0]} {rakip[1]}"
        team2["1. Rakip"] = rakip[-1]
        turnuvalar.append(team2)

    if rakip2_div_text:
        team3 = {}
        if len(rakip2_div_text) >= 2:
            rakip2_div_text = f"{rakip2_div_text[0]} {rakip2_div_text[1]}"
        team3["2. Rakip"] = rakip2_div_text[-1]
        turnuvalar.append(team3)


    # 1.maç kalan zaman
    rakip1_rm_time = soup.find_all("a", class_="wf-card fc-flex m-item")[0].find_all("span", class_="rm-item-score-eta")
    rakip1_full_time = soup.find_all("a", class_="wf-card fc-flex m-item")[0].find_all("div", class_="m-item-date")
    rakip1_full_time_text = ""



    rakip1_rm_time_text = ""
    for time in rakip1_rm_time:
        rakip1_rm_time_text += time.text.strip() + ""
        rm1_time = {}
        rm1_time["1.rakip kalan zaman"] = rakip1_rm_time_text
        turnuvalar.append(rm1_time)

    for fullTime in rakip1_full_time:
        rakip1_full_time_text += fullTime.text.strip() + ""
        full_time_r1 = f"{rakip1_full_time_text.split()[0]} {rakip1_full_time_text.split()[1]}"
        r1_time = {}
        r1_time["1.rakip mac zamani"] = full_time_r1
        turnuvalar.append(r1_time)


    # 2.maç kalan zaman
    rakip2_rm_time = soup.find_all("a", class_="wf-card fc-flex m-item")[1].find_all("span", class_="rm-item-score-eta")
    rakip2_rm_time_text = ""
    for time in rakip2_rm_time:
        rakip2_rm_time_text += time.text.strip() + ""
        rm2_time = {}
        rm2_time["2.rakip kalan zaman"] = rakip2_rm_time_text
        turnuvalar.append(rm2_time)

    rakip2_full_time = soup.find_all("a", class_="wf-card fc-flex m-item")[1].find_all("div", class_="m-item-date")
    rakip2_full_time_text = ""

    for fullTime2 in rakip2_full_time:
        rakip2_full_time_text += fullTime2.text.strip() + ""
        full_time_r2 = f"{rakip2_full_time_text.split()[0]} {rakip2_full_time_text.split()[1]}"
        r2_time = {}
        r2_time["2.rakip mac zamani"] = full_time_r2
        turnuvalar.append(r2_time)
        

    match = json.dumps(turnuvalar, ensure_ascii=False)

    results1 = {}
    for item in turnuvalar:
        for key, value in item.items():
            if key.startswith("1."):
                results1[key] = value

    results2 = {}
    for item in turnuvalar:
        for key, value in item.items():
            if key.startswith("2."):
                results2[key] = value

    f_match = {"Turnuva Adi = ": results1.get('1. Oyun'),
            "Rakip = ": results1.get('1. Rakip'),
            "Kalan Zaman = ": results1.get('1.rakip kalan zaman'),
            "Mac Tarihi = ": results1.get('1.rakip mac zamani')}

    s_match = {"Turnuva Adi = ": results2.get('2. Oyun'),
            "Rakip = ": results2.get('2. Rakip'),
            "Kalan Zaman = ": results2.get('2.rakip kalan zaman'),
            "Mac Tarihi = ": results2.get('2.rakip mac zamani')}
    
    all_game = {"1. mac":f_match,
                "2. mac": s_match}
    # print(f_match)
    print(all_game)

    return all_game

def get_time(url:str):
    dict_ = get_matches(url)
    rakip1 = dict_.get("1. mac")
    
    time = rakip1.get("Kalan Zaman = ")
    return time


# df = pd.read_csv("all_region.csv")
# url = df.loc[df["team_name"].str.contains("bbl"), "url"].values[0]
# get_time(url)