# create a heterogeneous list of numbers and names. Split the list from highest number,use basic functions not slicing etc
a = [10, "Amit", 25, "Rahul", 5, "Priya", 40, "Swarali"]

b = []

for i in a:
    if type(i) == int:
        b.append(i)

b.sort()
highest = b[-1]

list1 = []
list2 = []
flag = 0

for i in a:
    if i == highest:
        flag = 1
    if flag == 0:
        list1.append(i)
    else:
        list2.append(i)

print(list1)
print(list2)



