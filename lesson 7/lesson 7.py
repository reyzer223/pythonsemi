# def f(n):
#     return n**2

# def f1(n):
#     return n%2 == 0


# pre_arr = input().split()
# print(pre_arr)
# pre_arr = list(map(int, pre_arr))
# arr = list(map(f, pre_arr))
# arr = list(map(lambda x: x**2, pre_arr))
# print(arr)
# x=5
# per = x%2==0
# print(per)
# arr = list(filter(f1, pre_arr))
# arr = list(filter(lambda x: x%2==0, pre_arr))
# print(arr)


# arr1= [1, 2, 3, 4, 5]
# arr2= [11, 22, 33, 44, 55, 66]


# arr3 = list(zip(arr1, arr2))
# arr3.append("asfsadf")
# print(arr3)


# arr = [11, 22, 33, 44, 55, 66]
# arr_res = list(enumerate(arr))
# print(arr_res)


# Дан список
# в отдельном списке вывести буквы
# в другом цифры

# arr = [1, 'abfdjksdagf', 2, 'ugfuisgf']

# arr_1 = list(filter(lambda x: type(x) == int, arr))
# arr_2 = list(filter(lambda x: type(x) != int, arr))
# print(arr_1, arr_2)

# 2 вариант

# arr_in = input('Введите строку -> ').split()
# arr_1 = list(filter(lambda x: x.isdigit(), arr_in))
# arr_2 = list(filter(lambda x: x.isalpha(), arr_in))
# print(arr_1, arr_2)