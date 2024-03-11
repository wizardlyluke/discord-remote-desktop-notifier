import discord
import asyncio
import os
import logging
from discord.ext import tasks
from dotenv import load_dotenv
from rdp_session_detector import is_user_remoting

import sys

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

env_path = os.path.join(application_path, '.env')
load_dotenv(env_path)
logging.basicConfig(level=logging.INFO)

server_id = int(os.getenv('DISCORD_SERVER_ID', '0'))

class DiscordBot(discord.Client):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()  # This enables the default intents
        intents.members = True  # Enable intents for members if needed
        intents.messages = True  # Enable intents for messages if needed
        super().__init__(*args, **kwargs, intents=intents)
        # Load configuration from environment variables
        self.status_message = os.getenv('DISCORD_STATUS_MESSAGE', 'Remoting In')
        self.check_interval_seconds = int(os.getenv('DISCORD_PING_INTERVAL_SECONDS', 10))
        self.voice_client = None

    async def on_ready(self):
        logging.info(f'Logged in as {self.user} (ID: {self.user.id})')
        logging.info('------')
        self.manage_status_and_voice_channel_task.start()  # Start the loop when the bot is ready

    @tasks.loop(seconds=10)
    async def manage_status_and_voice_channel_task(self):
        try:
            # Check if a user is logged in via RDP
            if is_user_remoting():
                logging.info('User is remoting in, updating the bot status message and joining the voice channel if not already connected.')
                # If a user is remoting in, update the bot's status message
                await self.change_presence(activity=discord.Game(name=self.status_message))
                # Join the voice channel if not already connected
                if not self.voice_client or not self.voice_client.is_connected():
                    for guild in self.guilds:
                        for channel in guild.voice_channels:
                            if channel.id == server_id:
                                self.voice_client = await channel.connect()
                                logging.info(f'Joined voice channel: {channel.name}')
                                break
            else:
                # If no user is remoting in, clear the bot's status message and leave the voice channel
                logging.info('No user is remoting in, clearing the bot status message and leaving the voice channel.')
                await self.change_presence(activity=None)
                if self.voice_client and self.voice_client.is_connected():
                    await self.voice_client.disconnect()
                    logging.info('Left the voice channel as no active remote desktop sessions.')
                    self.voice_client = None
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    # Load the bot token from the environment variables
    bot_token = os.getenv('DISCORD_BOT_TOKEN')

    # Create and run the bot
    bot = DiscordBot()
    try:
        bot.run(bot_token)
    except Exception as e:
        logging.error(f"Failed to run the bot: {e}")

