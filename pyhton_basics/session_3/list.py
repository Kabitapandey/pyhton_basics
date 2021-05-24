from functools import reduce

li = [1, 2, 3, 4, 5]
print(li[0])

# add value at the end
li.append(5)

# removes value from the end
li.pop()

# removes values present at the specified index
li.remove(3)

# prints list after the index 2
print(li[2:])
# printing list using for loop
for i in li:
    print(i)

li2 = []

for i in li:
    if(i % 2 == 0):
        li2.append(0)
    else:
        li2.append(1)
print(li2)
print(li)

# map function


def function(i):
    if(i % 2 == 0):
        return 0
    else:
        return 1


# li2 = map(function, li)
print(list(li2))

# ternary opertaor
a = 1
b = 2
print(a > b and True or False)

# filter method
li3 = [1, 2, 3, 4, 5, 6, 7, 8]

ans = filter(lambda x: 1 if x % 2 == 0 else 0, li3)
ans1 = map(lambda x: 1 if x % 2 == 0 else 0, li3)
print(list(ans))
print(list(ans1))

# reduce method
ans2 = reduce(lambda a, b: a+b, li3)
print(ans2)
