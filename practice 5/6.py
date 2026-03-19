import re

# Только буквы
print(re.findall(r"[a-zA-Z]+", "abc123XYZ"))

#  Только цифры
print(re.findall(r"[0-9]+", "abc123XYZ"))

#  НЕ цифры
print(re.findall(r"[^0-9]+", "abc123XYZ"))

#  Гласные
print(re.findall(r"[aeiou]", "hello"))

# Буквы и цифры
print(re.findall(r"[a-zA-Z0-9]+", "abc123!!!"))