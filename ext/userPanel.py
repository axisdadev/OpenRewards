import hikari.embeds
import hikari.users
import hikari, lightbulb, miru, asyncio

from lib.profile import Profile
from lib.logging import Logging
import lib.discordLog as discordLog


from tinydb import TinyDB, Query
from tinydb.operations import add, subtract, delete

plugin = lightbulb.Plugin("userPanel")

class amountModel(miru.Modal, title="Choose Amount to Add/Remove"):
    amount = miru.TextInput(
        label="Amount",
        placeholder="100",
        required=True
    )
    async def callback(self, context: miru.ModalContext) -> None:
        self.saveResp = await context.respond("🔃💾 **Please wait...**", flags=hikari.MessageFlag.EPHEMERAL)
        return 
    

class userPanel(miru.View):
    @miru.button(emoji="➕", label="Add Points", style=hikari.ButtonStyle.SUCCESS)
    async def addPoints(self, ctx: miru.ViewContext, button: miru.Button) -> None:
        profileManager = Profile()
        db = profileManager.db
        
        self.config = profileManager.config
        
        if not profileManager.profile_exists(self.userId):
            profileManager.create_profile(self.userId)
        
        fetchProfile = profileManager.fetch_profile(self.userId)
        promptModal = amountModel()
        await ctx.respond_with_modal(promptModal)
        await promptModal.wait()
        
        amountSelect = promptModal.amount.value
        await promptModal.saveResp.delete()
        
        ## Checking valid permissions based off config.yaml
        
        if int(amountSelect) >= int(self.config['MAXIMUM_ADD']):
            if any(role_id in self.user.role_ids for role_id in self.config['BYPASS_ROLE']):
                pass
            else:
                await discordLog.makeLog(self.bot, f"> ⚠️➕ Staff member 👤{ctx.user.mention} ({ctx.user.id}) **Attempted to add {amountSelect}{self.config['ICON']}** {self.config['CUSTOM_NAME']} **to 👤{self.user.mention} ({self.userId})**, User was blocked due to set server limit.")
                return await ctx.respond(f"> ❌ Unable to add that amount of points. This server has a set limit of {self.config['MAXIMUM_ADD']}.", flags=hikari.MessageFlag.EPHEMERAL)
            
        ## DB Operations
        
        user = Query()
        operation = db.update(add("points", int(amountSelect)), user.user == self.userId)
        
        ## Logging and Notification
        
        await ctx.respond(f"> ✅ Sucessfully added **{amountSelect}{self.config['ICON']}** {self.config['CUSTOM_NAME']}.", flags=hikari.MessageFlag.EPHEMERAL)
        Logging.warn(f'Staff member {ctx.user.username} ({ctx.user.id}) Sucessfully gave {amountSelect} {self.config['CUSTOM_NAME']} to {self.user.username} ({self.userId})')
        await discordLog.makeLog(self.bot, f"> ➕ Staff member 👤{ctx.user.mention} ({ctx.user.id}) **Sucessfully gave {amountSelect}{self.config['ICON']}** {self.config['CUSTOM_NAME']} **to 👤{self.user.mention} ({self.userId})**")
        
        ## User notifcation
        
        if self.config['ENABLE_USER_NOTIFS'] == True:
            notifEmbed = hikari.Embed(
                title=f"{self.config['CUSTOM_NAME']} Were added to your account.",
                description=f"**👋 Hi there!** {amountSelect}{self.config['ICON']} {self.config['CUSTOM_NAME']} **Have been added** to your account. Hooray! 🎉",
                colour=profileManager.config['EMBED_COLOUR']
            )
            
            if not profileManager.config['EMBED_THUMBNAIL'] == None or profileManager.config['EMBED_THUMBNAIL'] == "":
               notifEmbed.set_thumbnail(profileManager.config['EMBED_THUMBNAIL'])
        
            if not profileManager.config['EMBED_IMAGE'] == None or profileManager.config['EMBED_IMAGE'] == "":
               notifEmbed.set_image(profileManager.config['EMBED_IMAGE'])
    
            if not profileManager.config['AUTHOR_NAME'] == None or profileManager.config['AUTHOR_NAME'] == "":
               notifEmbed.set_author(name=profileManager.config['AUTHOR_NAME'], icon=profileManager.config['AUTHOR_ICON'])
    
            if not profileManager.config['FOOTER'] == None or profileManager.config['FOOTER'] == "":
               notifEmbed.set_footer(text=profileManager.config['FOOTER'], icon=profileManager.config['FOOTER_ICON'])
            
            try:
                await self.user.send(embed=notifEmbed)
            except:
                Logging.error("I wasnt able to message user about point addition.")
            
        ## Update the panel for ease of access
    
        updatedProfile = profileManager.fetch_profile(self.userId)[0] # Update the fetchProfile variable for the latest data to be displayed.
        panelEmbed = hikari.Embed(
            title=f"{profileManager.config['ICON']} Staff Panel",
            description=f"The staff panel for User {profileManager.config['CUSTOM_NAME']} Management.",
            colour=profileManager.config['EMBED_COLOUR'],
        )
            
        if not profileManager.config['EMBED_THUMBNAIL'] == None or profileManager.config['EMBED_THUMBNAIL'] == "":
            panelEmbed.set_thumbnail(profileManager.config['EMBED_THUMBNAIL'])
    
        panelEmbed.add_field(f"{profileManager.config['ICON']} {profileManager.config['CUSTOM_NAME']}", value=f"> {updatedProfile['points']}")
        panelEmbed.set_author(name=self.user.username, icon=self.user.make_avatar_url())
        panelEmbed.set_footer(f"Staff Member: {ctx.author.username} ({ctx.user.id})", icon=ctx.author.make_avatar_url())
        await ctx.edit_response(embed=panelEmbed)
            
    
    @miru.button(emoji="➖", label="Remove Points", style=hikari.ButtonStyle.DANGER)
    async def removePoints(self, ctx: miru.ViewContext, button: miru.Button) -> None:
        profileManager = Profile()
        db = profileManager.db
        
        self.config = profileManager.config
        
        if not profileManager.profile_exists(self.userId):
            profileManager.create_profile(self.userId)
        
        fetchProfile = profileManager.fetch_profile(self.userId)[0]
        promptModal = amountModel()
        await ctx.respond_with_modal(promptModal)
        await promptModal.wait()
        
        amountSelect = promptModal.amount.value
        await promptModal.saveResp.delete()
        
        ## Checking valid permissions based off config.yaml
        
        if int(amountSelect) >= int(self.config['MAXIMUM_SUB']):
            if any(role_id in self.user.role_ids for role_id in self.config['BYPASS_ROLE']):
                pass
            else:
                await discordLog.makeLog(self.bot, f"> ⚠️➖ Staff member 👤{ctx.user.mention} ({ctx.user.id}) **Attempted to remove {amountSelect}{self.config['ICON']}** {self.config['CUSTOM_NAME']} **to 👤{self.user.mention} ({self.userId})**, User was blocked due to set server limit.")
                return await ctx.respond(f"> ❌ Unable to remove that amount of points. This server has a set limit of {self.config['MAXIMUM_SUB']}.", flags=hikari.MessageFlag.EPHEMERAL)
        
        if int(amountSelect) > fetchProfile['points']:
            if any(role_id in self.user.role_ids for role_id in self.config['BYPASS_ROLE']):
                pass
            else:
                return await ctx.respond(f"> ❌ Unable to remove that amount of points. That user doesnt have a greater balance then what is selected.", flags=hikari.MessageFlag.EPHEMERAL)
        
        ## DB Operations
        
        user = Query()
        operation = db.update(subtract("points", int(amountSelect)), user.user == self.userId)
        
        ## Logging and Notification
        
        await ctx.respond(f"> ✅ Sucessfully removed **{amountSelect}{self.config['ICON']}** {self.config['CUSTOM_NAME']}.", flags=hikari.MessageFlag.EPHEMERAL)
        Logging.warn(f'Staff member {ctx.user.username} ({ctx.user.id}) Sucessfully removed {amountSelect} {self.config['CUSTOM_NAME']} to {self.user.username} ({self.userId})')
        await discordLog.makeLog(self.bot, f"> ➖ Staff member 👤{ctx.user.mention} ({ctx.user.id}) **Sucessfully removed {amountSelect}{self.config['ICON']}** {self.config['CUSTOM_NAME']} **from 👤{self.user.mention} ({self.userId})**")
        
        ## User notifcation
        
        if self.config['ENABLE_USER_NOTIFS'] == True:
            notifEmbed = hikari.Embed(
                title=f"{self.config['CUSTOM_NAME']} Were removed from your account.",
                description=f"**👋 Hi there!** {amountSelect}{self.config['ICON']} {self.config['CUSTOM_NAME']} **Have been removed** from your account. If you believe this was incorrect or a mistake. Contact a server adminstrator or open a support ticket.",
                colour=profileManager.config['EMBED_COLOUR']
            )
            
            if not profileManager.config['EMBED_THUMBNAIL'] == None or profileManager.config['EMBED_THUMBNAIL'] == "":
               notifEmbed.set_thumbnail(profileManager.config['EMBED_THUMBNAIL'])
        
            if not profileManager.config['EMBED_IMAGE'] == None or profileManager.config['EMBED_IMAGE'] == "":
               notifEmbed.set_image(profileManager.config['EMBED_IMAGE'])
    
            if not profileManager.config['AUTHOR_NAME'] == None or profileManager.config['AUTHOR_NAME'] == "":
               notifEmbed.set_author(name=profileManager.config['AUTHOR_NAME'], icon=profileManager.config['AUTHOR_ICON'])
    
            if not profileManager.config['FOOTER'] == None or profileManager.config['FOOTER'] == "":
               notifEmbed.set_footer(text=profileManager.config['FOOTER'], icon=profileManager.config['FOOTER_ICON'])
            
            try:
                await self.user.send(embed=notifEmbed)
            except:
                Logging.error("I wasnt able to message user about point removal.")
            
        ## Update the embed for ease of access.
        
        updatedProfile = profileManager.fetch_profile(self.userId)[0] # Update the fetchProfile variable for the latest data to be displayed.
        panelEmbed = hikari.Embed(
               title=f"{profileManager.config['ICON']} Staff Panel",
               description=f"The staff panel for User {profileManager.config['CUSTOM_NAME']} Management.",
               colour=profileManager.config['EMBED_COLOUR'],
        )
            
        if not profileManager.config['EMBED_THUMBNAIL'] == None or profileManager.config['EMBED_THUMBNAIL'] == "":
            panelEmbed.set_thumbnail(profileManager.config['EMBED_THUMBNAIL'])
            
        panelEmbed.add_field(f"{profileManager.config['ICON']} {profileManager.config['CUSTOM_NAME']}", value=f"> {updatedProfile['points']}")
        panelEmbed.set_author(name=self.user.username, icon=self.user.make_avatar_url())
        panelEmbed.set_footer(f"Staff Member: {ctx.author.username} ({ctx.user.id})", icon=ctx.author.make_avatar_url())
        
        await ctx.edit_response(embed=panelEmbed)
    
    @miru.button(emoji="🛑", label="Close Panel", style=hikari.ButtonStyle.DANGER)
    async def stopPanel(self, ctx: miru.ViewContext, button: miru.Button) -> None:
        await ctx.edit_response(component=None)
        self.stop()
        return
        

