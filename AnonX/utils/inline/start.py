from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✧ أضفني إلى مجموعتك ✧",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="مساعدة",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="الإعدادات", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✧ أضفني إلى مجموعتك ✧",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="مساعدة", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✧ المساعدة ✧", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="˛ َِ𝗔َِ𝗹َِ𝘀َِ𝗵 .¹#", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="᷂للحزن ᷂ابواب",
                url=f"https://t.me/P8EEO",
            )
        ],
     ]
    return buttons
