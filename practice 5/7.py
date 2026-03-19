import re

pattern = re.compile(r"\d+")

# Использование много раз
print(pattern.findall("123 abc 456"))

# Поиск в другой строке
print(pattern.findall("no 789 here"))

#  Проверка
print(bool(pattern.search("abc")))

#  Замена
print(pattern.sub("#", "a1b2c3"))

#  Быстрый повторный поиск
for s in ["1a", "22b", "ccc"]:
    print(pattern.findall(s))