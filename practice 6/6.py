# 1. write
with open("test.txt", "w") as f:
    f.write("Hello")

# 2. read
with open("test.txt", "r") as f:
    print(f.read())

# 3. append
with open("test.txt", "a") as f:
    f.write("\nWorld")

# 4. read lines
with open("test.txt") as f:
    print(f.readlines())

# 5. count lines
with open("test.txt") as f:
    print(len(f.readlines()))