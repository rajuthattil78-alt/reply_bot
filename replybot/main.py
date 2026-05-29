import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import bot

# Bot token provided by the user
TOKEN = bot.Bot_Token

dp = Dispatcher()

# --- Keyboard Setup ---
# Creating the reply keyboard with your specific buttons
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Send ID")],
        [KeyboardButton(text="Matching orders")],
        [KeyboardButton(text="Keep UPI online")]
    ],
    resize_keyboard=True, # Makes the buttons fit nicely on mobile screens
    input_field_placeholder="Select an option from below"
)

# --- Handlers ---

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(
        f"Hello, {html.bold(message.from_user.full_name)}!\n"
        f"Please click one of the keyboard options below to proceed.",
        reply_markup=main_keyboard
    )

@dp.message(F.text == "Send ID")
async def send_id_handler(message: Message) -> None:
    """Handles the 'Send ID' button press"""
    response_text = (
        "Please send your ID.\n"
        "Please explain your problem in one sentence."
    )
    await message.answer(response_text)

@dp.message(F.text == "Matching orders")
async def matching_orders_handler(message: Message) -> None:
    """Handles the 'Matching orders' button press"""
    await message.answer("The system will automatically match orders for you.")

@dp.message(F.text == "Keep UPI online")
async def keep_upi_handler(message: Message) -> None:
    """Handles the 'Keep UPI online' button press"""
    await message.answer("Keep your UPI online, and the system will automatically add funds to your account.")


# --- Main Startup Logic ---
async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    # And the run events dispatching
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())