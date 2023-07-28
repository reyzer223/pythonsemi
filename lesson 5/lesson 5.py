# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи

# def FibbonachyNumber(value):
#     if value <= 1:
#         return 1
#     else:
#         return (FibbonachyNumber(value - 1) + FibbonachyNumber(value - 2))

# while True:
#     n = int(input('Введите интересующую вас Номер числа Фиббоначи -> '))
#     if n < 1:
#         print('Вы ввели отрицательное число или 0')
#     else:
#         break
# print(f'Число Фибонначи в позиции {n} - {FibbonachyNumber(n)}')


# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.


# 1 2 3 4 5 5 5 5
# 1 2 3 4 1 1 1 1

while True:
    n = int(input('Кол-во оценок -> '))
    if n < 1:
        print('Вам не нужно менять оценки')
    else:
        break

arr = []

while n > 0:
    b = int(input('Введите оценку -> '))
    arr.append(b)
    n -= 1

print(arr)

max_val = max(arr)
min_val = min(arr)

for i in range(0, len(arr)):
    if arr[i] == max_val:
        arr[i] = min_val

print(arr)