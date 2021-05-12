#!/usr/bin/env python3

from discord.ext.commands import Bot
from discord import Intents
from dotenv import load_dotenv
import os
import sys
from util.change_class import ChangeClass
from util.welcome import Welcome


def main():
    intents = Intents.default()
    intents.members = True

    bot = Bot(command_prefix='$', intents=intents)

    cc = ChangeClass(bot)
    welcome = Welcome(bot)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')

    bot.add_cog(cc)
    bot.add_cog(welcome)

    load_dotenv()

    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as interrupt:
        sys.exit(2)
    except Exception as ex:
        print(ex)
        sys.exit(1)
