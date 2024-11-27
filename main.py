from telebot import TeleBot


bot = TeleBot('7936260622:AAF2nw5aoEfXa2FxHDoKxPBxkIBwyaSoVgg')
@bot.message_handler(commands=['start'])
def totor(message):
    bot.send_message(message.chat.id, 'Привет, я помогу в ткачестве и вязании. Подберу цветовую палитру. Чтобы продолжить введи команду colour')
    
@bot.message_handler(commands=['colour'])
def cotor(message):
    bot.send_message(message.chat.id, '*Какой цвет вы выбираешь основным?* Палитра: white, beige, gray, pink, fuchsia (dark pink), red, tomato red, cherry red, raspberry red, brown, light brown, dark brown, red-brown, orange, light orange, dark orange, yellow, lemon yellow, pale yellow, gold, olive, green, light green, turquoise, light blue, dark blue, mauve, dark purple, black. Если вам неудобно воспользоваться ботом, можете перейти по [ссылке](https://vk.com/wall-172663717_5721)')
   

@bot.message_handler(commands=['white'])
def cotor1(message):
    bot.send_message(message.chat.id, 'Белый: сочетается со всем. Наилучшее сочетание с синим, красным и черным.')
        
@bot.message_handler(commands=['beige'])
def cotor2(message):
    bot.send_message(message.chat.id, 'Бежевый: с голубым, коричневым, изумрудным, черным, красным, белым.')
        
@bot.message_handler(commands=['gray'])
def cotor3(message):
    bot.send_message(message.chat.id, 'Серый – хорошо сочетается с цветом фуксия, красный, фиолетовый, розовый, синий.')
        
@bot.message_handler(commands=['pink'])
def potor(message):
    bot.send_message(message.chat.id, 'Розовый – с коричневым, белым, цветом зеленой мяты, оливковым, серым, бирюзовым, нежно - голубым.')
        
@bot.message_handler(commands=['fushsia', 'darkpink'])
def potor1(message):
    bot.send_message(message.chat.id, 'Фуксия (темно – розовый) – с серым, желто-коричневым, зеленым лаймом, зеленой мятой, коричневый.')
        
@bot.message_handler(commands=['red'])
def potor2(message):
    bot.send_message(message.chat.id, 'Красный – подходит к желтым, белым, бурым, зеленым, синим и черным.')
        
@bot.message_handler(commands=['tomatored'])
def potor3(message):
    bot.send_message(message.chat.id, 'Томатно – красный: голубой, зеленая мята, песчаный, сливочно – белый, серый.')
        
@bot.message_handler(commands=['cherryred'])
def potor4(message):
    bot.send_message(message.chat.id, 'Вишнево-красный: лазурный, серый, светло-оранжевый, песчаный, бледно-желтый, бежевый.')
        
@bot.message_handler(commands=['raspberryred'])
def potor5(message):
    bot.send_message(message.chat.id, 'Малиново-красный: белый, черный, цвет дамасской розы.')
        
@bot.message_handler(commands=['brown'])
def potob(message):
    bot.send_message(message.chat.id, 'Коричневый: ярко-голубой, кремовый, розовый, палевый, зеленый, бежевый.')
        
@bot.message_handler(commands=['lightbrown'])
def potob1(message):
    bot.send_message(message.chat.id, 'Светло-коричневый: бледно-желтый, кремово-белый, синий, зеленый, пурпурный, красный.')
        
@bot.message_handler(commands=['darkbrown'])
def potob2(message):
    bot.send_message(message.chat.id, 'Темно-коричневый: лимонно-желтый, голубой, зеленая мята, пурпурно-розовый, зеленый лайм.')
        
@bot.message_handler(commands=['red-brown'])
def potob3(message):
    bot.send_message(message.chat.id, 'Рыжевато-коричневый: розовый, темно-коричневый, синий, зеленый, пурпурный.')
        
@bot.message_handler(commands=['orange'])
def pooob(message):
    bot.send_message(message.chat.id, 'Оранжевый: голубой, синий, лиловый, фиолетовый, белый, черный.')
        
@bot.message_handler(commands=['lightorange'])
def pooob1(message):
    bot.send_message(message.chat.id, 'Светло – оранжевый: серый, коричневый, оливковый.')
        
@bot.message_handler(commands=['blackorange'])
def pooob2(message):
    bot.send_message(message.chat.id, 'Темно –оранжевый: бледно – желтый, оливковый, коричневый, вишнёвый.')
        
@bot.message_handler(commands=['yellow'])
def pooyb(message):
    bot.send_message(message.chat.id, 'Желтый: синий, лиловый, светло-голубой, фиолетовый, серый, черный.')
        
@bot.message_handler(commands=['lemonyellow'])
def pooyb1(message):
    bot.send_message(message.chat.id, 'Лимонно-желтый: вишнево-красный, коричневый, синий, серый.')
        
@bot.message_handler(commands=['paleyellow'])
def pooyb2(message):
    bot.send_message(message.chat.id, 'Бледно-желтый: фуксия, серый, коричневый, оттенки красного, желтовато-коричневый, синий, пурпурный.')
        
@bot.message_handler(commands=['gold'])
def pooyb3(message):
    bot.send_message(message.chat.id, 'Золотисто-желтый: серый, коричневый, лазурный, красный, черный.')
        
@bot.message_handler(commands=['olive'])
def gooyb(message):
    bot.send_message(message.chat.id, 'Оливковый: апельсиновый, светло-коричневый, коричневый.')
        
@bot.message_handler(commands=['green'])
def gooyb1(message):
    bot.send_message(message.chat.id, 'Зеленый: золотисто- коричневый, оранжевый, салатный, желтый, коричневый, серый, кремовый, черный, сливочно-белый.')
        
@bot.message_handler(commands=['lightgreen'])
def gooyb2(message):
    bot.send_message(message.chat.id, 'Салатовый цвет: коричневый, желтовато-коричневый, палевый, серый, темно-синий, красный, серый.')
        
@bot.message_handler(commands=['turquoise'])
def gooyb3(message):
    bot.send_message(message.chat.id, 'Бирюзовый: фуксия, вишнево-красный, желтый, коричневый, кремовый, темно-фиолетовый.')
        
@bot.message_handler(commands=['lightblue'])
def gobyb(message):
    bot.send_message(message.chat.id, 'Голубой: красный, серый, коричневый, оранжевый, розовый, белый, желтый.')
        
@bot.message_handler(commands=['blackblue'])
def gobyb1(message):
    bot.send_message(message.chat.id, 'Темно-синий: светло-лиловый, голубой, желтовато-зеленый, коричневый, серый, бледно-желтый, оранжевый, зеленый, красный, белый.')
        
@bot.message_handler(commands=['mauve'])
def gobyb2(message):
    bot.send_message(message.chat.id, 'Лиловый: оранжевый, розовый, темно-фиолетовый, оливковый, серый, желтый, белый.')
        
@bot.message_handler(commands=['blackpurple'])
def gobyb3(message):
    bot.send_message(message.chat.id, 'Темно-фиолетовый: золотисто-коричневый, бледно-желтый, серый, бирюзовый, зеленая мята, светло-оранжевый.')
        
@bot.message_handler(commands=['black'])
def gobyb4(message):
    bot.send_message(message.chat.id, 'Черный универсален, элегантен, смотрится во всех сочетаниях, лучше всего с оранжевым, розовым, салатным, белым, красным, сиреневатым или желтым.')
        

    
bot.infinity_polling()
