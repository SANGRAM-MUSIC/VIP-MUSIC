from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
        InlineKeyboardButton(
            text="✯ 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 ✯",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ],
        [
      InlineKeyboardButton(text="🌷𝐉𝐨𝐢𝐧 𝐏𝐥𝐬🍒", url=f"https://t.me/VIP_CREATORS"),
      InlineKeyboardButton(text="🍒𝐂𝐨𝐦𝐞 𝐁𝐚𝐛𝐲😘", url=f"https://t.me/TG_FRIENDSS")
    ],
    [
      InlineKeyboardButton(text="★ 𝐎𝐰𝐧𝐞𝐫 ★", url=f"https://t.me/THE_VIP_BOY"),
      
  ],
]
)
pm_buttons = [
    [
        InlineKeyboardButton(
            text="✯ 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 ✯",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="🩸ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs🩸", callback_data="fallen_help")],
    [
      InlineKeyboardButton(text="🌷𝐉𝐨𝐢𝐧 𝐏𝐥𝐬🍒", url=f"https://t.me/VIP_CREATORS"),
      InlineKeyboardButton(text="🍒𝐂𝐨𝐦𝐞 𝐁𝐚𝐛𝐲😘", url=f"https://t.me/TG_FRIENDSS")
    ],
    [
        InlineKeyboardButton(
            text="🌱sᴏᴜʀᴄᴇ🌱", url="https://github.com/THE-VIP-BOY-OP/VIP-MUSIC"
        ),
        InlineKeyboardButton(text="★ 𝐎𝐰𝐧𝐞𝐫 ★", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="✯ 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 ✯",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
      InlineKeyboardButton(text="🌷𝐉𝐨𝐢𝐧 𝐏𝐥𝐬🍒", url=f"https://t.me/VIP_CREATORS"),
      InlineKeyboardButton(text="🍒𝐂𝐨𝐦𝐞 𝐁𝐚𝐛𝐲😘", url=f"https://t.me/TG_FRIENDSS")
    ],
    [
        InlineKeyboardButton(
            text="🌱sᴏᴜʀᴄᴇ🌱", url="https://github.com/THE-VIP-BOY-OP/VIP-MUSIC"
        ),
        InlineKeyboardButton(text="★ 𝐎𝐰𝐧𝐞𝐫 ★", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="✯ 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 ✯",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(
            text="❣️ᴇᴠᴇʀʏᴏɴᴇ❣️",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="🥀sᴜᴅᴏ🥀", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="🍁ᴏᴡɴᴇʀ🍁", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="✯ ʙᴀᴄᴋ ✯", callback_data="fallen_home"),
        InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"),
    ],
]


help_back = [
    [
        InlineKeyboardButton(
            text="✯ 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 ✯",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="🍒𝐂𝐨𝐦𝐞 𝐁𝐚𝐛𝐲😘", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="✯ ʙᴀᴄᴋ ✯", callback_data="fallen_help"),
        InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"),
    ],
]
