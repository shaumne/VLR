import pandas as pd

ap_player = pd.read_excel("ap_player_url.xlsx")
brazil_player = pd.read_excel("brazil_player_url.xlsx")
china_player = pd.read_excel("china_player_url.xlsx")
eu_player = pd.read_excel("eu_player_url.xlsx")
japan_player = pd.read_excel("japan_player_url.xlsx")
kr_player = pd.read_excel("kr_player_url.xlsx")
la_s_player = pd.read_excel("la-s_player_url.xlsx")
na_player = pd.read_excel("na_player_url.xlsx")

combined_players = pd.concat([ap_player, brazil_player, china_player, eu_player, japan_player, kr_player, la_s_player, na_player])

combined_players.to_csv("all_region_player.csv", index=False)