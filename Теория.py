# def check_pull_aps(number = 12):
#     if number == 12:
#         print("Дава ты молодец")
#     elif number < 12:
#         print("Дава, нормально, но мог бы лучше")
#     else:
#         print("ДАВА ТЫ ПРОТСТО КРАСАВЧИК)")
#
# check_pull_aps(15)
# check_pull_aps(12)
# check_pull_aps(10)

# def check_list(username, age):
#     if age >= 20:
#         print("Допускается вход в клуб")
#     else:
#         print("Вход в клуб запрещен для", username+"а")
#
# # Примеры вызова функции
# check_list("Антон", 19)
# check_list("Аня", 20)

"""F-strings"""
# a = 45
# b = 54
# c = a + b
# print(f"{c}" "Это результат сложения чисел")

# username = "Яма" # Это яма яма яма пупсики
# telephone_number = input("Пожалуйста, введите свой номер телефона, дорогая Яма Ямочка: ") ####vr
#
# if telephone_number == '63':
#     print(f"Дорогая {username}, что ты хотела позвонив сюда?")
# else:
#     print("Вы не Яма Ямочка! Что вам нужно?")


# username = input("Hello, please enter your name: ")
# print("hallo, hallo  "  f"{username}")

# """Расчет площади:
# Попросите пользователя ввести длину и ширину прямоугольника,
# а затем выведите сообщение с расчетом его площади с помощью F-строки."""
#
# width = int(input("Введите ширину пожалуйста:   "))
# length = int(input("Введите длинну пожалуйста:   ")) # We are asking to write numbers od width and length
#
# P = (f"{width + length}")
# print(P)   # We are knowing perivetr

# """Конвертер валют:
# Попросите пользователя ввести сумму в рублях,
# а затем выведите эквивалент этой суммы в долларах с использованием текущего курса обмена с помощью F-строки."""
# rub = int(input("Please, enter sum in ruble:  "))
# dollar = (f"{rub/92,50}")
# print("This sum in dollars will be"    f"{dollar}$ ")





# def sport_record_bench_press(Kg=50):
#     if Kg == 50:
#         print("Dave you are good")          # Делаем цыклы иф елиф вайл
#     elif Kg >= 50:
#         print("Congatulations Dave, you have just brought your record ")
#     else:
#         print("Dave, your best result is 53. Keep moving.")
#
# Kg = int(input("Please David, input your worl weight on bench press:   "))
# sport_record_bench_press(Kg)

"""Списки"""
# my_list = []
# print(type(my_list))

"""Список - это упорядоченно-изменяемая коллекция обектов разных типов, тоесть в список мы можем положить всё что 
угодно (строки, цыфры, дробные цыфры, другие списки и т. д. """

# Варианты создания списков

# my_list_1 = []
# print(type(my_list_1))
#
# my_list_2 = list()
# print(type(my_list_2))

# У каждого елемента в списке есть свой индекс - номер

                #-3                 -2               -1
                # 0                  1                2
my_list = ["яма ямочка", "сьесть кулебяку", "кусь-кусь-кусь"]

# print(my_list[-1])
# print(my_list[0])

# print(len(my_list))    # Узнаём длинну списка по команде Len() (по количеству обьектов-слов)

"""Срез - это извлеченние одного или нескольких обьектов из коллекции"""
# print(my_list[0:2])               # Если выборку начинать с начала, то ноль можно не учитывать

"""Фунуции - команды для списков"""
my_list.append("Сьесть шаверму")
print(my_list)                  #Добовляет обьект в конце спска

my_list.insert(2, "Поучить пайтон")       #  Добовляет обьект на место указанного синтекса (2)
print(my_list)

my_list.pop(-2)                         # Метод pop удаляет и возвращает из списка елемент с указанным индексом
print(my_list)

# Если ничего не передать (-2) Метод удалит и вернёт последний метод в списке

my_list__2 = ["Пойти на море", "Покушать кашки", "Поехать в Святогорск"]
my_list.extend(my_list__2)
print(my_list)

# Также можно складывать списки с друг-другом:

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a + b
print(c)

t = ["Hallo, hallo"] + ["my dear friend"] + ["Natan"]
print(t)

my_list.remove("яма ямочка")                                # Метод remove удаляет введенное значение
print(my_list)

my_list_copy = my_list.copy()
print(my_list_copy)            # Метод copy осуществляет копирование


print(my_list.count("Пойти на море"))
# Метод count возврощает количество елементов с введенным в него значением (Считает елемент в списке) как я понял


n_list = [10000000, 0.10, 12, 55, 2323,23232324]
n_list.sort()
print(n_list)                                 # Метод sort сортирует списки

n_list.reverse()                       #Метод reverse возврощает список в обратном порядке, тоесть переварачивает
print(n_list)

print(min(n_list))                    #Узнаем максимум и минимумм соответсвенно
print(max(n_list))

my_list_str = ["Ну", "здарова,", "брат!"]
my_str = " ".join(my_list_str)#Метод join склеевает обьекты  в его коллекции по разделителю ( , . ! - + и т.д.)
print(my_list_str)
