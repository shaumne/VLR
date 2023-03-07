import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.vlr.gg/rankings/europe"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# links listesini oluştur
links = []
for link in soup.select('a[href^="/team/"]'):
    href = link.get("href")
    data_sort_value = link.get("data-sort-value")
    links.append((href, data_sort_value))

# DataFrame oluştur
df = pd.DataFrame(links, columns=["url", "team_name"])

# url prefixini ekleyerek url kolonunu düzenle
df["url"] = "https://www.vlr.gg" + df["url"]

df.to_excel("eu_teams.xlsx", index=False)