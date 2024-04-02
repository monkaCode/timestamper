from typing import Literal
import discord
from discord import app_commands
from discord.ext import commands
import requests

from config import Config
from get_last_vct_emea_match_id import get_last_vct_emea_match_id

class stats(commands.Cog):
    def __init__(cmd, bot: commands.Bot) -> None:
        cmd.bot = bot

    @app_commands.command(name="stats", description="Create a timestamp")
    @app_commands.allowed_installs(guilds=False, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def stats(
        cmd,
        interaction: discord.Interaction,
        team: Literal["KC", "TH", "NAVI", "FNC", "VIT", "KOI", "FUT", "TL", "GX", "BBL", "M8"]):

        await interaction.response.send_message(embed=discord.Embed(title=":hourglass: FETCHING DATA...", color=0xffff00), ephemeral=True)
        msg:discord.Message = await interaction.original_response()
        embed = msg.embeds[0]

        match_info = get_last_vct_emea_match_id(team)

        data = requests.post(f"https://api.valolytics.gg/api/stats/teamstats/esports/{match_info['matchId']}", headers={"x-api-key": Config.VALOLYTICS_API_KEY }).json()

        emojis = {
            "Red": data['teams']['Red']['emoji'],
            "Blue": data['teams']['Blue']['emoji']
        }
        
        embed.title = "STATS"
        embed.description = f":stopwatch: Start: <t:{round(match_info['gameStartTimeMillis']/1000)}:R>\n:crossed_swords: {emojis['Red']} {data['teams']['Red']['teamName']} - {data['teams']['Blue']['teamName']} {emojis['Blue']} [{data['teams']['Red']['roundsWon']} : {data['teams']['Blue']['roundsWon']}]\n:map: Map: {data['map']}"
        team_stats_value = f"FK Conversion:\n{emojis['Red']}`{data['teams']['Red']['firstKillRoundConversions']}/{data['teams']['Red']['firstKills']}` | {emojis['Blue']}`{data['teams']['Blue']['firstKillRoundConversions']}/{data['teams']['Blue']['firstKills']}`"
        team_stats_value += f"\nFD Conversion:\n{emojis['Red']}`{data['roundConversions']['4vs5']['roundsWon']}/{data['teams']['Red']['firstDeaths']}` | {emojis['Blue']}`{data['roundConversions']['5vs4']['rounds']-data['roundConversions']['5vs4']['roundsWon']}/{data['teams']['Blue']['firstDeaths']}`"
        team_stats_value += f"\nGun Round Wins:\n{emojis['Red']}`{data['teams']['Red']['gunRoundsWon']}/{data['teams']['Red']['gunRounds']}` | {emojis['Blue']}`{data['teams']['Blue']['gunRoundsWon']}/{data['teams']['Blue']['gunRounds']}`"
        team_stats_value += f"\nPlant Wins:\n{emojis['Red']}`{data['teams']['Red']['plantsWon']}/{data['teams']['Red']['plants']}` | {emojis['Blue']}`{data['teams']['Blue']['plantsWon']}/{data['teams']['Blue']['plants']}`"
        team_stats_value += f"\nDefuse Wins:\n{emojis['Red']}`{data['teams']['Blue']['plants']-data['teams']['Blue']['plantsWon']}/{data['teams']['Blue']['plants']}` | {emojis['Blue']}`{data['teams']['Red']['plants']-data['teams']['Red']['plantsWon']}/{data['teams']['Red']['plants']}`"

        embed.add_field(name=f"Team Stats", value=team_stats_value)

        player_stats_red_value = ""
        player_stats_blue_value = ""
        for player in data['teams']['Red']["players"].values():
            player_stats_red_value += f"{player['gameName'].split(' ', 1)[1]}: `{player['firstKills']}-{player['firstDeaths']}`\n"
        for player in data['teams']['Blue']["players"].values():
            player_stats_blue_value += f"{player['gameName'].split(' ', 1)[1]}: `{player['firstKills']}-{player['firstDeaths']}`\n"
        
        embed.add_field(name=f"{emojis['Red']} FK-FD", value=player_stats_red_value)
        embed.add_field(name=f"{emojis['Blue']} FK-FD", value=player_stats_blue_value)

        embed.color = 0x00ff00
        await msg.edit(embed=embed)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(stats(bot))