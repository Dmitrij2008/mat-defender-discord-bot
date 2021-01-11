# mat-defender-discord-bot
MAT defender - это Discord бот для удаления сообщений, содержащих мат

# Системные требования
- python3 (>= 3.5.3)
- библиотека python 3 [discord.py](https://github.com/Rapptz/discord.py "discord.py")

# Установка
## Debian 10/Buster
	su -
	apt install python3 python3-pip
	pip3 install discord
	dpkg --install mat-defender-bot*.deb
	
## Ubuntu
	sudo apt install python3-discord
	sudo dpkg --install mat-defender-bot*.deb

## Другой дистрибутив GNU/Linux
Установите из вашего пакетного менеджера: python3 python3-pip

	git clone https://github.com/lcomrade/mat-defender-discord-bot.git
	cd mat-defender-discord-bot
	chmod +x install.sh
	sudo ./install.sh
