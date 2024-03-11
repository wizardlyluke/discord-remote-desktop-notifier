import discord_bot
import rdp_session_detector
import asyncio

async def check_rdp_and_update_status():
    """
    Checks if a user is logged in via Remote Desktop and updates the Discord bot status accordingly.
    """
    # Create an instance of the Discord bot
    bot = discord_bot.DiscordBot()

    # Override the update_status_task loop in the DiscordBot class
    @bot.update_status_task.before_loop
    async def before_update_status():
        await bot.wait_until_ready()  # Ensure the bot is ready before starting the loop

    @bot.update_status_task.loop(seconds=bot.check_interval_seconds)
    async def update_status_task():
        # Use the is_user_remoting function to check for RDP sessions
        if rdp_session_detector.is_user_remoting():
            # If a user is remoting in, update the bot's status message
            await bot.change_presence(activity=discord.Game(name=bot.status_message))
        else:
            # If no user is remoting in, clear the bot's status message
            await bot.change_presence(activity=None)

    # Run the bot
    bot.run(bot.config['discord_bot_token'])

if __name__ == '__main__':
    asyncio.run(check_rdp_and_update_status())
