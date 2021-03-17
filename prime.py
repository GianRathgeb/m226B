import tkinter as tk


root = tk.Tk()
root.geometry("200x400")

def fnFindPrimes(intMax):
    arrPrimes =  [x for x in range(2, intMax) if all(x % y != 0 for y in range(2, x))] 
    return arrPrimes

def fnButtonClicked():
    primes = fnFindPrimes(int(inputField.get()))
    for position, primeNumber in enumerate(primes):
        listBox.insert(position, f"{position}: {primeNumber}")



button = tk.Button(root, text = "Show Primes in range", command = fnButtonClicked)
inputField = tk.Entry(root)
listBox = tk.Listbox(root, height = 20)

button.pack(padx = 20, pady = (30, 3))
inputField.pack(padx = 20, pady = 3)
listBox.pack(padx = 20, pady = 3)
root.mainloop()



