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
                for i in temp:
                    strCompanies += f"{i} "
                strCompanies += '\n'
            else:
                for i in temp:
                    strPersones += f"{i} "
                strPersones += '\n'
    fnWriteToFile("Persones.txt", strPersones)
    fnWriteToFile("Companies.txt", strCompanies)


fnSortAddresses()
