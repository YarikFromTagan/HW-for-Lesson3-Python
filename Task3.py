# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
os.system("cls")

n = int(input("Введите размерность списка N = "))
print('\n')

lst = [float(input(f'Введите {i+1}-й элемент списка: ')) for i in range(n)]    # создали список вещественных чисел размерности N
print('\n')

fract_lst = []      # создали список из дробных частей с учётом знака числа
for i in range(n):
    if lst[i] < 0:
        fract_lst.append(1 - lst[i]%1)
    else:
        fract_lst.append(lst[i]%1)

fract_lst.sort()    # отсортировали дробные части по возрастанию

for i in range(n):
    if 0 in fract_lst:
        fract_lst.remove(0.0) # удалили из списка нули, если таковые имеется

if len(fract_lst) == 1:
    diff  = fract_lst[0]
else:
    diff = (fract_lst[-1] - fract_lst[0])  # нашли разницу между последним и первым элементом отсортированного списка

print(f'{lst} => {diff}')
print('\n')
