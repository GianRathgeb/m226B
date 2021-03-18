from family import *


def fnwritetofile(strfilename, strcontent):
    with open(strfilename, mode='w') as objFile:
        objFile.write(strcontent)


arrClients = []
with open('Adressen.txt', mode='r') as file:
    for row in file:
        row = row.replace('"', '').replace('\n', '')
        temp = row.split(";")
        arrClients.append(Family(f"{temp[0]}", f"{temp[1]} {temp[2]}", f"{temp[3]}", f"{temp[4]} {temp[5]}"))

stringtowrite = ""
for c in arrClients:
    stringtowrite += f"{c.clientNumber};{c.fullName};{c.address};{c.place}\n"
fnwritetofile('ClientsWithClasses.txt', stringtowrite)

