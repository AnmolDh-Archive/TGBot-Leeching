#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Jigarvarma2005

import logging

import pyrogram
# the logging things
from tobrot import AUTH_CHANNEL
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    await message.reply_text("Hello \nI am Telegram Leech Robot! \nClick Below to know how to use me.", 
                             reply_markup=InlineKeyboardMarkup(
                                                               [
                                                                  [
                                                                   InlineKeyboardButton("Help", url=f"https://telegra.ph/Universal-Leecher-Help-Menu-03-18")
                                                                  ]
                                                               ]
                            ), disable_web_page_preview=True, parse_mode="markdown")
