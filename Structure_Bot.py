# Данный бот будет доработан в будущем и подключен полностью к телеграмму, пока это просто структура, есть небольшие места с подключением телеграмма.

from pyowm import OWM
import telebot

def telebot_connect():
    bot = telebot.TeleBot('your bot code')

    @bot.message_handler(content_types=['text'])

    def start(message):
        if message.text == '/reg':
            bot.send_message(message.from_user.id, "Как тебя зовут?");
            bot.register_next_step_handler(message, get_name);  # следующий шаг – функция get_name
        else:
            bot.send_message(message.from_user.id, 'Напиши /reg');

    def get_name(message):  # получаем фамилию
        global name
        name = message.text
        bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
        bot.register_next_step_handler(message, get_surname);


    def get_surname(message):
        global surname
        surname = message.text
        bot.send_message(message.from_user.id, 'Сколько тебе лет?');
        bot.register_next_step_handler(message, get_age);


    def get_age(message):

        global age
        age = message.text
        bot.send_message(message.from_user.id,'Тебе ' + str(age) + ' ' + 'лет, тебя зовут ' + str(name) + ' ' + str(surname) + '?')

    bot.polling()
# ==================================================================================================
def print_message():
    print("Добро пожаловать, я чат-бот и я умею делать некоторые вещи: ")
    print("1. Могу вывести тебе твое расписание на конкретный день учитывая четную и нечетную неделю")
    print('2. Могу сказать тебе подробную погоду в Казани на сегодняшний день')
    print('3. Могу предложить поиграть в небольшую игру-опрос')
    print('4. Выход из приложения')
# ==================================================================================================
def weather():
    owm = OWM("API key")
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place('Kazan, RU')
    w = observation.weather

    w.detailed_status  # clouds
    w.wind()  # speed
    w.humidity  # 87
    w.temperature('celsius')  # temp
    w.rain  # {}
    w.heat_index  # None
    w.clouds  # 75

    print("-- г.Казань - Погода на сегодняшний день --")
    print("Температура: ", w.temperature('celsius')['temp'], 'градуса по Цельсию')
    print("Облака: ", w.detailed_status)
    print('Ветер: ', w.wind()['speed'], 'м/c')
    print("Влажность: ", w.humidity)
    print("Дождь: ", w.rain)
    print("Тепловой индекс: ", w.heat_index)
# ==================================================================================================
def game_quiz():
    print('Добро пожаловать в небольшую игру-опрос')
    print('Вопросы посвящены описанию автора')
    answer = input('Готовы ли вы сыграть в игру? да/нет: ')
    score = 0
    total_questions = 3

    if answer.lower() == 'да':
        answer = input('Вопрос 1-ый: Какого цвета глаза у автора? ')
        if answer.lower() == 'синие' or answer.lower() == 'синий' or answer.lower() == 'синего':
            score += 1
            print('Верно :)')
        else:
            print('Не верно :(')

        answer = input('Вопрос 2-ой: Какого цвета волосы у автора? ')
        if answer.lower() == 'рыжий' or answer.lower() == 'рыжего' or answer.lower() == 'оранжевый':
            score += 1
            print('Верно :)')
        else:
            print('Не верно :(')

        answer = input('Вопрос 3-ий: Какой самый любимый язык программирования у автора этого кода? ')
        if answer.lower() == 'python' or answer.lower() == 'питон' or answer.lower() == 'пайтон':
            score += 1
            print('Верно :)')
        else:
            print('Не верно :(')

    print('Игра закончена, ваш счет:', score, "правильных ответов из", total_questions)
# ==================================================================================================
def auto():
    s = str(input("Какой сегодня день недели? "))  # Введите строку (название дня недели)
    q = 1  # Состояние
    for i in range(len(s)):
        match q:
            case 1:
                if s.lower() == "понедельник" or s.lower() == 'пн':
                    q = 2
                elif s.lower() == "вторник" or s.lower() == 'вт':
                    q = 3
                elif s.lower() == "среда" or s.lower() == 'ср':
                    q = 4
                elif s.lower() == "четверг" or s.lower() == 'чт':
                    q = 5
                elif s.lower() == "пятница" or s.lower() == 'пт':
                    q = 6
                elif s.lower() == "суббота" or s.lower() == 'сб':
                    q = 7
                elif s.lower() == "воскресенье" or s.lower() == 'вс':
                    print("Сегодня выходной")
                    # exit()
                    break
            case 2:
                s1 = str(input("Четная или нечетная неделя? "))
                print("12:00 - 13:30 Физическая культура")
                print("15:40 - 17:10 Объекто ориентированный анализ")
                print("17:50 - 19:20 Теория автоматов и формальных языков")
                # exit()
                break
            case 3:
                s1 = str(input("Четная или нечетная неделя? "))
                print("8:30 - 10:00 Языки и методы программирования")
                if s1.lower() == "четная" or s1.lower() == 'чет':
                    print("10:10 - 11:40 Технологическая практика")
                # exit()
                break
            case 4:
                s1 = str(input("Четная или нечетная неделя? "))
                print("14:00 - 15:30 Английский язык")
                if s1.lower() == "четная" or s1.lower() == 'чет':
                    print("15:40 - 17:10 Языки и методы программирования")
                #    exit()
                elif s1.lower() == "нечетная" or s1.lower() == 'нечет':
                    print("15:40 - 17:10 Объекто ориентированный анализ")
                    print("17:50 - 19:20 Объекто ориентированный анализ")
                #    exit()
                break
            case 5:
                s1 = str(input("Четная или нечетная неделя? "))
                if s1.lower() == "нечетная" or s1.lower() == 'нечет':
                    print("10:10 - 11:40 Теория автоматов и формальных языков")
                elif s1.lower() == "четная" or s1.lower() == 'чет':
                    print("10:10 - 11:40 Базы данных")
                print("12:00 - 13:30 Физическая культура")
                print("14:00 - 15:30 Проектированние человекомашинного интерфейса")
                # exit()
                break
            case 6:
                s1 = str(input("Четная или нечетная неделя? "))
                print("10:10 - 11:40 Математическая логика")
                print("17:50 - 19:20 Проектированние человекомашинного интерфейса")
                # exit()
                break
            case 7:
                s1 = str(input("Четная или нечетная неделя? "))
                print("8:30 - 10:00 Архитектура вычислительных систем")
                print("10:10 - 11:40 Математическая логика")
                if s1.lower() == "четная" or s1.lower() == 'чет':
                    print("11:50 - 13:20 Базы данных")
                #    exit()
                elif s1.lower() == "нечетная" or s1.lower() == 'нечет':
                    print("11:50 - 13:20 Архитектура вычислительных систем")
                #    exit()
                break
# ==================================================================================================
def main_input():
    num = int(input('Выбери цифру и мы продолжим: '))
    # ==================================================================================================
    if num == 1:
        auto()      # расписание
    # ==================================================================================================
    elif num == 2:
        s4 = str(input("Узнать какая погода в Казани: да/нет "))
        if s4.lower() == "да":
            weather()  # выводит температуру
    # ==================================================================================================
    elif num == 3:
        s2 = str(input("Хотите сыграть в игру-опрос?: да/нет "))
        if s2.lower() == 'да':
            game_quiz()  # игра-опрос
    # ==================================================================================================
    elif num == 4:
        exit()
    # ==================================================================================================
    main_input()    # рекурсия
# ==================================================================================================

# ==================================================================================================
print_message()
main_input()

telebot_connect()
# ==================================================================================================
