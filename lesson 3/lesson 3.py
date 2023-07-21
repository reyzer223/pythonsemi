# import random

# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# print(len(set(input("введите элементы через пробел -> ").split())))

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю 
# последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.


# arr =[]

# while True:
#     n = int(input('Введите длину списка -> '))
#     if n > 0:
#         break

# while n > 0:
#     a = int(input('Введите число -> '))
#     arr.append(a)
#     n -= 1


# while True:
#     k = int(input('Введите длину сдвига k -> '))
#     if k > 0:
#         break


# arr_2 = []

# for i in arr[k:]:
#     arr_2.append(i)
# for i in arr[:k]:
#     arr_2.append(i)

# print(arr_2)

# print(1,2,3,4,5)
# print(3,4,5,1,2)

# spisok = [1,2,3,4,5,6,7]
# k = int(input("Введите значение"))
# spisok = spisok[len(spisok) - k :] + spisok[:len(spisok) - k]
# print(spisok)

# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# data = {'1': 'S001','2': 'S002','3': 'S001','4': 'S005','5': 'S005','6': 'S009','7': 'S007'}

# print(set([value for key,value in data.items()]))
# print(set(data.values))

# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# array = [0, -1, 5, 2, 3]
# print(len([array[i] for i in range(1, len(array)) if array[i-1] < array[i]]))

# import random
#
# array_frs = []
#
# while True:
#     a = input('Как вы хотите заполнить список. Напишите (вручную или автоматически) -> ')
#     if a == 'вручную' or a == 'автоматически':
#         break
#
# while True:
#     array_len = int(input('Введите длину списка -> '))
#     if array_len > 0:
#         break
#
# # Заполнение списка
# if a == 'вручную':
#     i = 1
#     while i <= array_len:
#         a = int(input(f'Введите {i} элемент списка -> '))
#         array_frs.append(a)
#         i += 1
# if a == 'автоматически':
#     while array_len > 0:
#         a = random.randint(-20, 20)
#         array_frs.append(a)
#         array_len -= 1
#
# print(array_frs)
# count = 0
# res_array = ''
#
#
# for i in range(1, len(array_frs)):
#     frst, scnd = array_frs[i-1], array_frs[i]
#     if frst < scnd:
#         res_array += ' (' + str(frst) + ' < ' + str(scnd) + ') '
#         count += 1
#
#
# print(f'Количество элементов которые больше предыдущих -  {count}')
# print(res_array)