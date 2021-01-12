#!/bin/bash
echo copy files
cp src/mat-defender-bot.py /usr/bin/mat-defender-bot
cp src/mat-defender-bot-reconfigure.py /usr/bin/mat-defender-bot-reconfigure
cp uninstall.sh /bin/mat-defender-bot-uninstall

cp mat /usr/share/dict/mat

cp sys/mat-defender-bot.service /lib/systemd/system/mat-defender-bot.service

mkdir -p /usr/share/doc/mat-defender-bot
cp copyright /usr/share/doc/mat-defender-bot/copyright

mkdir -p /var/log/mat-defender

if [ -e $HOME/testing ]
then
echo config creation
python3 /usr/bin/mat-defender-bot-reconfigure
else
echo the config already exists
echo if you want to reconfigure do: python3 / usr / bin / mat-defender-bot-reconfigure
fi

echo setting access rights
chmod +x /usr/bin/mat-defender-bot
chmod +x /usr/bin/mat-defender-bot-reconfigure
chmod 600 /etc/mat-defender.conf
chmod 644 /lib/systemd/system/mat-defender-bot.service
chmod 644 /usr/share/dict/mat
chmod 600 /log/mat-defender
chmod 755 /usr/bin/mat-defender-bot-reconfigure
chmod 755 /bin/mat-defender-bot-uninstall

echo installation completed
