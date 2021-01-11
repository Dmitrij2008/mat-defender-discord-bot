# mat-defender-discord-bot
MAT defender - это Discord бот для удаления сообщений, содержащих мат. Блокировка мата не зависит от регистра сообщения.

# Системные требования
- python3 (>= 3.5.3)
- библиотека python 3 [discord.py](https://github.com/Rapptz/discord.py "discord.py")

# Установка
## Debian 10/Buster
	su -
	apt install python3 python3-pip
	pip3 install discord
	dpkg --install mat-defender-bot*.deb
	systemctl enable mat-defender-bot.service
	systemctl start mat-defender-bot.service
	
## Ubuntu
	sudo apt install python3-discord
	sudo dpkg --install mat-defender-bot*.deb
	sudo systemctl enable mat-defender-bot.service
	sudo systemctl start mat-defender-bot.service

## Другой дистрибутив GNU/Linux
Установите из вашего пакетного менеджера: python3 python3-pip

	pip3 install discord
	git clone https://github.com/lcomrade/mat-defender-discord-bot.git
	cd mat-defender-discord-bot
	chmod +x install.sh
	sudo ./install.sh
	sudo systemctl enable mat-defender-bot.service
	sudo systemctl start mat-defender-bot.service
