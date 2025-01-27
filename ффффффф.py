"""4.Тренерка формує команду для гри в баскетбол з учениць, які на зріст не нижчі ніж 180 см. Розробіть програму визначення,
 чи потрапить у цю команду дівчина зростом h см? """

h = float(input("Введіть свій зріст у сантиметрах: "))
if h <= 180:
    print("Чудово, ви нам підходите")
else:
    print("Вибайе але ви нам не підходите ")


"""5.Дано рівносторонній трикутник зі стороною b. Розробіть програму визначення,
 чи можна в трикутник уписати коло з радіусом r."""
import math

# Зчитуємо значення сторони трикутника і радіус кола
b = float(input("Введіть довжину сторони трикутника b: "))
r = float(input("Введіть радіус кола r: "))

# Знаходимо радіус описаного кола
circumradius = b / (2 * math.sin(math.pi / 3))  # Формула радіусу описаного кола у рівносторонньому трикутнику

# Перевіряємо можливість вписати коло в трикутник
if r >= circumradius:
    print("Коло можна вписати в трикутник.")
else:
    print("Коло не можна вписати в трикутник.")

"""6.	Відомі три найкращі результати учнівства школи в стрибках у довжину. Розробіть програму,
за допомогою якої за результатами стрибків визначаються прізвища учнів."""

a = int(input("Введіть результат стрибка у довжину: "))
if a == 200:
    print("Це Фролов")
if a == 220:
    print("Це Марусенко")
if a == 235:
    print("Це Підмогидьний")

"""7.У п’ятницю в 9 класі такі уроки: 1 – історія, 2 – математика, 3 – географія, 4 – інформатика, 5 – фізкультура.
Розробіть програму, за допомогою якої визначається назва предмета за його номером у розкладі."""

# Створюємо словник з розкладом уроків
rozklad = {
    1: "історія",
    2: "математика",
    3: "географія",
    4: "інформатика",
    5: "фізкультура"
}

# Зчитуємо номер уроку від користувача
num_uroku = int(input("Введіть номер уроку: "))

# Перевіряємо, чи є такий номер у розкладі
if num_uroku in rozklad:
    # Виводимо назву предмета за введеним номером
    print("Предмет у дану годину:", rozklad[num_uroku])
else:
    print("Урока з таким номером немає у розкладі.")

"""8.Знайдіть в Інтернеті та складіть список із п’яти найбільших міст України. Розробіть програму,
за допомогою якої визначається назва міста за його номером у цьому списку."""
# Список з найбільшими містами України
najbilshi_mista = [
    "Київ",
    "Харків",
    "Одеса",
    "Дніпро",
    "Донецьк"
]

# Зчитуємо номер міста від користувача
num_mista = int(input("Введіть номер міста (від 1 до 5): "))

# Перевіряємо, чи введений номер знаходиться у межах діапазону
if 1 <= num_mista <= 5:
    # Виводимо назву міста за введеним номером
    print("Місто з номером", num_mista, ":", najbilshi_mista[num_mista - 1])
else:
    print("Введено неправильний номер міста.")
