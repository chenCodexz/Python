# myList=[]
# myList.append(1)
# myList.append(2)
# myList.append(3)
# print(myList)
# print(myList[0])
# print(myList[1])
# print(myList[2])

# for x in myList:
#     print(x)

# print(myList[10]) 不存在 列表索引超出范围

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
print("The second name on the names list is "+second_name)
print("The second name on the names list is",second_name)