# help(str.upper)
# print(str.upper("abc"))
my_pets = ['alfred', 'tabitha', 'william', 'arla']

# uppered_pets = list(map(str.upper, my_pets))
# uppered_pets = map(str.upper, my_pets)
# print(dir(uppered_pets))
# print(uppered_pets.get())
# help(round)
# print(round(55.5555,-1))
# for i in range(1,5):
#     print(i)
# circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

# result = list(map(round, circle_areas, range(1, 9999)))

# print(result)
# help(zip)
# print(list(list(zip([1,2,3],[4,5,6]))[0]))
# str="123456789"
# print(str[::-2])
# Python 3
# from functools import reduce

# numbers = [3, 4, 6, 9, 34, 12]
filter()
# def custom_sum(first, second):
#     print(first,second)
#     # print(second)
#     return first + second

# result = reduce(custom_sum, numbers)
# print(result)
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
print(list(map(lambda n:n*n,my_floats)))
print(list(map(lambda n:round(n*n,3),my_floats)))