from discord.ext.commands import Cog, command
import discord
from .base import Base
from .statics import STATICS


def welcome_message(member):
    return f'''--- DEMO MESSAGE ---
**Willkommen**

Hallo **{member.name}**, Willkommen auf dem Discord Server der WoW Classic Gilde **Solitaire** auf dem EU-Server Transcendence
Dies sind unsere Community-Regeln:
    ...
    ...

Bitte ändere deinen Discord-**Nicknamen** in deinen **Ingame-Namen**.

Damit du dich auf unserem Discord bewegen kannst, wähle bitte auch deine aktive Klasse aus, dann bekommst du automatisch die nötigen Rechte
--- DEMO MESSAGE ---
'''


class Welcome(Base):
    @command()
    async def welcome(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        msg = await self.send_dm(welcome_message(member))
        await self.add_classes(msg)

    @Cog.listener()
    async def on_member_join(self, member):
        try:
            dm = await self.send_dm(member, welcome_message(member))
            await self.add_classes(dm)
            await member.add_roles(await self.get_guest_role(), reason='bot changed roll because of command')
        except Exception as ex:
            print(ex)
