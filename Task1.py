# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
import os
os.system('cls')

n = int(input("Введите размерность списка N = "))
min = int(input("Введите минимальное значение списка: "))
max = int(input("Введите максимальное значение списка: "))

lst = [randint(min, max) for i in range(n)]
print(lst)

lst_new = []
i = 1
while i < len(lst):
    lst_new.append(lst[i])
    i +=2
print(lst_new)

print(sum(lst_new))
