import re

#  Цифры
print(re.findall(r"\d", "a1b2c3"))

#  Слова
print(re.findall(r"\w+", "Hello 123"))

#  Пробелы
print(re.findall(r"\s", "a b c"))

#  НЕ цифры
print(re.findall(r"\D+", "123abc456"))

# НЕ пробелы
print(re.findall(r"\S+", "a b c"))