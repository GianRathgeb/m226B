import tkinter as tk
root = tk.Tk()

def fnFillValues(objBox, arrValues):
    for i, j in enumerate(arrValues):
        objBox.insert(i, str(j))

def fnButtonClicked():
    arrAddresses = []
    arrClientNumber = []
    with open('Adressen.txt', mode='r') as file:
       for row in file:
            row = row.replace('"', '')
            temp = row.split(";")
            arrAddresses.append(f"{temp[-1]} {temp[-2]} {temp[-3]}")
            arrClientNumber.append(temp[0])
    fnFillValues(listBoxAddresses, arrAddresses)
    fnFillValues(listBoxClientNumber, arrClientNumber)


button = tk.Button(root, text="Read addresses", command=fnButtonClicked)
listBoxAddresses = tk.Listbox(root, height=20, width=30)
listBoxClientNumber = tk.Listbox(root, height=20, width=30)

button.grid(column=0, row=0)
listBoxAddresses.grid(column=0, row=1)
listBoxClientNumber.grid(column=1, row=1)

root.mainloop()
