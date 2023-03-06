import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

df = pd.read_excel("all_region.xlsx")
df["team_name"] = df["team_name"].str.lower()
df.to_csv("all_region.csv", index=False)