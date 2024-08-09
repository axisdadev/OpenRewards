
![Logo](https://github.com/axisdadev/OpenRewards/blob/main/logo/BannerWithBg.png)

# OpenRewards

![Static Badge](https://img.shields.io/badge/mom_made-pizza_rolls-red)![Static Badge](https://img.shields.io/badge/python-version_3.12-blue)
![Static Badge](https://img.shields.io/badge/made_with-hikari_&_lightbulb-blue)


> An **open source**, **free to use** airline reward discord bot for **PTFS/PTC** Communities! Made using [hikari](<https://github.com/hikari-py/hikari>) and [hikari-lightbulb](<https://github.com/axisdadev/OpenRewards/blob/main/logo/BannerWithBg.png>), with a bit of [hikari-miru](<https://github.com/search?q=hikari-miru&type=repo>) dazzled in for staff panels.

Built with good intentions and the goal of customizability with easy setup to get started! 

**THIS PROJECT IS BEST RAN ON A SERVER IN A VIRTUAL ENV.**

# Basic setup

**Prerequistes**
- [Python 3.9+](<https://www.python.org/downloads/windows/>)
- [Virtual Environment](<https://docs.python.org/3/library/venv.html>)

To get the most basic setup of all, follow this quick guide. Download the project or fork it via git. This tutorial is for windows & linux only.

First to get started, create a virutal Environment using python.

**Windows:**
```python3 -m venv venv```


**Linux:** If pip is not in your system, install it via ```$ sudo apt-get install python-pip```, Then install if not already present install python3-venv ```sudo apt-get install python3-venv```, Then create your Virtual Environment via using the command ```python3 -m venv venv```.

Once completed, activate the Virtual Environment.

**Windows:** ```./venv/Scripts/activate```

**Linux:** ```source venv/bin/activate```

Next, install the nessecary packages for the program via running the command

```pip install -r requirements.txt```

Wait for installation to finish, once complete. Get your discord bot token via the discord developer website. Enable the users, guild and other intents as required. [Getting your token and setting up your bot for production.](<https://github.com/axisdadev/OpenRewards/blob/main/guides/production_bot/Guide.md>)

Once the bot has been invited and you have the token, open the ``config.yaml`` file, and insert it in the ``TOKEN`` field, You can delete the current ``config.yaml`` and replace it with ``default_config.yaml`` if you want a clean slate, if you want a premade version to test out the bot. Use the current config.

Once complete, and you're done filling out the configuration as wanted. Run your code via using the command. [Filling out the configuration.](<https://github.com/axisdadev/OpenRewards/blob/main/guides/configuring_the_file/Guide.md>)

```python main.py```

If you want to pass the optimization flag for possible better performance. Run the command.

``python -O main.py``


> **And tada! 🥳 You're all done!**

If you want more in depth and detailed guides on how to setup the correct permissions for the bot, i would recommend reading these below. Youtube video on how to set it up for production & more will come later down the line.

