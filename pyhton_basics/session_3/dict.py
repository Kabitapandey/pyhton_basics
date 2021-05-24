def Message_print(*a, **b):
    print(a)

    print(b)


Message_print(1, 2, 3, 4, 5, name='Kabita')

d = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
print(len(d))
# printing keys
print(d.keys())
# printing values
print(d.values())
# printing items
print(d.items())
del d[1]
print(d)
# updating
d.update({1: 'five'})
d[1] = 'update'
print(d)

# using for loop
for i, j in d.items():
    print(i, j)
