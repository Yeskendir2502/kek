import logging
from flask import Flask, request
import os
import telebot
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
server = Flask(__name__)
PORT = int(os.environ.get('PORT', 5000))
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
bot=telebot.TeleBot(TOKEN)
# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
CALLMESSAGEREACTION, COMPLIMENT, CUPOF, WORK, STARTREAD, NAME, TRULY, SADEND = range(8)


# функция обратного вызова точки входа в разговор
def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['Написать', 'Позвонить']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Закатное солнце озаряло крыши и стекла соседних многоэтажек, но взгляд молодого художника был прикован горными склонами Заилийского Алатау. Здесь, на крыше двенадцатиэтажного здания расположился ресторан средиземноморской кухни «Олимпия», который стоило посетить хотя бы ради живописного вида. Пока художник любовался видом, за соседним столиком, мужчина в сером поглядывал на свои поцарапанные часы. Его подруга опаздывала уже на 45 минут.',
        reply_markup=markup_key)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `GENDER`
    # if reply_markup == "Написать":
    #     update.message.reply_text('Она не прочитала. Едыге было не ловко уже в пятый раз говорить официанту, что его подруга должна скоро подойти.',
    #     reply_markup=ReplyKeyboardRemove(),)
    # elif reply_markup == "Позвонить":
    #     update.message.reply_text(
    #         'Она не ответила. Едыге было не ловко уже в пятый раз говорить официанту, что его подруга должна скоро подойти.',
    #         reply_markup=ReplyKeyboardRemove(), )
    return CALLMESSAGEREACTION

def callmessagereaction(update, _):
        # Список кнопок для ответа
    if update.message.text == "Написать":
        update.message.reply_text('Она не прочитала.',)
    elif update.message.text == "Позвонить":
        update.message.reply_text('Она не ответила.',)
    reply_keyboard = [['Колье', 'Брошь', 'Платье']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Едыге было не ловко уже в пятый раз говорить официанту, что его подруга должна скоро подойти.'
        'И вот, она наконец пришла.'
        'На ней было длинное, белое платье, имевшее нечто греческое в своем фасоне, в особенности в своем лабиринтообразном узоре. У нее были прекрасные, черные волосы и бирюзовая челка, к которой она подобрала крупное колье из бирюзы. Брошь виде золотого трезубца дополнял облик морской богини.'
        'На секунду от ее вида мужчина потерял дар речи, но быстро опомнился. Надо поздороваться, сделав, по возможности, комплимент.',
        reply_markup=markup_key)
    update.message.reply_text(
        '–Привет, Саарин, прекрасно выглядишь, особенно …',
        reply_markup=markup_key)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `GENDER`
    return COMPLIMENT

def compliment(update, _):
    # Список кнопок для ответа
    if update.message.text == "Колье":
        update.message.reply_text('–Колье, просто прекрасное колье (язык мой злейший враг).',)
        update.message.reply_text('–Спасибо… Я его одолжила у подруги. Извини, что опоздала. Немного задержали на работе.')
    elif update.message.text == "Брошь":
        update.message.reply_text('–Брошь, она такая… золотая (язык мой злейший враг).',)
        update.message.reply_text('–Спасибо… Я его заказала на Алиэкспрессе, но не сочти это за рекламу. Извини, что опоздала. Немного задержали на работе.')
    elif update.message.text == "Платье":
        update.message.reply_text('–В этом платье. Не то чтобы не в платье ты выглядишь не так… (язык мой злейший враг).')
        update.message.reply_text('–Спасибо… Мне его коллега привез из Кипра. Извини, что опоздала. Немного задержали на работе.')


    reply_keyboard = [['Чай', 'Кофе']]

    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Не прошло и пяти минут, как к ним подошел все тот же официант, уставший ждать не меньше парня. ')
    update.message.reply_text(
        '–Вы готовы сделать заказ?\n–Одну минуту…  Сет «Атлант», а к нему... –Едыге вопросительно посмотрел на Саарин.', reply_markup=markup_key)
    # Начинаем разговор с вопроса
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `GENDER`
    return CUPOF

