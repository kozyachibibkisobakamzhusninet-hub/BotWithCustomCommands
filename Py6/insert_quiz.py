from pathlib import Path

p = Path('main.py')
text = p.read_text('utf-8')
marker = 'bot.polling(none_stop=True)'
if marker not in text:
    raise SystemExit('marker not found')
if '@bot.message_handler(func=lambda message: message.chat.id in quiz_data)' in text:
    print('already inserted')
    raise SystemExit(0)

insert = "\n\n@bot.message_handler(func=lambda message: message.chat.id in quiz_data)\ndef handle_quiz_answer(message):\n    current_quiz = quiz_data.pop(message.chat.id, None)\n    if not current_quiz:\n        return\n\n    user_answer = message.text.strip()\n    correct_answer = current_quiz[\"answer\"]\n    if user_answer == correct_answer:\n        bot.send_message(message.chat.id, f\"✅ Вірно! Правильна відповідь: {correct_answer}\")\n    else:\n        bot.send_message(message.chat.id, f\"❌ Невірно. Ти відповів: {user_answer}. Правильна відповідь: {correct_answer}\")\n"

p.write_text(text.replace(marker, insert + marker, 1), 'utf-8')
print('inserted')
