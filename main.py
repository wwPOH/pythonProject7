while True:
 chat=input()
 print((chat.lower()))
 if 'привіт' in chat or 'хай' in chat or 'доброго дня' in chat:
  print(" Доброго вечора, я бот з України! ")
 elif 'як справи?' in chat or 'що робиш?' in chat or 'чим займаєшся?' in chat:
  print(" Вчусь програмувати на Python!")
 elif 'фільм' in chat or 'кінотеатр' in chat or 'серіал' in chat:
  print(" Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться фільм Залізна людина, він просто бомба!")
 elif 'бувай' in chat or'гудбай' in chat or 'надобраніч'  in chat or 'до зустрічі'  in chat:
  print(" Побачимось у мережі, I'll be back.")
  exit(0)
 else :
  print ('Дуже цікаво, але, нажаль, ніфіга не зрозуміло :( ')
