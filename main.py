import lib.logging as logging, lib.profile as profile
import yaml, hikari, lightbulb, miru, random
from lightbulb.ext import tasks

with open("config.yaml") as conf:
    config = yaml.safe_load(conf)

bot = lightbulb.BotApp(config['TOKEN'], intents=hikari.Intents.ALL_UNPRIVILEGED)
bot.load_extensions_from("ext")
bot.d.miru = miru.Client(bot)

@tasks.task(s=int(config['CHANGE_INTERVAL']))
async def statusChanger():
    status = random.choice(config['STATUS_OPTIONS'])
    await bot.update_presence(status=hikari.Status.ONLINE, activity=hikari.Activity(type=hikari.ActivityType.CUSTOM, name=f"{status}"))

@bot.listen(hikari.StartedEvent)
async def onStart(event: hikari.StartedEvent):
    botProfile = bot.get_me()
    logging.Logging.info(f"Logging in as '{botProfile.username}' with a user id of '{botProfile.id}'.")
    logging.Logging.info(f"Bot has started! You are currently running OpenRewards Version {config['VERSION']}.")
    
    if config['STATUS'] == True:
        statusChanger.start() 



bot.run()