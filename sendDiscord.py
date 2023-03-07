import discord
from discord import app_commands
import json
import time
import requests
from requests import Session
import discord
from discord.ext import commands
from main import get_matches, get_time
from get_roster import get_roster, winrate
import pandas as pd
from map_table import get_map_stats
import asyncio


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
            print("Anotherbot olarak bağlanıldı")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name="games", description="See the Upcoming Matches")
async def get_matches1(interaction:discord.Interaction, args:str):
    df = pd.read_csv("all_region.csv")
    args = args.lower()
    url = ""
    url = df.loc[df["team_name"].str.contains(args), "url"].values[0]
    await interaction.response.defer(ephemeral=False)
    await asyncio.sleep(4)
    print(url)
   
    all_game = get_matches(url)
    rakip1 = all_game.get('1. mac')
    rakip2 = all_game.get('2. mac')

    rm_time = rakip1.get('Kalan Zaman = ')
    
    embed = discord.Embed(title=f"{args} takımının yaklaşmakta olan maçları")
    embed.add_field(name="En yakın maç", value=rakip1.get('Rakip = '), inline=True)
    embed.add_field(name='Kalan Zaman', value=rakip1.get('Kalan Zaman = '), inline=True)
    embed.add_field(name='Maç Tarihi', value=rakip1.get('Mac Tarihi = '), inline=True)
    embed.add_field(name="Sonraki Maç", value=rakip2.get('Rakip = '))
    embed.add_field(name='Kalan Zaman', value=rakip2.get('Kalan Zaman = '), inline=True)
    embed.add_field(name='Maç Tarihi', value=rakip2.get('Mac Tarihi = '), inline=True)
    

    await interaction.followup.send(embed=embed)


@tree.command(name="team", description="See the Team's Stats")
async def get_matches1(interaction:discord.Interaction, args:str):
    df = pd.read_csv("all_region.csv")
    args = args.lower()
    url = ""
    url = df.loc[df["team_name"].str.contains(args), "url"].values[0]
    await interaction.response.defer(ephemeral=True)
    await asyncio.sleep(4)
    
    
    players = get_roster(url)
    matches = get_matches(url)
    rate = winrate(url)


    w_l = f"{rate[0]}/{rate[1]}"

    rakip1 = matches.get('1. mac')
    rakip2 = matches.get('2. mac')

    # Upcoming Matches
    embed = discord.Embed(title=f"{args} takımının yaklaşmakta olan maçları")
    embed.add_field(name="Takımın Total W/L", value=w_l, inline=False)
    embed.add_field(name="En yakın maç", value=rakip1.get('Rakip = '), inline=True)
    embed.add_field(name='Kalan Zaman', value=rakip1.get('Kalan Zaman = '), inline=True)
    embed.add_field(name='Maç Tarihi', value=rakip1.get('Mac Tarihi = '), inline=True)
    embed.add_field(name="Sonraki Maç", value=rakip2.get('Rakip = '))
    embed.add_field(name='Kalan Zaman', value=rakip2.get('Kalan Zaman = '), inline=True)
    embed.add_field(name='Maç Tarihi', value=rakip2.get('Mac Tarihi = '), inline=True)

    # Team player
    embed1 = discord.Embed(title=f" Roster of {args}")
    embed1.add_field(name="Player 1", value=players[0]["Member"], inline=True)
    embed1.add_field(name="Player 2", value=players[1]["Member"], inline=True)
    embed1.add_field(name="Player 3", value=players[2]["Member"], inline=True)
    embed1.add_field(name="Player 4", value=players[3]["Member"], inline=True)
    embed1.add_field(name="Player 5", value=players[4]["Member"], inline=True)





    await interaction.followup.send(embeds=[embed, embed1])

