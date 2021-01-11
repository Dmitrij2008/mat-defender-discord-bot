#!/bin/bash
cp src/mat-defender-bot.py /usr/bin/mat-defender-bot
cp src/mat-defender-bot-reconfigure.py /usr/bin/mat-defender-bot-reconfigure

cp mat /usr/share/dict/mat

cp sys/mat-defender-bot.service /lib/systemd/system/mat-defender-bot.service

mkdir -p /usr/share/doc/mat-defender-bot
cp copyright /usr/share/doc/mat-defender-bot/copyright

mkdir -p /var/log/mat-defender

python3 /usr/bin/mat-defender-bot-reconfigure

chmod +x /usr/bin/mat-defender-bot
chmod +x /usr/bin/mat-defender-bot-reconfigure
chmod 600 /etc/mat-defender.conf
chmod 644 /lib/systemd/system/mat-defender-bot.service
chmod 644 /usr/share/dict/mat
chmod 600 /log/mat-defender
