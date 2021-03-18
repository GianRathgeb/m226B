from family import *


def fnWriteToFile(strFileName, strContent):
    with open(strFileName, mode='w') as file:
        file.write(strContent)


arrClients = []
with open('Adressen.txt', mode='r') as file:
    for row in file:
        row = row.replace('"', '').replace('\n', '')
        temp = row.split(";")
        arrClients.append(Family(f"{temp[0]}", f"{temp[1]} {temp[2]}", f"{temp[3]}", f"{temp[4]} {temp[5]}"))
        



print(arrClients)


