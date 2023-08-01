from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "6426647294:AAGOJFgJRJ3I7IyTUa3MvVtvN35MWTmFOEw"

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


users_ids = [490415921,  744475470 ]

@dp.message_handler()
async def forward_to_users(message: types.Message):
    # Проверяем, содержит ли сообщение сигнал для пересылки (например, ключевое слово "переслать")
    if "$signal" in message.text.lower():
        # Пересылаем сообщение каждому пользователю из списка
        for user_id in users_ids:
            try:
                await bot.forward_message(chat_id=user_id,
                                          from_chat_id=message.chat.id,
                                          message_id=message.message_id)
            except Exception as e:
                # Обработайте исключение, если пересылка сообщения не удалась
                print(f"Не удалось переслать сообщение пользователю с ID {user_id}: {e}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)