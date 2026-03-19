import re

text = "cat 123 dog 456"

# Найти первое число
print(re.search(r"\d+", text).group())

#  Найти все числа
print(re.findall(r"\d+", text))

#  Заменить числа на #
print(re.sub(r"\d+", "#", text))

# Удалить пробелы
print(re.sub(r"\s+", "", text))

# Заменить cat на dog
print(re.sub(r"cat", "dog", text))