import os
import urllib.parse
from telethon import TelegramClient, events

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION = os.environ["SESSION"]

client = TelegramClient("userbot", API_ID, API_HASH)

afk_reason = None

MENU = """
╭━━━『 MEGUMI USERBOT 』━━━╮
┃
┃  USERBOT
┃
┃  .menu
┃  .afk <reason>
┃  .unafk
┃  .alive
┃  .ping
┃  .id
┃
┃  MUSIC
┃
┃  +song <song name>
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
"""


# =========================
# MENU
# =========================

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.menu$"))
async def menu(event):
    await client.send_message("me", MENU)
    await event.delete()


# =========================
# AFK
# =========================

@client.on(
    events.NewMessage(
        outgoing=True,
        pattern=r"^\.afk(?:\s+(.+))?$"
    )
)
async def afk(event):
    global afk_reason

    reason = event.pattern_match.group(1)
    afk_reason = reason.strip() if reason else "AFK"

    await event.edit(f"AFK enabled: {afk_reason}")


@client.on(events.NewMessage(outgoing=True, pattern
