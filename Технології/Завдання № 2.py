"""Дано два дійсних числа. Розробіть програму, за допомогою якої менше число замінюється нулем, а більше – одиницею"""

chislo_1 = float(input("Введіть перше число: "))
chislo_2 = float(input("Введіть друге число: "))
if chislo_1 < chislo_2:
    chislo_1 = 0
    chislo_2 = 1
else:
    chislo_1 = 1
    chislo_2 = 0
