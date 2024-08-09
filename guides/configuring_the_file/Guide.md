# Configuring your configuration file.

> 👋 **Hi there!** In this tutorial. I will go over a brief explaination of the configuration file, what each one does & More! Without further ado. Lets get into it!

**Part 1**
Basic configuration part of the file.

```
TOKEN: "" # The bot token, retrive from https://discord.com/developers/applications
LOGGING: true # Enable basic logging for actions caused by the bot, user or more. Example: [LOG] Created profile for axisdadev (998819061817413652)
USER_DB: "data/users.json" # The name of the database used to store user data. Default = "data/users.json" 
STAFF_ROLES: [1270948998248927253] # The list of staff role ids that are able to give users points and currency. Example: [1260625936685076613, 1260646882741456949]
VERSION: "0.0.1 DEV" # Updated from github, touch if wanted. This doesnt affect much
```

The comments are already self explaintory, ``TOKEN`` is your bot's token, You can learn how to setup your bot for production in [This Guide](<https://github.com/axisdadev/OpenRewards/blob/main/guides/production_bot/Guide.md>)

> The ``LOGGING`` variable is either to enable or disable output logs in the python program. Example: [LOG] Created profile for axisdadev (998819061817413652) (Not recommended to disable!)

> The ```USER_DB`` variable is a string type, leading to where the data storing with TinyDB shall be located. This must be a .json file with the name "users"

> The ```STAFF_ROLES`` variable is a list with snowflake types, of the discord role ids. Developer mode must be enabled to get a role id. Learn how to enable it [here](<https://www.howtogeek.com/714348/how-to-enable-or-disable-developer-mode-on-discord/>), Right click on a users role or in the role management page to get them.

> The ```VERSION``` variable Is updated through github, this wont affect much if changed. feel free to do so!

**Part 2**
Customization

```
CUSTOM_NAME: "Southwest Points" # Set a custom name for the points/rewards system. Example: American Miles, Southwest Points, Miles, Points
ICON: "<:SWAIcon:1270867620673097820>" # Set a discord emoji for the points/rewards icon. Example: <:SWAHeart:1260662835772657718>

STATUS: true # Allow the bot to put quotes as its status.
STATUS_OPTIONS: ["Fly Southwest!", "Low fares, no hidden fees. Thats TransFarency!", "Save up to 50% on your next flight!"] # The options that can be the statuses. Example: "Join Southwest!", "Fly american!", Or something silly. "I have 10 children locked in my basement."
CHANGE_INTERVAL: 30 # The interval to change the status options.
```

> The ``CUSTOM_NAME`` variable is a string for the name of your rewards/point system. This can be whatever you want.

> The ``ICON`` variable is a string for the icon of your points in discord, This can be left blank or set to a discord emoji. To set it to a discord emoji. Go to the discord developers page. Click on your bot and find where the "EMOJIS" Tab is, upload your emoji. Once uploaded. Click the copy button that says "Copy Markdown" and set it to that variable.

> The ``STATUS`` Variable is to enable or disable the bot status options. 

> The ``STATUS_OPTIONS`` Variable is to make a list of the statuses that will be randomly picked over a time interval. Example ["Test 1", "Test 2", "Test 3"].

> The ``CHANGE_INTERVAL`` Variable is a interger to define the amount of time before the statuses switch.

** Part 3**
Embed/Profile Customization


```
GREET_MSG: "<:SWAIcon:1270867620673097820> Hiya!, {user}!" # The greeting message when running the /profile command. {user} Will be replaced with username. Example: Good day, {user} will look like Good day, axisdadev.
PRIVATE: true # Make the embed invisble/ephermal to other users?


EMBED_THUMBNAIL: "https://cdn.discordapp.com/attachments/1260626688728109137/1263045210011865118/0a92d260-9421-461e-8ce7-cc69de2252ab.png?ex=66b52644&is=66b3d4c4&hm=0005eda473003cbb0cd30838ec40716b41c9c074d8cafb7021345314a65a02e6&" # Add a discord media link to put as the image.
EMBED_IMAGE: "https://cdn.discordapp.com/attachments/1260626688728109137/1270499844414378037/SWA_Advert_2024_Ver4.png?ex=66b53e2f&is=66b3ecaf&hm=606be46d8e9705d13b96d9ec6fe99d43197e158e3b683f9833ad67b2e063c1e9&" # Add a discord media link to put as the thumbnail/icon of the embed.
EMBED_COLOUR: "#1b2d83" # Set a hexidecimal color code to put as the embed colour. Example: #FFD700
EMBED_DESCRIPTION: "Good day, **Ready to fly, {user}?**" # The description of the embed. Example: Here are your points, {user}. will look like Here are your points, axisdadev.

AUTHOR_NAME: "Southwest Rapid Rewards"
AUTHOR_ICON: "https://cdn.discordapp.com/attachments/1260626688728109137/1270401886222159963/quicktemp.png?ex=66b4e2f4&is=66b39174&hm=f51491b112a70e4a4971d06578f13efa3a4eb9779d57031a2edf3883c0304ad0&"
FOOTER: "Copyright Southwest PTFS 2024"
FOOTER_ICON: "https://cdn.discordapp.com/attachments/1260626688728109137/1270401886222159963/quicktemp.png?ex=66b4e2f4&is=66b39174&hm=f51491b112a70e4a4971d06578f13efa3a4eb9779d57031a2edf3883c0304ad0&"
```

> The ``GREET_MSG`` Variable is what to set the title of the embed to.

> The ``PRIVATE`` Variable is rather to set the variable ephermal/invisible to other users. False = Visible to others, True = Invisible to others.

> The ``EMBED_THUMBNAIL`` Variable is a media link for the embed, for the little icon in the top right.

> The ``EMBED_IMAGE`` Variable is a media link for the embed, for the image at the bottom.

> The ``EMBED_COLOUR`` Variable is a hexidemical code for the embed.

> The ``EMBED_DESCRIPTION`` Variable is self explainatory, the description of the embed.

> The ```AUTHOR_NAME`` Variable is self explainatory, the author name of the embed.

> The ```AUTHOR_ICON`` Variable is self explainatory, the icon for the author of the embed, Must be discord media link or other.

> The ``FOOTER`` Variable is self explainatory, the footer text of any embed.

> The ``FOOTER_ICON`` Variable is self explainatory, the icon for the footer of the embed, Must be discord media link or other.


**Part 4**
Staff limits.

```
MAXIMUM_ADD: 10000 # The maximum points a staff member is able to add to a user at once, Recommended 10000.
MAXIMUM_SUB: 10000 # The maximum points a staff member is able to remove from a user at once, Recommended 10000.
BYPASS_ROLE: [1270949019677495378] # Set a list of roles or one that allow this limit to be bypassed. Example: [1260625936685076613, 1260646882741456949]
```
> The ```MAXIMUM_ADD`` Variable is a integer of the maxium points a staff member is allowed to add.

> The ```MAXIMUM_SUB`` Variable is a integer of the maxium points a staff member is allowed to remove.

> The ```BYPASS_ROLE`` Variable is a list of the allowed staff role ids that can bypass these restrictions, Only give this to trusted users.

**Part 5**
Notifications & Discord logging

```
ENABLE_USER_NOTIFS: true # Enable user notifications for points given and removed.
ENABLE_DISCORD_LOGS: true # Enable discord logging for staff point additions and subtractions.
DISCORD_LOG_CHANNEL: 1270952470461546598 # A channel ID to set where logs will be posted. Confirm bot has permission to send messaages in that channel.
```

> The ``ENABLE_USER_NOTIFS`` Variable is to notify the user when their points are added to and removed from them. False = No notification, True = Will send a notification.

> The ``ENABLE_DISCORD_LOGS`` Variable is to enable discord sided logging in channels for staff transactions and changes.

> The ``DISCORD_LOG_CHANNEL`` Variable is to point the bot where to send messages to log, must be a channel id.
