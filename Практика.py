"""Проверка, является ли число v четным"""

# def number_check(v):
#     return v % 2 == 0
#
# v = int(input("Пожалуйста, ввидите число:  "))
#
# if number_check(v):
#     print("Чётное")
# else:
#     print("Нечётное")

""" Нахождение факториала числа"""
# def factorial_find(a):
#     if a == 0:
#         return 1
#     else:
#         return a * factorial_find(a - 1)
#
# a = int(input("Введите число: "))
# print(factorial_find(a))

"""Определение суммы цифр числа"""

# def define_sum(a):
#     summa = 0
#     while a > 0:
#         digit = a % 10
#         summa += digit
#         a //= 10
#     return summa
#
# a = int(input("Введите число:   "))
# print(define_sum(a))


# def sum(c):
#     return c  #
#
#
# a = int(input("enter your number (a) :   "))
# b = int(input("enter your number (b) :   "))
# c = a + b
# print(c)

# def chek_push_ups(number):
#     if number > 15:
#         print("molodec")
#     else:
#         return number + 40
#
# number = int(input("enter: "))
#
# print(chek_push_ups(number))

# def define_vowel_count(user_string):
#     vowels = "aeiouAEIOU"
#     vowel_count = 0
#     for char in user_string:
#         if char in vowels:
#             vowel_count += 1
#     return vowel_count
#
# user_string = input("Введите строку: ")
# vowel_count = define_vowel_count(user_string)
# print("Количество гласных букв в строке:", vowel_count)


# s = ('hallo')
# for d in range(1, 100):
#     print(s)



# s = ('hallo, how are you?')
# for i in range(1, 222222):
#     print(s)
#
# s = 'Natan xlxoxh'
# for i in s:
#     if i == 'x':
#         continue
#     if i == 'h':
#         break
#     print(i)
# print()

#
# for i in range(1, 11):
#     for s in range(1, 11):
#         print(i, '*', s, '=', i * s, end='    ' )


# s = 'bubuy'
# for i in range(0, 1000000):
#     print(s)

# for i in 'nsastsasnsbsusbsusbsusy':
#     if i == 's':
#         continue
#     print(i)

# for a in range(1, 11):
#     if a == 9:
#         break
#     print(a)



"""Цыкл For"""
# # Вывести на экран числа от 1 до 10.
# for i in range(1, 11, 1):
#     print(i)
#
# Вывести на экран все четные числа от 1 до 20.
# for i in range(2, 21, 2):
#      print(i)

"""Найти сумму всех чисел от 1 до 100."""
# sum = 0
# for i in range(1,101):
#     sum +=i
#     print(sum)

"""Найти произведение всех чисел от 1 до 10."""
# sum = 1
# for i in range(1,11):
#     sum *=i
#     print(sum)

"""Вывести на экран все числа от 10 до 1 в обратном порядке."""
# for i in range(10,0,-1):
#     print(i)

"""Найти сумму всех нечетных чисел от 1 до 20."""
# sum = 0
# for i in range(1,20,3):
#     sum += i
#     print(i)
"""Найти среднее арифметическое всех чисел от 1 до 100."""
#
# sum = 0
# for i in range(1,101):
#     sum += i
#
# srednee = sum / 100
# print(sum)

"""Вывести на экран все числа, кратные 3, от 1 до 30."""

# for i in range(1,31):
#     if i % 3 == 0:
#         print(i)

"""Найти факториал числа N."""
# y = int(input('Введите число:  '))
#
# factorial = 1
#
# for i in range(1, y + 1):
#     factorial *= i
#     print(factorial)

"""Вывести на экран все простые числа от 1 до N."""
# a = int(input('input your number:  '))

# for num in range(1, a + 1):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

"""Найти сумму квадратов всех чисел от 1 до N."""
# a = int(input('Input:  '))
#
# for num in range(1, a + 1):
#     summ_cvadrat = a ** num
# print(summ_cvadrat)


# a = int(input('Input:  '))
#
# summ_cvadrat = 0
# for num in range(1, a + 1):
#     summ_cvadrat += num ** 2
#
# print(summ_cvadrat)

# """Вывод таблицы умножения"""
# for i in range(1, 10):
#     j = 1
#     while j <= 10:
#         print(i * j)
#         j += 1
#

"""Суммирование элементов списка"""
# list_1 = [1, 2, 3, 4, 5]
# a = len(list_1)
# i = 0
# sum = 0
# while i < a:
#     sum += list_1[i]
#     i += 1
# print(sum)

"""Факториал числа"""
# factorial = 1
# number = 12
# i = 1
# while i <= number:
#     factorial *= i
#     i += 1
# print(factorial)

# """Поиск элемента в списке"""
# list_1 = ["a", "b", "c", "d", "e"]
# element_dla_poiska = "e"
# i = 0
# while i < len(list_1):
#     if list_1[i] == element_dla_poiska:
#         print("Елемент найден")
#     i += 1
#
# while False:
#     print("Элемент не найден")

# s = float(input("Введіть суму на яку працівник виготовив товару: "))
# if s >= 30000:  # Якщо працівник виготовив товару на сумму більше ніж 30 000 грн, то йому даеться премія в розмірі 50% від окладу
#     a = s * 1.5
#     print(a)
# elif (s > 0) and (s < 30000):  # Якщо працівник виготовив товару менше ніж на 30000 він отримує просто свою зарплату
#     print(30000)
# else:
#     print("Людина не може виготовити від'ємну кількість товару")

# """Дано два дійсних числа. Розробіть програму, за допомогою якої менше число замінюється нулем, а більше – одиницею"""
#
# chislo_1 = float(input("Введіть перше число: "))
# chislo_2 = float(input("Введіть друге число: "))
# if chislo_1 < chislo_2:
#     chislo_1 = 0
#     chislo_2 = 1
# else:
#     chislo_1 = 1
#     chislo_2 = 0

"""	Дано ціле число  n. Розробіть програму, за допомогою якої це число збільшується на 7, якщо воно більше 15,
і зменшується на 5, якщо воно менше або дорівнює 15."""

# n = int(input("Введіть ціле число: "))
# result = 0
# if n > 15:
#     result = n + 7
# else:
#     result = n - 5
#
# print(result)