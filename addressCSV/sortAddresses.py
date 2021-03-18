def fnWriteToFile(strFileName, strContent):
    with open(strFileName, mode='w') as file:
        file.write(strContent)

def fnSortAddresses():
    strPersones = ''
    strCompanies = ''
    with open('Adressen.txt', mode='r') as file:
       for row in file:
            row = row.replace('"', '').replace('\n', '')
            temp = row.split(";")
            if temp[1] == '':
                strCompanies += f"{temp[0]};{temp[2]};{temp[3]} {temp[4]} {temp[5]}\n"
            else:
                strPersones += f"{temp[0]}{chr(9)}{temp[1]} {temp[2]}{chr(9)}{temp[3]} {temp[4]} {temp[5]}\n"
    fnWriteToFile("Persones.txt", strPersones)
    fnWriteToFile("Companies.txt", strCompanies)


fnSortAddresses()
