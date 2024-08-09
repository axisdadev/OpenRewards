
# Setting up your Bot [In detail]

> **In this guide, we will go over how to configure your bot on discord.com/applications, get it ready for production & more!**

To get started, head over to https://discord.com/developers/applications And log into your discord account. Once logged in. You should see *a screen similar* to **this**

![Home Page](<image/shome.png>)

In the top right corner, click on "New Application"

![The new application button](<images/new_app.png>)

In this prompt, fill out the name you want for your Bot, im going to call it OpenRewards Testing for this tutorial.

![The prompt](<images/bot_creation_step1.png>)

Agree to discords developer terms aswell.

![Details filled](<images/bot_details_filled.png>)

Click on the "Create" Button, once complete. You should see a page like **this**.

![New Bot Page](<images/new_bot_page.png>)

Fill out the details on the page as wanted, **Eg: Name, Icon & More.**, I have now filled mine out how i like it.

![Profile Made](<images/bot_profile_made.png>)

## Setting the intents

This next step is CRUICIAL, to your bot working, so follow carefully. On the page we were just on, on the middle left of the screen, find the tab that says "Bot"

![Selecting bot on the page](<images/select_bot_settings.png>)

Once clicked on the page should **look like this.**

![Bot config page](<images/bot_settings_page.png>)

Scroll down on that page until you see the words "Privileged Gateway Intents", Once found. Enable these gateway intents shown.

![Intents](<images/intents.png>)

Also make sure to save your changes, or they wont take place.
Great! That step is now complete. Time to retrive our bot token and put it in our configuration now!

Scroll back up to the bot settings page, and click on the Reset Token button. This is how it should look.

![Reset Token](<images/reset_token.png>)

Once clicked on, you will be prompted with this. Click on "Yes, do it!"

![Reset Token Prompt](<images/reset_token_prompt.png>)

Authenticate with a multi factor security key or anything else as required. Once completed, your token should be ready to go on the page, Copy it where its marked.

![I didnt leak my token dw](<images/token_gen.png>)

One completed, paste that into the ``TOKEN`` field of your configuration.yaml file.
> ⚠️ **Fair warning, NEVER Share your bot token. If your bot has the right permissions in many servers. It can result in a rouge user nuking and deleting all of the channels, roles & messages.**

![Pasting into place](<images/token_Yaml.png>)

> 🎉🥳 **Congrats!** You're done with this step! Now onto the next one :)

## Inviting/Authorizing the bot

Now for the final part, inviting and Authorizing your bot.

Head back over to the main page and find the OAuth2 tab.

![OAuth2](<images/oAuthPointer.png>)

Click on it and you will be greeted with this.

![OAuth2](<images/oauthgreet.png>)

Click on the little box that says ``Bot``

![Box highlighted](<images/oath_bot_clicked.png>)

Once completed, everything should look like this.

![Bot permissions](<bot_permissions.png>)

Click on nessecary permissions as required, i recommend adding "Send Messages", "Embed Links", "Attach files", Add whatever else floats your boat. Do not turn on "ADMINSTRATOR", as it is not needed with the warning above. Besides that. Once completed, look below for the invite link and copy it.

![Invite Copy](<copy_invite.png>)

Once copied, paste your link into the browser. It should look something like this

![Authorization](<authorization_final.png>)

Click on the dropdown below and invite to the selected server. Once complete. Click "Continue", The new page should look like this. 


![Authorization](<authorization_perms.png>)

Next, click on "Authorize", If all is good. You should get a sucess message and a notification that the bot has joined that server!

![Final](<openrewards_invited.png>)

And **tada! 🥳🎉**, you're all done! Configure whats needed in your config.yaml, and run the bot, It should work. If you have any issues, Please open a [Github Issue](<https://github.com/axisdadev/OpenRewards/issues>) for the time being.

I hope this tutorial helped!