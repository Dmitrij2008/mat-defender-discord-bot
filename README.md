# MAT Defender Discord bot
![CENSURE](https://raw.githubusercontent.com/lcomrade/mat-defender-discord-bot/main/raw/logo_horizontal.jpeg)
MAT defender - это Discord бот для удаления сообщений, содержащих мат. Блокировка мата не зависит от регистра сообщения.

# Системные требования
- python3 (>= 3.5.3)
- [discord.py](https://github.com/Rapptz/discord.py "discord.py")

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
Установите из вашего менеджера пакетов: `Python 3 и PIP 3`

	pip3 install discord
	git clone https://github.com/lcomrade/mat-defender-discord-bot.git
	cd mat-defender-discord-bot
	chmod +x install.sh
	sudo ./install.sh
	sudo systemctl enable mat-defender-bot.service
	sudo systemctl start mat-defender-bot.service
	
____
*Wiki* - [Конфигурация](https://github.com/lcomrade/mat-defender-discord-bot/wiki/%D0%9A%D0%BE%D0%BD%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%B0%D1%86%D0%B8%D1%8F) - [Удаление](https://github.com/lcomrade/mat-defender-discord-bot/wiki/%D0%A3%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
____
Copyright 2021 Leonid Maslakov
