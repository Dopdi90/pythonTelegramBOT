import telebot
from telebot import types
from config import*
import random

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
#Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("рандомное число")
    item2 = types.KeyboardButton("Как дела?😊")
    item3 = types.KeyboardButton('🤖Отправка контента в чат🤖')

    markup.add(item1, item2)
    markup.add(item3)

    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}! Напиши мне что-нибудь )', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lal(message):
    if message.chat.type == 'private':
        if message.text == 'рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Как дела?😊':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, как сам?', reply_markup=markup)

        elif message.text == '🤖Отправка контента в чат🤖':

            markup = types.InlineKeyboardMarkup(row_width=4)
            item3 = types.InlineKeyboardButton('Видео', callback_data='vid')
            item4 = types.InlineKeyboardButton('Картинка', callback_data='pt')
            item5 = types.InlineKeyboardButton('Ссылка в чат', callback_data='url')
            item6 = types.InlineKeyboardButton('Кнопка Ссылка', url='https://www.python.org')
            markup.add(item3)
            markup.add(item4)
            markup.add(item5, item6)
            bot.send_message(message.chat.id, 'Выбирай: ', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить🥲')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отлично😁')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает, крепись☺️')
            elif call.data == 'vid':
                bot.send_message(call.message.chat.id, 'Допустим тут видео')
            elif call.data == 'pt':
                bot.send_photo(call.message.chat.id, open('./images.jpg', 'rb'))
            elif call.data == 'url':
                bot.send_message(call.message.chat.id, 'https://www.python.org')
            #Удаление инлайн кнопок
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='как дела?', reply_markup=None)
            # Уведомление
            #bot.answer_callback_query(chat_id=call.message.id, show_alert=False, text='Уведомление!!!')
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)