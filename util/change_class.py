from discord.ext.commands import Cog, command
import discord
from .statics import STATICS
from .base import Base


class ChangeClass(Base):
    @command()
    async def solitaire_class(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if member:
            msg = await self.send_dm(member, f'Hallo **{member.name}**, du möchtest deine Klasse ändern? Welche Klasse spielst du aktuell?')
            await self.add_classes(msg)

    @Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        if (reaction.user_id != self.bot.user.id):
            member = await self.get_member(reaction.user_id)
            
            reacted_msg = await member.fetch_message(reaction.message_id)
            if reaction.emoji.name in STATICS.WOW_CLASSES_EMOJIS or str(reaction.emoji.id) in STATICS.EMOJI_IDS:
                if not self.is_member(member) and not self.is_guest(member):
                    await member.add_roles(await self.get_guest_role(), reason='bot changed roll because of command')
                print(f'{member.name} choose {reaction.emoji.name}')
                my_reactions = list(
                    filter(lambda x: x.me, reacted_msg.reactions))
                for react in my_reactions:
                    await reacted_msg.remove_reaction(react, self.bot.user)
                changed = await self.change_role(member, reaction.emoji)
                if changed:
                    answer = await self.send_dm(member, f'Willkommen {reaction.emoji.name}! Möchtest du deine Klasse ändern, sende mir ein `$solitaire_class` zu.')
                else:
                    answer = await self.send_dm(member, f'Ich konnte deine Klasse leider nicht ändern. Probiere es noch einmal, oder melde dich bei einem Offizier!')
            else:
                print(f'something else: {reaction.emoji.name}')

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

    async def change_role(self, member, role_name):
        try:
            if role_name:
                if self.is_member(member):
                    roles = STATICS.SOLITAIRE_ROLES
                    role = await self.get_role(role_name)
                else:
                    roles = list(
                        map(lambda x: f'{x} (Gast)', STATICS.SOLITAIRE_ROLES))
                    role = await self.get_role(role_name, True)
                all_roles = await self.get_roles(roles)
                await member.remove_roles(*all_roles, reason='bot change role because of command')
                await member.add_roles(*role, reason='bot changed roll because of command')
                return True
        except discord.errors.Forbidden as fe:
            print(fe)
        except Exception as ex:
            print(ex)

    async def get_member(self, user_id):
        try:
            return await self.bot.guilds[0].fetch_member(user_id)
        except Exception as ex:
            print('Error fetching member', ex.message)

    async def get_role(self, emoji, guest=False):
        try:
            if emoji:
                prefix = ' (Gast)' if guest else ''
                roles = await self.bot.guilds[0].fetch_roles()
                role = list(filter(lambda x: x.name ==
                            f'{STATICS.SOLITAIRE_ROLES_MAP[emoji.name]}{prefix}', roles))
                return role
        except Exception as ex:
            print('Error fetching roles', ex.message)

    async def get_roles(self, names):
        try:
            if names and len(names) > 0:
                roles = await self.bot.guilds[0].fetch_roles()
                roles = list(filter(lambda x: x.name in names, roles))
                return roles
        except Exception as ex:
            print('Error fetching roles', ex)

    def is_member(self, member):
        boolean = STATICS.MEMBER in list(map(lambda x: x.name, member.roles))
        return boolean

    def is_guest(self, member):
        boolean = STATICS.GUEST in list(map(lambda x: x.name, member.roles))
        return boolean
