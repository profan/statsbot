from pydantic import BaseModel
import hikari
import json

def read_bot_token_from_file(path: str) -> str:
    with open(path) as f:
        config = json.load(f)
        return config["bot_token"]

CONFIG_FILE_NAME = "config.json"
CONFIG_BOT_TOKEN = read_bot_token_from_file(CONFIG_FILE_NAME)

bot = hikari.GatewayBot(token=CONFIG_BOT_TOKEN)

@bot.listen()
async def register_message_event(event: hikari.GuildMessageCreateEvent) -> None:

    # if contentless message or from a bot, ignore message
    if event.is_bot or not event.content:
        return
    
    actual_channel = event.get_channel()
    if actual_channel:
        actual_channel_name = actual_channel.name
        await event.message.respond(f"hi user in: {actual_channel_name}")

@bot.listen()
async def histogram_channel_activity(event: hikari.GuildMessageCreateEvent) -> None:
    pass

bot.run()