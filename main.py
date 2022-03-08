from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import keyboard_main as kb
import keyboard_garbage as garb
import random

bot = Bot(token='5214888454:AAGaHxxyS655yUoVCtA76fM6iv83-S_P_mQ')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'назад'])
async def process_start_command(message: types.Message):

    await message.reply('''Привет, я Эко-бот, а точнее Эко-кот! 😸
Я помогу тебе разобраться в том, что такое экология, 
завести полезные привычки,
подскажу, где сдать мусор в переработку и многое другое.''', reply_markup=kb.main_kb)
    await message.reply('''В 1895 году в Нью-Йорке была создана первая система предварительной сортировки мусора.
Жители должны были сортировать бумагу, металл и пищевые отходы, и распределять их по раздельным бакам.
Эту систему совершенствуют и используют до сих пор, что очень сильно помогает в переработке мусора.
Но к сожалению некоторые люди всё равно не сортируют мусор.
Этот проект создан для того, что бы призвать людей к сортировке мусора.

Мы хотим жить в чистом городе!
''', reply_markup=kb.main_kb)
    await message.reply('''Скорее выбирай, что тебя беспокоит 😼⬇''', reply_markup=kb.main_kb)


array=["♻ Выбрасывай мусор только в сортировочные баки ️ \n🗑 И правильно их используй ",
"Складывай батарейки в отдельную коробочку и сдавай в пункты приёма.\nА ещё можно организовать в своём подъезде пункт сбора и потом централизовано отвозить батарейки 🔋🛢",
"🚯️ После отдыха на природе — убери за собой! \nВсегда выбрасывай мусор в предназначенные для этого места ♻",
"🍀 Сдавай банки из под консервов или освежителей воздуха в пункты приёма. \nДля того, чтобы из них сделали новый продукт ♻",
"🍵♻ Носи сегодня с собой кружку из дома,чтобы не использовать пластиковые стаканчики или бумажные чашки",
"🍃 Носи с собой многоразовую сумку для покупок, так ты сэкономишь на пакетах в магазине и сделаешь лучше окружающей среде",
"👕👚 Собери старую одежду и принеси её в пункты переработки или отдай её тем, кто в ней нуждается больше",
"💡 Используй энергосберегающие лампы, а после того, как она отслужит свой срок — найди пукнты, где принимают такие лампочки"]



@dp.message_handler(commands=[kb.habbit])
async def habbits_handler(message: types.Message):
    await message.reply("Ваша привычка на сегодня:\n\n"+random.choice(array)+"\n\nЕсли хотите ещё одну -- напишите '/Привычки'")


@dp.message_handler(commands=[kb.sort_garbage])
async def garbage_handler(message: types.Message):
    await message.reply("Garbage", reply_markup=garb.main_kb)


@dp.message_handler(commands=[garb.sort_batteries])
async def batteries_handler(message: types.Message):
    await message.reply("Батарейки можно здавать в магазинах \"Эльдорадо\", \"Вкусвилл\", \"Леруа Мерлен\" и \"Лента\"")


@dp.message_handler(commands=[garb.sort_plastic_and_glass])
async def plastic_handler(message: types.Message):
    await message.reply('''Пластик один из самых распространенных материалов на земле.
     Он не дорогой и очень практичный.
     Из-за этого его производят в огромных количествах и не всегда правильно утилизируют.
     
     Правильно утилизируя пластик, ты спасаешь живую природу. 
     Пластик, который ты собираешься выбросить, надо сдавать в пункты приема пластика. 
     
     Если ты не знаешь, где находится ближайший пункт приема, то почти в каждом дворе есть контейнер, который помечен специальным значком пластика:)
     Дальше мусор поступает в пункт переработки, а уже из него пластик поступает на предприятия и из него изготавливаются новые вещи!
     
     Такие меры позволяют сократить производство пластика и его попадание в окружающюю среду.
     
     ''')




@dp.message_handler(commands=[garb.sort_old_clothes])
async def clothes_handler(message: types.Message):
    await message.reply("Старая одежда")



@dp.message_handler()
async def bloobe(message: types.Message):
    await message.reply('something goes wrong')


if __name__ == '__main__':
    executor.start_polling(dp)