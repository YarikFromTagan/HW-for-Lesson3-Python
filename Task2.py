# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import os
import math
from random import randint
os.system("cls")

n = int(input("Введите размерность списка N = "))
min = int(input("Введите минимальное значение списка: "))
max = int(input("Введите максимальное значение списка: "))

lst = [randint(min, max) for i in range(n)]

lst_new = [lst[i]*lst[-i-1] for i in range(math.ceil(n/2))]

print(f'{lst} => {lst_new}')
