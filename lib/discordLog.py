import hikari, lightbulb, miru, yaml
from lib.logging import Logging as log

async def makeLog(botApp: lightbulb.BotApp, Message: str):
    with open("config.yaml") as conf:
        config = yaml.safe_load(conf)
    
    if config['ENABLE_DISCORD_LOGS'] == False:
        return
    
    LOG_CHANNEL = config['DISCORD_LOG_CHANNEL']
    FETCH_CHANNEL: hikari.GuildTextChannel = await botApp.rest.fetch_channel(LOG_CHANNEL)
    
    if FETCH_CHANNEL:
        await FETCH_CHANNEL.send(Message)
        return
    else:
        log.error(f"Unable to send messages in the channel selected ({LOG_CHANNEL}), Confirm the bot has permission to view channel/send messages?")
        return