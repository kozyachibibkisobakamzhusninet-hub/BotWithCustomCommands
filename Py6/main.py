import telebot
from telebot import types
from dotenv import load_dotenv
import os
import random

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)
quiz_data = {}

def keyboard():
    buttons = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )
    button1 = types.KeyboardButton(text='ℹ️ Допомога')
    button2 = types.KeyboardButton(text='🛤️ Напрями в ІТ')
    button3 = types.KeyboardButton(text='📚 Що вчити')
    button4 = types.KeyboardButton(text='🎲 Випадкове число')
    button5 = types.KeyboardButton(text='😂 Жарт')
    button6 = types.KeyboardButton(text='🪙 Підкидання монетки')
    button7 = types.KeyboardButton(text='🔐 Генератор паролів')
    button8 = types.KeyboardButton(text='🙏 Побажання')
    button9 = types.KeyboardButton(text='🧠 Факт')
    button10 = types.KeyboardButton(text='💭 Цитата')
    button11 = types.KeyboardButton(text='✨ Пророцтво')
    button12 = types.KeyboardButton(text='😍 Комплімент')
    button13 = types.KeyboardButton(text='🎯 Щоденне завдання')
    button14 = types.KeyboardButton(text='📝 Вікторина')
    buttons.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14)
    return buttons

@bot.message_handler(commands=['start'])
def start(message):
    text = f"Привіт\nЯ IT-Guide Bot.\nЯ допоможу тобі розібратись, як зайти в ІТ\nНапиши /help"

    bot.send_message(message.chat.id, text, reply_markup=keyboard())


def help(message):
    text = f"Ось що я можу:\n/paths — напрями в ІТ\n/skills — що вчити зараз\n/randomnumber — випадкове число від 1 до 6\n/joke — жарт\n/coinflip — підкидання монетки\n/passwordgenerator — генератор паролів\n/wish — побажання\n/fact — цікавий факт\n/quote — цитата\n/fortune — передбачення на день\n/compliment — комплімент\n/dailychallenge — щоденне завдання\n/quiz — вікторина"

    bot.send_message(message.chat.id, text, reply_markup=keyboard())


def paths(message):
    text = f"Backend / Frontend\nUI/UX Design\nData / AI\nCybersecurity\nQA"

    bot.send_message(message.chat.id, text, reply_markup=keyboard())


def skills(message):
    text = f"База для старту:\nPython\nGit\nАнглійська\nЛогіка"

    bot.send_message(message.chat.id, text, reply_markup=keyboard())


def random_number(message):
    number = random.randint(1, 6)
    text = f"Твоє випадкове число: {number}"

    bot.send_message(message.chat.id, text, reply_markup=keyboard())


def joke(message):
    jokes = [
        "Чому програмісти не люблять природу? Вона повна багів.",
        "Що сказав нуль одиниці? 'Ти мене не розумієш!'",
        "Чому комп'ютери не можуть грати в футбол? Вони бояться вірусів.",
        "Як називається програміст, який не може знайти помилку? Безпомилковий.",
        "Чому програмісти завжди плутають Хелловін і Різдво? Тому що Oct 31 = Dec 25."
    ]
    joke = random.choice(jokes)
    bot.send_message(message.chat.id, joke, reply_markup=keyboard())


def coin_flip(message):
    flip = random.choice(['Орел', 'Решка'])
    bot.send_message(message.chat.id, f"Випадковий результат: {flip}", reply_markup=keyboard())


def password_generator(message):
    length = 12
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    bot.send_message(message.chat.id, f"Згенерований пароль: {password}", reply_markup=keyboard())


def wish(message):
    wishes = [
        "Бажаю тобі успіху в навчанні!",
        "Нехай твої ідеї завжди здійснюються!",
        "Щоб твоя робота приносить радість!"
    ]
    wish = random.choice(wishes)
    bot.send_message(message.chat.id, wish, reply_markup=keyboard())


def fact(message):
    facts = [
        "Перший комп'ютерний вірус був створений у 1986 році.",
        "Python названий на честь комедійного шоу 'Monty Python's Flying Circus'.",
        "Перший веб-сайт був створений у 1991 році.",
        "Більшість сучасних програмістів використовують Git для контролю версій.",
        "AI (штучний інтелект) активно розвивається з 1950-х років."
    ]
    fact = random.choice(facts)
    bot.send_message(message.chat.id, fact, reply_markup=keyboard())


def quote(message):
    quotes = [
        "Програмування — це мистецтво вирішення проблем.",
        "Код повинен бути зрозумілим для людей, а не тільки для комп'ютера.",
        "Не бійся помилок, вони — частина навчання.",
        "Великий код починається з маленьких кроків.",
        "Навчання ніколи не закінчується, особливо в ІТ."
    ]
    quote = random.choice(quotes)
    bot.send_message(message.chat.id, quote, reply_markup=keyboard())


