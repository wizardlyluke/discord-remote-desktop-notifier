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

3. Create a `.env` file in the root directory of the project with the following content, replacing the placeholders with your actual data:

```plaintext
# .env file for Discord Bot and RDP Session Detector Project

# Discord Bot Token
DISCORD_BOT_TOKEN=your_discord_bot_token_here

# The ID of the Discord channel where the bot will update its status
DISCORD_CHANNEL_ID=your_discord_channel_id_here

# Windows 11 Remote Desktop Session Information (Optional)
RDP_USERNAME=your_rdp_username_here
RDP_MACHINE_NAME=your_windows_11_machine_name_here
```

4. Update the `config.json` file with your Discord bot token and preferred status message (optional if you've set everything in the `.env` file):

```json
{
  "discord_bot_token": "YOUR_DISCORD_BOT_TOKEN_HERE",
  "status_message": "Remoting In",
  "check_interval_seconds": 10
}
```

### Running the Project

To run the project, execute the `main.py` script:

```bash
python main.py
```

The script will start, and the Discord bot will update its status to "Remoting In" whenever a Remote Desktop session is active on the specified Windows 11 machine.

## Project Structure

- `config.json`: Configuration file for the Discord bot token, status message, and check interval.
- `requirements.txt`: File listing the necessary Python packages.
- `discord_bot.py`: Script for Discord bot operations.
- `rdp_session_detector.py`: Script to detect active RDP sessions.
- `main.py`: Main script that orchestrates the bot and RDP session detection.
- `.env`: Environment variables for Discord bot token and channel ID.
- `README.md`: This file, containing project documentation.

## Contributing

Feel free to fork the project and submit pull requests with improvements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open source and available under the [MIT License](LICENSE.md).
