import json
from telegram import Bot
from telegram.error import TelegramError
import asyncio
import logging

from domain.general.messenger import Messenger


class TelegramMessenger(Messenger):
    def __init__(self, token: str, chat_id: str | int):
        """
        Initialize Telegram messenger with bot token and chat ID

        Args:
            token (str): Telegram Bot API token obtained from BotFather
            chat_id (str | int): Telegram chat ID or username
        """

        self.bot = Bot(token=token)
        self.chat_id = chat_id
        self.logger = logging.getLogger(__name__)

    async def send(self, message: dict) -> bool:
        """
        Send a message to a specified chat

        Args:
            chat_id (str|int): Telegram chat ID or username
            text (str): Message text to send

        Returns:
            bool: True if message was sent successfully, False otherwise
        """
        try:
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=self.format_message(message),
                parse_mode="HTML",
            )
            return True
        except TelegramError as e:
            self.logger.error(f"Failed to send Telegram message: {str(e)}")
            return False

    def send_message_sync(self, chat_id: str | int, text: str) -> bool:
        """
        Synchronous wrapper for send_message

        Args:
            chat_id (str|int): Telegram chat ID or username
            text (str): Message text to send

        Returns:
            bool: True if message was sent successfully, False otherwise
        """
        return asyncio.run(self.send_message(chat_id, text))

    def format_message(self, message: dict) -> str:
        return json.dumps(message)