def fortune(message):
    fortunes = [
        "Сьогодні ти зможеш досягти свого мети.",
        "Твоя доброта повернеться до тебе.",
        "Нові можливості відкриються для тебе.",
        "Ти зможеш перемогти будь-які перешкоди.",
        "Твоя енергія та ентузіазм приведуть до успіху."
    ]
    fortune = random.choice(fortunes)
    bot.send_message(message.chat.id, fortune, reply_markup=keyboard())


def compliment(message):
    compliments = [
        "Ти чудова людина!",
        "Твоя посмішка робить світ кращим.",
        "Ти надихаєш інших своїм прикладом.",
        "Твоя працьовитість заслуговує на повагу.",
        "Ти маєш неймовірний талант!"
    ]
    compliment = random.choice(compliments)
    bot.send_message(message.chat.id, compliment, reply_markup=keyboard())


def daily_challenge(message):
    challenges = [
        "Сьогодні спробуй вивчити нову функцію в Python.",
        "Напиши невеликий скрипт для автоматизації задачі.",
        "Прочитай статтю про нову технологію в ІТ.",
        "Спробуй вирішити одну задачу на LeetCode.",
        "Поділися своїм знанням з другом або колегою."
    ]
    challenge = random.choice(challenges)
    bot.send_message(message.chat.id, challenge, reply_markup=keyboard())


def quiz(message):
    questions = [
        {
            "question": "Яка мова програмування використовується для веб-розробки?",
            "options": ["Python", "JavaScript", "C++", "Java"],
            "answer": "JavaScript"
        },
        {
            "question": "Що таке Git?",
            "options": ["Мова програмування", "Система контролю версій", "Операційна система", "База даних"],
            "answer": "Система контролю версій"
        },
        {
            "question": "Що таке API?",
            "options": ["Інтерфейс програмування додатків", "Мова програмування", "База даних", "Операційна система"],
            "answer": "Інтерфейс програмування додатків"
        }
    ]
    quiz_question = random.choice(questions)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for option in quiz_question["options"]:
        markup.add(option)

    quiz_data[message.chat.id] = quiz_question
    bot.send_message(message.chat.id, quiz_question["question"], reply_markup=markup)


@bot.message_handler(func=lambda message: message.chat.id in quiz_data)
def handle_quiz_answer(message):
    current_quiz = quiz_data.pop(message.chat.id, None)
    if not current_quiz:
        return

    user_answer = message.text.strip()
    correct_answer = current_quiz["answer"]
    if user_answer == correct_answer:
        bot.send_message(message.chat.id, f"✅ Вірно! Правильна відповідь: {correct_answer}")
    else:
        bot.send_message(message.chat.id, f"❌ Невірно. Ти відповів: {user_answer}.\n Правильна відповідь: {correct_answer}")


@bot.message_handler(func=lambda message: message.text == '😂 Жарт')
def handle_joke_button(message):
    joke(message)


@bot.message_handler(func=lambda message: message.text == '😍 Комплімент')
def handle_compliment_button(message):
    compliment(message)


@bot.message_handler(func=lambda message: message.text == '✨ Пророцтво')
def handle_fortune_button(message):
    fortune(message)


@bot.message_handler(func=lambda message: message.text == '💭 Цитата')
def handle_quote_button(message):
    quote(message)


@bot.message_handler(func=lambda message: message.text == '🧠 Факт')
def handle_fact_button(message):
    fact(message)


@bot.message_handler(func=lambda message: message.text == 'ℹ️ Допомога')
def handle_help_button(message):
    help(message)


@bot.message_handler(func=lambda message: message.text == '🛤️ Напрями в ІТ')
def handle_paths_button(message):
    paths(message)


@bot.message_handler(func=lambda message: message.text == '📚 Що вчити')
def handle_skills_button(message):
    skills(message)


@bot.message_handler(func=lambda message: message.text == '🎲 Випадкове число')
def handle_randomnumber_button(message):
    random_number(message)


@bot.message_handler(func=lambda message: message.text == '🪙 Підкидання монетки')
def handle_coinflip_button(message):
    coin_flip(message)


@bot.message_handler(func=lambda message: message.text == '🔐 Генератор паролів')
def handle_passwordgen_button(message):
    password_generator(message)


@bot.message_handler(func=lambda message: message.text == '🙏 Побажання')
def handle_wish_button(message):
    wish(message)


@bot.message_handler(func=lambda message: message.text == '🎯 Щоденне завдання')
def handle_challenge_button(message):
    daily_challenge(message)


@bot.message_handler(func=lambda message: message.text == '📝 Вікторина')
def handle_quiz_button(message):
    quiz(message)


bot.polling(none_stop=True)