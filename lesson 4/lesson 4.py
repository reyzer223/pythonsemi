# 25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.



# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# string = input('Введите элементы списка через пробел -> ').split()

# dict = {}
# result = ''
# for i in string:
#     if i in dict:
#         dict[i] += 1
#         result += str(i) + '_' + str(dict[i]) + ' '
#     else:
#         dict[i] = 0
#         result += str(i) + ' '
# print(result)

# Задача Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

# import re
# string = re.split(' |\\.', input('Введите текст -> ').lower())
# string.sort()
# dict = {}
# for i in string:
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1
# print(dict)
# max_val = 0
# max_key = ''
# for key, value in dict.items():
#     if value > max_val:
#         max_val = value
#         max_key = key
# print(f'Слово которое чаще всего встречалось - {max_key}, оно встретилось - {max_val} раз/раза!' )

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# print(len(set(re.split(' |\\.', input('Введите текст -> ').lower()))))