nums = [1, 2, 3, 4, 5]

print(list(filter(lambda x: x % 2 == 0, nums)))
print(list(filter(lambda x: x > 3, nums)))
print(list(filter(lambda x: x > 0, [-1, 2, -3, 4])))
print(list(filter(None, ["", "a", "b"])))
print(list(filter(lambda x: len(x)>3, ["hi", "hello"])))