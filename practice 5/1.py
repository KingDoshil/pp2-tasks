import re

#  Проверка наличия цифр
print(bool(re.search(r"\d", "abc123")))

# Найти все числа
print(re.findall(r"\d+", "a1b22c333"))

# Найти слова
print(re.findall(r"\w+", "Hello world 123"))

#  Начинается ли с Hello
print(bool(re.match(r"Hello", "Hello world")))

# Заканчивается ли на end
print(bool(re.search(r"end$", "the end")))