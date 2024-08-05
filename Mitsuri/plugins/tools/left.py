
import asyncio
import os
from Mitsuri import app
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup



# Define a handler for when a user leaves, is banned, or is kicked from a group
@app.on_chat_member_updated()
async def handle_user_update(client: Client, message: Message):
    # Check if the user was banned, kicked, or left
    if message.new_chat_member is None:
        action = "left"
    elif message.new_chat_member.status == "kicked":
        action = "kicked"
    elif message.new_chat_member.status == "banned":
        action = "banned"
    else:
        return

    # Get the user's information
    user = message.from_user

    # Check if the user is already in the banned list
banned_users = []
    if user.id in banned_users:
        return

    # Add the user to the banned list
    banned_users.append(user.id)

    # Send a message to the group with the user's photo and caption
    await message.reply_video(
        video="https://telegra.ph/file/0afc7e12967295d0414ce.mp4",
        caption=f"{user.first_name} has been {action} from the group.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Unban", callback_data=f"unban_{user.id}")
                ]
            ]
        ),
    )


# Define a handler for when the bot receives a callback query
@app.on_callback_query()
async def handle_callback_query(client: Client, callback_query: Message):
    # Check if the callback query is for unbanning a user
    if callback_query.data.startswith("unban_"):
        # Get the user's ID from the callback data
        user_id = int(callback_query.data.split("_")[1])

        # Remove the user from the banned list
        banned_users.remove(user_id)

        # Send a message to the group that the user has been unbanned
        await callback_query.answer(f"User has been unbanned.")

        # Send a message to the unbanned user
        await client.send_message(user_id, "You have been unbanned from the group.")