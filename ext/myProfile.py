import hikari, lightbulb
from lib.profile import Profile
import lib.discordLog

plugin = lightbulb.Plugin("myProfile")

@plugin.command
@lightbulb.command("profile", description="View your rewards profile.")
@lightbulb.implements(lightbulb.SlashCommand)
async def myProfile(ctx: lightbulb.Context):
    profileManager = Profile()
    exists = profileManager.profile_exists(ctx.user.id)
    
    if exists == False:
        newProfile = profileManager.create_profile(userId=ctx.user.id)
        
    profile = profileManager.fetch_profile(ctx.user.id)[0]
    
    filteredTitle = profileManager.config['GREET_MSG'].replace("{user}", ctx.user.username)
    filteredDescription = profileManager.config['EMBED_DESCRIPTION'].replace("{user}", ctx.user.username)
    
    constructEmbed = hikari.Embed(
        title=filteredTitle, description=filteredDescription, colour=profileManager.config['EMBED_COLOUR']
    )
    
    constructEmbed.add_field(f"{profileManager.config['ICON']} {profileManager.config['CUSTOM_NAME']}", value=f"> {profile['points']}")
    
    ## Details
    
    if not profileManager.config['EMBED_THUMBNAIL'] == None or profileManager.config['EMBED_THUMBNAIL'] == "":
        constructEmbed.set_thumbnail(profileManager.config['EMBED_THUMBNAIL'])
        
    if not profileManager.config['EMBED_IMAGE'] == None or profileManager.config['EMBED_IMAGE'] == "":
        constructEmbed.set_image(profileManager.config['EMBED_IMAGE'])
    
    if not profileManager.config['AUTHOR_NAME'] == None or profileManager.config['AUTHOR_NAME'] == "":
        constructEmbed.set_author(name=profileManager.config['AUTHOR_NAME'], icon=profileManager.config['AUTHOR_ICON'])
    
    if not profileManager.config['FOOTER'] == None or profileManager.config['FOOTER'] == "":
        constructEmbed.set_footer(text=profileManager.config['FOOTER'], icon=profileManager.config['FOOTER_ICON'])
        
    ## Final
    
    if profileManager.config['PRIVATE'] == True:
        await ctx.respond(embed=constructEmbed, flags=hikari.MessageFlag.EPHEMERAL)
    else:
        await ctx.respond(embed=constructEmbed)
    
    
    
    


def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)