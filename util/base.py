from .statics import STATICS
from discord.ext.commands import Cog


class Base(Cog):
    def __init__(self, bot):
        self.bot = bot

    async def send_dm(self, user, text):
        try:
            if user:
                dm = await user.create_dm()
                dmsg = await dm.send(text)
                return dmsg
        except Exception as ex:
            print('Error sending dm', ex.message)

    async def add_classes(self, msg):
        try:
            if msg:
                for react in STATICS.WOW_CLASSES_EMOJIS:
                    await msg.add_reaction(react)
        except Exception as ex:
            print('Error adding reactions to dm', ex.message)

    async def get_guest_role(self):
        try:
            roles = await self.bot.guilds[0].fetch_roles()
            role = list(filter(lambda x: x.name == STATICS.GUEST, roles))
            return role[0]
        except Exception as ex:
            print('Error fetching guest role', ex.message)
