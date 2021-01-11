#!/usr/bin/python3
"""
Copyright 2021 Leonid Maslakov <teaparanoid@protonmail.com>

License: GPL-3.0-or-later

    This file is part of mat-defender-bot.

mat-defender-bot is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

mat-defender-bot is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with mat-defender-bot.  If not, see <https://www.gnu.org/licenses/>.

See /usr/share/common-licenses/GPL-3, or
<https://www.gnu.org/licenses/gpl-3.0.txt> for the terms of the latest version
of the GNU General Public License.
"""

import os
import sys

config_file_path = "/etc/mat-defender.conf"

if os.path.isfile(config_file_path):
    import configparser
    config = configparser.ConfigParser()
    config.read(config_file_path)
    try:
        discord_bot_token = config.get("main", "discord_bot_token")
        dictionary = config.get("main", "dictionary")
        max_log_size_in_bytes = config.get("main", "max_log_size_in_bytes")
        log_backup_count = config.get("main", "log_backup_count")
        comment_to_delete_message = config.get("main", "comment_to_delete_message")
    except Exception:
        print("ERROR_CRITICAl:", "config file is not formatted correctly:", config_file_path)
        sys.exit(1)
else:
    print("ERROR:", "could not access the config file:", config_file_path)
    try:
        os.system("python3 /usr/bin/mat-defender-bot-reconfigure")
    except Exception:
        print("ERROR_CRITICAl:", "failed to create config file:", config_file_path)
        sys.exit(1)


log_dir = "/var/log/mat-defender"
log_file_path = log_dir+"/"+"mat-defender.log"

if os.path.isdir(log_dir):
    import logging
    #logging.basicConfig(format="[%(asctime)s] [%(levelname)s] => %(message)s")
    from logging.handlers import RotatingFileHandler
    logger = logging.getLogger("logger")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt="[%(asctime)s] [%(levelname)s] => %(message)s")
    handler = RotatingFileHandler(log_file_path, maxBytes=int(max_log_size_in_bytes), backupCount=int(log_backup_count))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
else:
    print("ERROR:", "could not access the logging folder:", log_dir)
    try:
        os.makedirs(log_dir)
    except Exception:
        print("ERROR_CRITICAl:", "failed to create folder for logs:", log_dir)
        sys.exit(1)


try:
    import discord
    from discord.ext import commands
except Exception:
    logger.critical("MAIN_ERROR_CRITICAl: " + "error importing library 'discord'")
    print("ERROR_CRITICAL:", "error importing library 'discord'")
    sys.exit(1)


class MyClient(discord.Client):
    async def on_ready(self):
        logger.info("MAIN_INFO: " + "logged on: " + "[" + str(self.user) + "]")

        logger.info("MAIN_INFO: " + "loading dictionary: " + "[" + str(self.user) + "] " + dictionary)
        if os.path.isfile(dictionary):
            global dictionary_list
            dictionary_list = []
            with open(dictionary, "r") as dictionary_file:
                for word in dictionary_file:
                    dictionary_list.append(word.rstrip())

            logger.info("MAIN_INFO: " + "dictionary loaded: " + "[" + str(self.user) + "] " + dictionary)
        else:
            logger.critical("MAIN_ERROR_CRITICAl: " + "could not access the dictionary file: " + "[" + str(self.user) + "] " + dictionary)
            print("ERROR_CRITICAl:", "could not access the dictionary file:", dictionary)
            sys.exit(1)


    async def on_guild_join(self, guild):
        logger.info("MAIN_INFO: " + "bot joined the server: " + "[" + str(self.user) + "] " + guild.name)

    async def on_message(self, message):
        logger.info("MAIN_INFO: " + "message received: " + "[" + str(self.user) + "] " + str(message.guild.name) + ": " + str(message.channel.name) + ": " + str(message.author) + " " + "(message ID: " + str(message.id) + ")")

        for word_num in range(len(dictionary_list)):
            if dictionary_list[word_num].lower() in message.content.lower():
                await message.delete()
                if comment_to_delete_message != "":
                    await message.channel.send(str(message.author) + ": " + str(comment_to_delete_message))
                    logger.info("MAIN_INFO: " + "message deleted"+"(comment: "+comment_to_delete_message+")"+": " + "[" + str(self.user) + "] " + str(message.guild.name) + ": " + str(message.channel.name) + ": " + str(message.author) + " " + "(message ID: " + str(message.id) + ")")
                else:
                    logger.info("MAIN_INFO: " + "message deleted quietly: " + "[" + str(self.user) + "] " + str(message.guild.name) + ": " + str(message.channel.name) + ": " + str(message.author) + " " + "(message ID: " + str(message.id) + ")")
                break


if __name__ == "__main__":
    try:
        client = MyClient()
        client.run(discord_bot_token)
    except Exception:
        logger.critical("MAIN_ERROR_CRITICAl: " + "Discord bot initialization error")
        print("ERROR_CRITICAl:", "Discord bot initialization error")
        sys.exit(1)
