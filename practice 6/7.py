import os
from pathlib import Path

# 1. текущая папка
print(os.getcwd())

# 2. список файлов
print(os.listdir())

# 3. проверка файла
print(os.path.exists("test.txt"))

# 4. создать папку
os.mkdir("new_folder")

# 5. путь
p = Path("test.txt")
print(p.resolve())