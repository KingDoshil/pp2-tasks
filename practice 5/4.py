import re

# 1 или более цифр
print(re.findall(r"\d+", "1 22 333"))

#  0 или 1 символ
print(re.findall(r"colou?r", "color colour"))

#  Ровно 3 цифры
print(re.findall(r"\d{3}", "123 12 1234"))

#  От 2 до 4 букв
print(re.findall(r"[a-z]{2,4}", "a ab abc abcd abcde"))

#  Любое количество
print(re.findall(r"a*", "aaab"))