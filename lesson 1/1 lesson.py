# name = 1
# if name < 10:
#     name = name + 1
#     print(name)
# else:
#     print(name - 1)


# 1. В некоторой школе решили набрать три новых математических класса и 
# оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, 
# которое нужно приобрести для них.

# **Input:**

# 20 -- 10

# 21 -- 11

# 22 -- 11

# **Output:**

# 32

# classroom_1 = int(input())
# classroom_2 = int(input())
# classroom_3 = int(input())
# print((classroom_1)//2 + (classroom_2+1)//2 + (classroom_3)//2)
# print(round((klass_1 + klass_2 + Klass_3) / 2))

# 2. Вагоны в электричке пронумерованы натуральными числами, начиная с 1 
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; 
#  это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. 
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
# Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это 
# делать или сообщать, что без дополнительной информации это сделать невозможно.

# **Input:**
# 3
# 4
# **Output:**
# 6
# i = 1
# j = 1
# if i == j:
#     print('0 условий')
# else:
#     print(i + j - 1)
    # 1,2,3,4,p,6,7
    
# Задача 3
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.

# age = int(input("Введите год: "))
# if (age % 4 == 0 and age % 100 != 0 or age % 400 == 0):
#    print("Yes")
# else:
#     print("No")