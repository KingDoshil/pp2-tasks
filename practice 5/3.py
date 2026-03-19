import re

#  Начинается с A
print(re.findall(r"^A\w*", "Apple Banana"))

#  Заканчивается цифрой
print(re.findall(r"\w+\d$", "abc1 def2 ghi"))

# Любой символ
print(re.findall(r"a.b", "acb aab a_b"))

# Любая последовательность
print(re.findall(r"a.*b", "axxb a123b"))

# Только начало строки
print(bool(re.match(r"^Hello", "Hello world")))