def cupof(update, _):
    # Список кнопок для ответа
    if update.message.text == "Чай":
        update.message.reply_text('–Жасминовый чай, пожалуйста.\n–Чайник, –дополнил Едыге.\n–Принято.')
    elif update.message.text == "Кофе":
        update.message.reply_text('–Стакан капучино.\n–Чашку жасминового чая, –добавил Едыге.\n–Принято.')
    ttt = update.message.text
    reply_keyboard = [['Да', 'Нет']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Официант ушел с довольной улыбкой. Он выиграл 5 тысяч, у своих коллег – девушка опоздала на 49 минут, но все-таки пришла.',reply_markup=markup_key)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `GENDER`
    if ttt == "Чай":
        update.message.reply_text(
            'Им принесли чайник жасминового чая. Играла живая музыка, сегодня был вечер Fourth Wall’s Breakers – ее любимой группы.')
    elif ttt == "Кофе":
        update.message.reply_text(
            'Им принесли стакан капучино и чашку имбирного чая. Играла живая музыка, сегодня был вечер Fourth Wall’s Breakers – ее любимой группы.')
    update.message.reply_text('–Как дела на работе?\n–Не представляешь!  Тьма работы, условия спартанские, один из моих коллег буквально настоящий… старина Лео, благо Надежда Викторовна всегда готова помочь. А у тебя?\n–Прекрасно. Твои рассказы? Не думала написать повесть или роман?')
    return WORK

def work(update,_):
    # Список кнопок для ответа
    if update.message.text == "Да":
        update.message.reply_text(
            '–Да, есть одна идейка… позже покажу.',)
    elif update.message.text == "Нет":
        update.message.reply_text(
            '–Пока нет, но осенью видно будет.',)
    reply_keyboard = [['Дать прочитать', 'Рассказать самому']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text('–Знаешь, я решил посвятить тебе коротенький рассказ… – начал Едыге.',
                              reply_markup=markup_key)
    return STARTREAD


def startread(update, _):
    # Список кнопок для ответа
    if update.message.text == "Дать прочитать":
        update.message.reply_text('–Прочитаешь? Он короткий.\n–Давай конечно.')
        update.message.reply_text('Он отправил ей ссылку в телеграме.')
        update.message.reply_text('–Это бот, ведь так?\n–Да, я сделал интерактивную историю.\n–Оу… интересно.')
    elif update.message.text == "Рассказать самому":
        update.message.reply_text(
            '–В общем, ты слышала про интерактивные истории? Я сделал тебе такую в телеграм боте.\n–Да? –Воодушевлено прервала меня Саарин, –Дашь прочитать?\n–Да, секунду.')
        update.message.reply_text('Он отправил ей ссылку в телеграме.')
    update.message.reply_text(
        'Саарин открыла телефон, и начала читать его рассказ. «Боже, какая ужасная идея!» – думал про себя теперь Едыге. Она сидит в телефоне, а Едыге сидит рядом с ней... Он успокаивал себя тем, что она усмехнулась пару раз пока читала его ванильные бредни.',)
    update.message.reply_text(
        'Саарин прочитала рассказ минут за десять-двенадцать. Их заказ еще не успели принести, но официанты уже начали новый спор: уйдут ли они вместе или по отдельности?',)
    update.message.reply_text('–Красивое имя у главной героини – Саадат.')

    reply_keyboard = [['–Я назвал ее в честь тебя...', '–Случайно пришло в голову… не думай ни о чем.']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        '–Надо же, –усмехнулась Саарин.\n–По правде…',
        reply_markup=markup_key)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `GENDER`
    return NAME

def name(update, _):
    # Список кнопок для ответа
    if update.message.text == "–Я назвал ее в честь тебя...":
        update.message.reply_text('–Я назвал ее в честь тебя... Точнее в честь твоей героини в «Балладе»… у нее такое красивое, восточное имя, выделяется на фоне имен твоих остальных героев.\n–Да, я обычно выбираю западные имена… Джоны, Лилии, Константины…',reply_markup=ReplyKeyboardRemove())
    elif update.message.text == "–Случайно пришло в голову… не думай ни о чем.":
        update.message.reply_text(
            '–Случайно пришло в голову… не думай ни о чем.\n–Да? Разве не в честь героини моей «Баллады»? –Едыге смутился, –Черт, да, точно, в честь нее!',)

    reply_keyboard = [['Структура', 'Язык']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        '–Кстати, хотел сказать.  По правде, мне не нравится мой рассказ, он вышел слишком… примитивным. Особенно...',
        reply_markup=markup_key)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `GENDER`
    return TRULY

def truly(update, _):
    # Список кнопок для ответа
    if update.message.text == "Структура":
        update.message.reply_text(
            '–Я использовал примитивную диаграмму алмаза… по большей части все выборы в рассказе фиктивные и не на что не влияют.',)
    elif update.message.text == "Язык":
        update.message.reply_text('–Я решил повторять за тобой. Сказать по правде, я обычно пишу не так как ты.')

    reply_keyboard = [['Почему рассказ называется Sad Date', 'Почему он посвятил его ей']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text('Я сделал короткую паузу, –Тебе он понравился?\nСаарин задумалась. Она бегло посмотрела на текст. Ей хотелось спросить…', reply_markup=markup_key)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `GENDER`
    return SADEND

def sadend(update, _):
    # Список кнопок для ответа
    if update.message.text == "Почему рассказ называется Sad Date":
        update.message.reply_text(
            '–Наверное, мне грустно, потому что этого никогда не случится.\nЕдыге грустно вздохнул. Он смотрел на открытый вордовский документ, служивший единственным источником света в его темной комнате. Уже был час ночи, а он писал ванильную историю.',)
    elif update.message.text == "Почему он посвятил его ей":
        update.message.reply_text(
            '–Сложно сказать. Наверное, потому что ты вдохновляешь меня писать. Служишь моей музой. Музой для того хромого сайгака…\nОфициант проспорил 10 тысяч у своих коллег.',)

    return ConversationHandler.END


def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Пока'
    )
    # Заканчиваем разговор.
    return ConversationHandler.END

if __name__ == '__main__':

    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("1998121466:AAERiWitGXdy2d4ByBL31WqDAFeDQBv_1qY")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CALLMESSAGEREACTION: [MessageHandler(Filters.regex('^(Написать|Позвонить)$'), callmessagereaction)],
            COMPLIMENT: [MessageHandler(Filters.regex('^(Колье|Брошь|Платье)$'), compliment)],
            CUPOF:[MessageHandler(Filters.regex('^(Чай|Кофе)$'), cupof)],
            WORK:[MessageHandler(Filters.regex('^(Да|Нет)$'), work)],
            STARTREAD:[MessageHandler(Filters.regex('^(Дать прочитать|Рассказать самому)$'), startread)],
            NAME:[MessageHandler(Filters.regex('^(–Я назвал ее в честь тебя...|–Случайно пришло в голову… не думай ни о чем.)$'), name)],
            TRULY:[MessageHandler(Filters.regex('^(Структура|Язык)$'), truly)],
            SADEND:[MessageHandler(Filters.regex('^(Почему рассказ называется Sad Date|Почему он посвятил его ей)$'), sadend)]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    bot.polling(none_stop=True)
    updater.idle()


