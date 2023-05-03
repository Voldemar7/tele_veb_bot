# Description of the bot for user authorization
___

This bot is written in Aiogram3 and is intended for user authorization. Users can create a username and password using the __/register__ command.

User data such as id, username, and fullname are stored in a SQLite3 database along with the usernames and passwords they create using the __/save_data__ command.

The bot code is not included in this file, but can be found in the corresponding project files.

## Installation requirements
To run the bot, you must have the following dependencies installed:

1. Python 3.7 or higher
2. Aiogram 3.0 or higher
3. SQLite3.

### Installation and launch instructions:

Download or clone the repository with the bot code.

Create a folder __.env__ in the project directory and place the __bot token key__ there, there is an example in __.env.example__.

Install all the necessary dependencies using the command `pip install -r requirements.txt`.

Run the bot with the command `python main.py`.

Use the __/register__ and __/save_data__ commands to create and save authorization data.