from classes import Weather
import os


def fnclearallfiles(strdir):
    for file in os.listdir(strdir):
        if file.endswith(".txt"):
            fnfilewriter(f"months/{file}", '', 'w')


def fnfilewriter(strfilepath, stringtowrite, strmode):
    with open(strfilepath, mode=strmode) as objFile:
        objFile.write(stringtowrite)


arrWeather = []
with open("Meteo.txt", "r") as file:
    for i, row in enumerate(file):
        if not i == 0:
            if 'VALUE' in row:
                arrT = row.split(chr(9))[4:]
                t = arrT[-1].replace('\n', '')
                arrT = arrT[0:-1]
                arrT.append(t)
            else:
                arrT = row.split(chr(9))
            arrWeather.append(Weather(arrT[0], arrT[1], arrT[2], arrT[3], arrT[4], arrT[5], arrT[6]))
        else:
            pass

fnclearallfiles("months")
for d in arrWeather:
    tempstring = f"{d.year};{d.date};{d.time};{d.pressure};{d.abshumidity};{d.relhumidity};{d.airtemp}"
    try:
        fnfilewriter(f'months/{d.date.split(".")[1]}.txt', tempstring, 'a')
    except:
        print(tempstring)

