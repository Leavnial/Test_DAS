import random
import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def test_psi(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Пройти тест',
                                          url='https://www.idrlabs.com/ru/anxiety-stress-depression/test.php'))
    bot.send_message(message.chat.id,
                     "Здравствуйте! Я бот, который пришлет тест по оценке уровня депрессии, тревожности и стресса.\nТакже я вышлю вам полезные ссылки, после того, как вы напишите мне, какой из показателей у вас повышен.\nИтак, начнем тестирование:",
                     reply_markup=markup)
    bot.send_message(message.chat.id,
                     "Когда вы закончите, напишите показатель, который у вас выше среднего показателя: *стресс*, *тревожность* или *депрессия*.",
                     parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_test_result(message):
    result = message.text.lower()

    if result not in ["стресс", "тревожность", "депрессия"]:
        bot.reply_to(message,
                     "Пожалуйста, напишите один из вариантов вашего повышенного показателя: *стресс*, *тревожность* или *депрессия*.",
                     parse_mode='Markdown')
        return

    polza_statei(result, message)
    polza_yutbe(result, message)

def polza_statei(result, message):
    if result == "стресс":
        url = "https://www.who.int/ru/news-room/fact-sheets/detail/mental-health-strengthening-our-response"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        article_text = ''
        for paragraph in soup.find_all(['p', 'h1', 'h2', 'h3']):
            article_text += paragraph.get_text() + "\n"
        bot.send_message(message.chat.id, "Вот статья по результатам теста:")
        msg = [article_text[i:i + 4096] for i in range(0, len(article_text), 4096)]
        for messages in msg:
            bot.send_message(message.chat.id, messages)
    elif result == "тревожность":
        url = "https://www.who.int/ru/news-room/fact-sheets/detail/anxiety-disorders"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        article_text = ''
        for paragraph in soup.find_all(['p', 'h1', 'h2', 'h3']):
            article_text += paragraph.get_text() + "\n"
        bot.send_message(message.chat.id, "Вот статья по результатам теста:")
        msg = [article_text[i:i + 4096] for i in range(0, len(article_text), 4096)]
        for messages in msg:
            bot.send_message(message.chat.id, messages)
    elif result == "депрессия":
        url = "https://www.who.int/ru/news-room/fact-sheets/detail/depression#:~:text=%D0%94%D0%B5%D0%BF%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5%20%D1%80%D0%B0%D1%81%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%BE%20(%D1%82%D0%B0%D0%BA%D0%B6%D0%B5%20%D0%BD%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC%D0%BE%D0%B5%20%D0%B4%D0%B5%D0%BF%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B5%D0%B9,%D1%81%D0%BF%D0%BE%D1%81%D0%BE%D0%B1%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B0%D1%82%D1%8C%20%D0%BE%D1%82%20%D0%BD%D0%B5%D0%B5%20%D1%83%D0%B4%D0%BE%D0%B2%D0%BE%D0%BB%D1%8C%D1%81%D1%82%D0%B2%D0%B8%D0%B5."
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        article_text = ''
        for paragraph in soup.find_all(['p', 'h1', 'h2', 'h3']):
            article_text += paragraph.get_text() + "\n"
        bot.send_message(message.chat.id, "Вот статья по результатам теста:")
        msg = [article_text[i:i + 4096] for i in range(0, len(article_text), 4096)]
        for messages in msg:
            bot.send_message(message.chat.id, messages)

def polza_yutbe(result, message):
    if result == "стресс":
        playlists = [
            "https://www.youtube.com/watch?v=Lcd-rCktwDg&list=PLPNzHQ3dbnnrqGgcKQqG-5Gtl-XqNASHv",
            "https://www.youtube.com/watch?v=8Tv3flM-xvY&list=PLv_BjIKGm-UYg22rthQiMQT8mWblEPYxI",
            "https://www.youtube.com/watch?v=j8bl81VVkxM&list=PLjRF0k-aUGD84s24jkHiBgitxCnNvfE8U"
        ]
    elif result == "тревожность":
        playlists = [
            "https://www.youtube.com/watch?v=1pMRpjC_lKg&list=PLwcFyFHL0afOg78eYfZeiLlxMKVKLg6BJ&pp=iAQB",
            "https://www.youtube.com/watch?v=-IAzSKYl6gk&list=PLosMrMnggLq97lZq7nWFQ7BilqcIcrip_",
            "https://www.youtube.com/watch?v=CRmYQhWvkGc&list=PLgSBXyruqjResprL3Q9I27ETas6XD_FZQ"
        ]
    elif result == "депрессия":
        playlists = [
            "https://www.youtube.com/watch?v=OtEFE0BSyfI&list=PLbXhsRoASq9i3IT1dSKWcGHlL4cDNOsQB",
            "https://www.youtube.com/watch?v=YaUkBmooefU&list=PLf7WRSHYASzQ2HGhT4OkLvwM_dANPmhkt",
            "https://www.youtube.com/watch?v=vcsmn4mtinw&list=PL7p2qY-vNoqbdRGuqAbJap7nX79_jxFUI"
        ]

    if playlists:
        bot.send_message(message.chat.id, "Вот видео по результатам теста:")
        playlist = random.choice(playlists)
        bot.send_message(message.chat.id, playlist)


bot.infinity_polling()
