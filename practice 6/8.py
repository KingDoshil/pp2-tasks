import os
import shutil

# создать файл
open("a.txt", "w").close()

#  удалить
os.remove("a.txt")

#  переименовать
os.rename("test.txt", "new.txt")

#  копировать
shutil.copy("new.txt", "copy.txt")

# очистить файл
open("new.txt", "w").close()