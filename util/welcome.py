from discord.ext.commands import Cog, command
import discord
from .base import Base
from .statics import STATICS
from os import path

def welcome_message():
    return '''--- DEMO MESSAGE ---
**Willkommen**

Hallo **{}**, Willkommen auf dem Discord Server der WoW Classic Gilde **Solitaire** auf dem EU-Server Transcendence.
Bitte ändere deinen Discord-**Nicknamen** in deinen **Ingame-Namen**.

Damit du dich auf unserem Discord bewegen kannst, wähle bitte auch deine aktive Klasse aus, dann bekommst du automatisch die nötigen Rechte.
--- DEMO MESSAGE ---
'''


class Welcome(Base):
    def __init__(self, bot, dev_mode):
        super().__init__(bot)
        self.dev_mode = dev_mode
        try:
            with open(path.join('.', 'welcome.txt')) as file:
                self.welcome_message = file.read()
        except IOError as ioe:
            print('IOError', ioe)
            self.welcome_message = welcome_message()

    @command()
    async def welcome(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        msg = await self.send_dm(member, self.welcome_message.format(member.name))
        await self.add_classes(msg)

    @Cog.listener()
    async def on_member_join(self, member):
        try:
            dm = await self.send_dm(member, self.welcome_message.format(member.name))
            await self.add_classes(dm)
        except Exception as ex:
            print(ex)
