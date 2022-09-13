print("Введите месяц:")
mounth_birthday = str(input())
print("Введите число:")
date_birthday = int(input())

if (mounth_birthday == "март" and 31 >= date_birthday >= 21) or (mounth_birthday == "апрель" and 1 <= date_birthday <= 20):
    print("Овен")
elif (mounth_birthday == "апрель" and 30 >= date_birthday >= 21) or (mounth_birthday == "май" and 1 <= date_birthday <= 21):
    print("Телец")
elif (mounth_birthday == "май" and 31 >= date_birthday >= 22) or (mounth_birthday == "июнь" and 1 <= date_birthday <= 21):
    print("Близнецы")
elif (mounth_birthday == "июнь" and 3 >= date_birthday >= 22) or (mounth_birthday == "июля" and 1 <= date_birthday <= 22):
    print("Рак")
elif (mounth_birthday == "июль" and 31 >= date_birthday >= 23) or (mounth_birthday == "август" and 1 <= date_birthday <= 23):
    print("Лев")
elif (mounth_birthday == "август" and 31 >= date_birthday >= 24) or (mounth_birthday == "сентябрь" and 1 <= date_birthday <= 22):
    print("Дева")
elif (mounth_birthday == "сентябрь" and 30 >= date_birthday >= 23) or (mounth_birthday == "октябрь" and 1 <= date_birthday <= 23):
    print("Весы")
elif (mounth_birthday == "октябрь" and 31 >= date_birthday >= 24) or (mounth_birthday == "ноябрь" and 1 <= date_birthday <= 22):
    print("Скорпион")
elif (mounth_birthday == "ноябрь" and 30 >= date_birthday >= 23) or (mounth_birthday == "декабрь" and 1 <= date_birthday <= 21):
    print("Стрелец")
elif (mounth_birthday == "декабрь" and 31 >= date_birthday >= 22) or (mounth_birthday == "январь" and 1 <= date_birthday <= 20):
    print("Козерог")
elif (mounth_birthday == "январь" and 31 >= date_birthday >= 21) or (mounth_birthday == "февраль" and 1 <= date_birthday <= 18):
    print("Водолей")
elif (mounth_birthday == "февраль" and 29 >= date_birthday >= 19) or (mounth_birthday == "март" and 1 <= date_birthday <= 20):
    print("Рыбы")
else:
    print("Вы ввели некоректные данные!")