# This command here is just how the lib works and is for decoration, this has no use. Note to the future contributor who says why the f**k is this here?

@plugin.command
@lightbulb.command("staff", description="Nani??")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def staff(ctx: lightbulb.Context):
    return

@staff.child
@lightbulb.option("user", "The user to manage in the panel.", type=hikari.Member)
@lightbulb.command("panel", "The staff panel for staff to add, remove & do other magic. 👀")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def panel(ctx: lightbulb.Context):
    profileManager = Profile()
    db = profileManager.db
    userId = ctx.options.user.id
    user: hikari.User = ctx.options.user
    
    if any(role_id in user.role_ids for role_id in profileManager.config['STAFF_ROLES']):
        pass
    else:
        return await ctx.respond("🛑 You are not allowed to run this command, you have **insufficent permissions.**", flags=hikari.MessageFlag.EPHEMERAL)
    
    if not profileManager.profile_exists(userId):
        profileManager.create_profile(userId)
        
    fetchProfile = profileManager.fetch_profile(userId)[0]
    panelEmbed = hikari.Embed(
        title=f"{profileManager.config['ICON']} Staff Panel",
        description=f"The staff panel for User {profileManager.config['CUSTOM_NAME']} Management.",
        colour=profileManager.config['EMBED_COLOUR'],
    )
    
    if not profileManager.config['EMBED_THUMBNAIL'] == None or profileManager.config['EMBED_THUMBNAIL'] == "":
        panelEmbed.set_thumbnail(profileManager.config['EMBED_THUMBNAIL'])
    
    panelEmbed.add_field(f"{profileManager.config['ICON']} {profileManager.config['CUSTOM_NAME']}", value=f"> {fetchProfile['points']}")
    panelEmbed.set_author(name=user.username, icon=user.make_avatar_url())
    panelEmbed.set_footer(f"Staff Member: {ctx.author.username} ({ctx.user.id})", icon=ctx.author.make_avatar_url())
    
    panelView = userPanel(timeout=9999)
    panelView.userId = userId
    panelView.user = user
    panelView.bot = ctx.bot
    
    await ctx.respond(embed=panelEmbed, components=panelView, flags=hikari.MessageFlag.EPHEMERAL)
    
    ctx.bot.d.miru.start_view(panelView)
    await panelView.wait()
    

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)