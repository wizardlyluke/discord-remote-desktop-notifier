# Discord Bot RDP Session Status Updater

This project is designed to update a Discord bot's status to "Remoting In" whenever a user is logged in via Remote Desktop on a Windows 11 machine. It checks for active RDP sessions at regular intervals and updates the bot's status accordingly.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- A Discord bot token (see [Discord's developer portal](https://discord.com/developers/applications) to create a bot and get a token)
- A machine running Windows 11 with Remote Desktop enabled

### Installation

1. Clone the repository to your local machine.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory of the project. Use the `.env.example` file as a template, replacing the placeholders with your actual data:

```plaintext
# .env file for Discord Bot and RDP Session Detector Project

# Discord Bot Token
DISCORD_BOT_TOKEN=your_discord_bot_token_here

# The ID of the Discord channel where the bot will update its status
DISCORD_CHANNEL_ID=your_discord_channel_id_here

# Status message to display when remoting in
DISCORD_STATUS_MESSAGE=your_status_message_here

# Interval in seconds for checking the RDP session
DISCORD_PING_INTERVAL_SECONDS=your_ping_interval_seconds_here

# The ID of the Discord server where the bot is active
DISCORD_SERVER_ID=your_discord_server_id_here

# Windows 11 Remote Desktop Session Information (Optional)
RDP_USERNAME=your_rdp_username_here
RDP_MACHINE_NAME=your_windows_11_machine_name_here


### Running the Project

To run the project, execute the `main.py` script:

```bash
python main.py
```

Upon starting, the script activates the Discord bot, which not only updates its status to "Remoting In" but also joins a voice channel whenever a Remote Desktop session is detected on the specified Windows 11 machine.

## Project Structure

- `config.json`: Configuration file for the Discord bot token, status message, and check interval.
- `requirements.txt`: File listing the necessary Python packages.
- `discord_bot.py`: Script for Discord bot operations.
- `rdp_session_detector.py`: Script to detect active RDP sessions.
- `main.py`: Main script that orchestrates the bot and RDP session detection.
- `.env`: Environment variables for Discord bot token and channel ID.
- `README.md`: This file, containing project documentation.
- `build.bat`: Run this to get a self contained exe file.

## Contributing

Feel free to fork the project and submit pull requests with improvements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open source and available under the [MIT License](LICENSE.md).
