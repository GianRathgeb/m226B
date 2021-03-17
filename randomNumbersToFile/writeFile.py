import random
with open("file.txt", mode="w") as file:
    for i in range(100000):
        file.write(str(random.randint(1, 10000000)) + "\n")
with open("fileSemicolon.txt", mode="w") as file:
    for i in range(100000):
        file.write(str(random.randint(1, 10000000)) + ";")