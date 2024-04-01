from typing import Literal
import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime as dt
from dateutil import tz

class timestamp(commands.Cog):
    def __init__(cmd, bot: commands.Bot) -> None:
        cmd.bot = bot

    @app_commands.command(name="timestamp", description="Create a timestamp")
    @app_commands.allowed_installs(guilds=False, users=True)
    @app_commands.allowed_contexts(guilds=False, dms=True, private_channels=True)
    async def about(
        cmd,
        interaction: discord.Interaction,
        hr: int,
        min: int,
        sec: int,
        day: int = dt.now().day,
        month: int = dt.now().month,
        year: int = dt.now().year,
        type: Literal["t", "T", "d", "D", "f", "F", "R"] = "R"):

        timestamp = dt(year, month, day, hr, min, sec, tzinfo=tz.gettz('Europe / Berlin'))
        
        await interaction.response.send_message(f"```<t:{round(timestamp.timestamp())}:{type}>```", ephemeral=True)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(timestamp(bot))