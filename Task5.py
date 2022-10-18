# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# F(n) = F(n-2) + F(n-1)
# F(-n) = (-1)^(n+1) * F(n)

import os
os.system("cls")

def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

k = abs(int(input('Введите количество элементов k = ')))
print('\n')
posfib = []
negfib = []

for i in range(0, k+1):
    posfib.append(fib(i))
    negfib.append(pow(-1, (i+1)) * fib(i))

lst = []
count = -1
for i in range(2*k+1):
    if count >= -k:
        lst.insert(i, negfib[-i-1])
        count -= 1
    else:
        lst.insert(i, posfib[i-k])

print(lst)
print('\n')