@tree.command(name="maps", description="See the Team's Map Stats")
async def get_maps(interaction:discord.Interaction, args:str):
    df = pd.read_csv("all_region.csv")
    args = args.lower()
    url = df.loc[df["team_name"].str.contains(args), "url"].values[0]

    map_stats = get_map_stats(url)
    print(map_stats)
    await interaction.response.defer(ephemeral=True)
    await asyncio.sleep(4)
    # Map Stats
    embed = discord.Embed(title=f"{args.upper()}'s Map Stats")
    embed.add_field(name="Bind", value="",inline=False)
    embed.add_field(name= "" ,value=f"Oynanan Maç: {map_stats['Bind']['Oynanan Maç']}", inline=True)
    embed.add_field(name= "" ,value=f"Winrate: {map_stats['Bind']['Winrate']}", inline=True)
    embed.add_field(name= "" ,value=f"Attack WR: {map_stats['Bind']['Attack WR']}", inline=True)
    embed.add_field(name= "" ,value=f"Def WR: {map_stats['Bind']['Def WR']}", inline=True)
    embed.add_field(name="Haven", value="",inline=False)
    embed.add_field(name= "" ,value=f"Oynanan Maç: {map_stats['Haven']['Oynanan Maç']}", inline=True)
    embed.add_field(name= "" ,value=f"Winrate: {map_stats['Haven']['Winrate']}", inline=True)
    embed.add_field(name= "" ,value=f"Attack WR: {map_stats['Haven']['Attack WR']}", inline=True)
    embed.add_field(name= "" ,value=f"Def WR: {map_stats['Haven']['Def WR']}", inline=True)
    embed.add_field(name="Split", value="",inline=False)
    embed.add_field(name= "" ,value=f"Oynanan Maç: {map_stats['Split']['Oynanan Maç']}", inline=True)
    embed.add_field(name= "" ,value=f"Winrate: {map_stats['Split']['Winrate']}", inline=True)
    embed.add_field(name= "" ,value=f"Attack WR: {map_stats['Split']['Attack WR']}", inline=True)
    embed.add_field(name= "" ,value=f"Def WR: {map_stats['Split']['Def WR']}", inline=True)
    embed.add_field(name="Ascent", value="",inline=False)
    embed.add_field(name= "" ,value=f"Oynanan Maç: {map_stats['Ascent']['Oynanan Maç']}", inline=True)
    embed.add_field(name= "" ,value=f"Winrate: {map_stats['Ascent']['Winrate']}", inline=True)
    embed.add_field(name= "" ,value=f"Attack WR: {map_stats['Ascent']['Attack WR']}", inline=True)
    embed.add_field(name= "" ,value=f"Def WR: {map_stats['Ascent']['Def WR']}", inline=True)
    embed.add_field(name="Icebox", value="",inline=False)
    embed.add_field(name= "" ,value=f"Oynanan Maç: {map_stats['Icebox']['Oynanan Maç']}", inline=True)
    embed.add_field(name= "" ,value=f"Winrate: {map_stats['Icebox']['Winrate']}", inline=True)
    embed.add_field(name= "" ,value=f"Attack WR: {map_stats['Icebox']['Attack WR']}", inline=True)
    embed.add_field(name= "" ,value=f"Def WR: {map_stats['Icebox']['Def WR']}", inline=True)
    
    embed2 = discord.Embed(title=f"{args.upper()}'s Map Stats")
    embed2.add_field(name="Breeze", value="",inline=False)
    embed2.add_field(name= "" ,value=f"Oynanan Maç: {map_stats['Breeze']['Oynanan Maç']}", inline=True)
    embed2.add_field(name= "" ,value=f"Winrate: {map_stats['Breeze']['Winrate']}", inline=True)
    embed2.add_field(name= "" ,value=f"Attack WR: {map_stats['Breeze']['Attack WR']}", inline=True)
    embed2.add_field(name= "" ,value=f"Def WR: {map_stats['Breeze']['Def WR']}", inline=True)
    embed2.add_field(name="Fracture", value="",inline=False)
    embed2.add_field(name= "" ,value=f"Oynanan Maç: {map_stats['Fracture']['Oynanan Maç']}", inline=True)
    embed2.add_field(name= "" ,value=f"Winrate: {map_stats['Fracture']['Winrate']}", inline=True)
    embed2.add_field(name= "" ,value=f"Attack WR: {map_stats['Fracture']['Attack WR']}", inline=True)
    embed2.add_field(name= "" ,value=f"Def WR: {map_stats['Fracture']['Def WR']}", inline=True)
    embed2.add_field(name="Pearl", value="",inline=False)
    embed2.add_field(name= "" ,value=f"Oynanan Maç: {map_stats['Pearl']['Oynanan Maç']}", inline=True)
    embed2.add_field(name= "" ,value=f"Winrate: {map_stats['Pearl']['Winrate']}", inline=True)
    embed2.add_field(name= "" ,value=f"Attack WR: {map_stats['Pearl']['Attack WR']}", inline=True)
    embed2.add_field(name= "" ,value=f"Def WR: {map_stats['Pearl']['Def WR']}", inline=True)
    embed2.add_field(name="Lotus", value="",inline=False)
    embed2.add_field(name= "" ,value=f"Oynanan Maç: {map_stats['Lotus']['Oynanan Maç']}", inline=True)
    embed2.add_field(name= "" ,value=f"Winrate: {map_stats['Lotus']['Winrate']}", inline=True)
    embed2.add_field(name= "" ,value=f"Attack WR: {map_stats['Lotus']['Attack WR']}", inline=True)
    embed2.add_field(name= "" ,value=f"Def WR: {map_stats['Lotus']['Def WR']}", inline=True)
    
    await interaction.followup.send(embeds=[embed, embed2])

client.run("MTA4MTk4NDQwMzAyODMxMjExNA.Ga1eWh.I6GiGNF31Y9pvUyni4vzWorPC1v2bTtREZrs_Q")