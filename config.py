import json

with open(r"config.json") as f:
    config = json.load(f)

class Config:
    APPLICATION_ID:int = config["application_id"]
    BOT_TOKEN:str = config["bot_token"]
    PREFIX:str = config["prefix"]
    OWNER:int = config["owner"]