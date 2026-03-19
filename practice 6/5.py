a = [1, 2, 3]
b = ["a", "b", "c"]

print(list(zip(a, b)))

print(dict(zip(a, b)))

for x, y in zip(a, b):
    print(x, y)

print([x+y for x, y in zip([1,2], [3,4])])

print([x-y for x, y in zip([5,6], [1,2])])