lst = ["a", "b", "c"]

for i, v in enumerate(lst):
    print(i, v)

for i, v in enumerate(lst, start=1):
    print(i, v)

print(list(enumerate(lst)))
print(list(enumerate(lst, 10)))

print([i for i, v in enumerate(lst) if v == "b"])