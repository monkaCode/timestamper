import sys
sys.path.append("")
import discord
from discord.ext import commands
from config import Config

class Timestamper(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix=Config.PREFIX,
            intents=discord.Intents.default(),
            application_id=Config.APPLICATION_ID
        )

        self.initial_extensions = [
            "timestamp"
        ]

    async def setup_hook(self) -> None:
        for ext in self.initial_extensions:
            await self.load_extension(ext)
        
    async def on_ready(self):
        print(f"{self.user} has connected to discord", flush=True)

    async def on_message(self, message: discord.Message) -> None:
        if(message.content == f"{Config.PREFIX}sync" and message.author.id == Config.OWNER):
            synced = await bot.tree.sync()
            await message.channel.send(f"Synced {len(synced)} commands globally")

if __name__ == "__main__":
    bot = Timestamper()
    bot.run(Config.BOT_TOKEN)