import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["علاوي","علوش","علش","المطور","Alsh","علي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("BxxBxxL")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━━˛ َِ𝗔َِ𝗹َِ𝘀َِ𝗵 .¹# ‌♡⁩━━⩺\n\n‍ ¦dev :{name}\n ¦user :@{usr.username}\n ¦id :`{usr.id}`\n ¦bio :{usr.bio}\n\n**⩹━━˛ َِ𝗔َِ𝗹َِ𝘀َِ𝗵 .¹# ‌♡⁩━━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
