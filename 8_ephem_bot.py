"""
Домашнее задание №1

Использование библиотек: ephem

* [x] Установите модуль ephem
  pip install ephem
* [x] Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* [x] В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* [x] При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem, datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import local_settings

logging.basicConfig(format='%(asctime)s %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='bot.log')

# PROXY = {
#     'proxy_url': 'socks5://t1.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {
#         'username': 'learn',
#         'password': 'python'
#     }
# }

def DICT_OF_PLANETS(planet_type = 'Planet'):
    """
    planet_type is Planet or PlanetMoon
    """
    planets = {}
    for planet in ephem._libastro.builtin_planets():
        if planet[1] == planet_type:
            planets[planet[2].lower()] = planet[2]
    return planets

def LIST_OF_PLANETS(planet_type = 'Planet'):
    """
    planet_type is Planet or PlanetMoon
    """
    planets = []
    for planet in ephem._libastro.builtin_planets():
        if planet[1] == planet_type:
            planets.append(planet[2])
    return planets

def where_is_planet(planet, dict_of_planets, date = None):
    if date == None:
        date = datetime.datetime.now()
    planet_name = dict_of_planets[planet]
    Planet = eval(f'ephem.{planet_name}("{date}")')
    const = ephem.constellation(Planet)
    return const[1]

def greet_user(update, context):
    text = """
Available commands:
/planet name_of_planet
    """
    update.message.reply_text(text)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet(update, context):
    planet_not_specified = len(update.message.text.split()) < 2
    if planet_not_specified:
        update.message.reply_text(f'Choose one of the planets: {", ".join(LIST_OF_PLANETS())}')
        return False

    planet = update.message.text.split()[1].lower()
    Planet = planet.capitalize()
    if planet in DICT_OF_PLANETS():
        print(planet in DICT_OF_PLANETS())
        planet_location = where_is_planet(planet, DICT_OF_PLANETS())
        print(planet_location)
        update.message.reply_text(f'Now {Planet} is in {planet_location}')
    else:
        update.message.reply_text(f'Don\'t know such planet - {Planet}')

def main():
    # mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)
    mybot = Updater(local_settings.TELEGRAM_BOT_TOKEN, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
