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

import configparser
import sys

config_file_path = "/etc/mat-defender.conf"


def reconfiguration():
    print("reconfiguration...")
    print("config file is located at:", config_file_path)

    config = configparser.ConfigParser(allow_no_value=True)
    config.add_section("main")
    config.set("main", "# Discord bot token.")
    config.set("main", "discord_bot_token", "")
    config.set("main", "# Location dictionary with forbidden words.")
    config.set("main", "dictionary", "/usr/share/dict/mat")
    config.set("main", "# Maximum size of 1 log in bytes.")
    config.set("main", "max_log_size_in_bytes", "5242880")
    config.set("main", "# Count of log backups.")
    config.set("main", "log_backup_count", "2")
    config.set("main", "# Comment on deleting a message. Leave blank if you want to silently delete messages.")
    config.set("main", "comment_to_delete_message", "в сообщении содержался мат, оно было удалено")

    with open(config_file_path, "w") as config_file:
        config.write(config_file)

if __name__ == "__main__":
    try:
        reconfiguration()
    except Exception:
        print("ERROR:", "failed to create config file")
        sys.exit(1)
