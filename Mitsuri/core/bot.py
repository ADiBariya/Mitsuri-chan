from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Mitsuri(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Mitsuri Starting...")
        super().__init__(
            name="Mitsuri",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    
async def start(self):
    await super().start()
    self.id = self.me.id
    self.name = self.me.first_name + " " + (self.me.last_name or "")
    self.username = self.me.username
    self.mention = self.me.mention

    try:
        await self.send_video(
            chat_id=config.LOGGER_ID,
            video="https://telegra.ph/file/7cd62280c13f48450c498.mp4",
            caption=f"🧚 Bot Is Alive Now 🧚",
        )
    except (errors.ChannelInvalid, errors.PeerIdInvalid):
        LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote your bot as an admin in your log group/channel."
            )
            exit()
        LOGGER(__name__).info(f"Mitsuri Started as {self.name}")

    async def stop(self):
        await super().stop()
