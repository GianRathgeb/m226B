import tkinter as tk


root = tk.Tk()
root.geometry("200x400")

def fnFindPrimes(intMax):
    arrPrimes = []
    position = 0
    for num in range(0, int(inputField.get()) + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                arrPrimes.append([position, num])
                position += 1
    return arrPrimes

def fnButtonClicked():
    primes = fnFindPrimes(int(inputField.get()))
    for position, primeNumber in primes:
        listBox.insert(position, f"{position}: {primeNumber}")



button = tk.Button(root, text = "Show Primes in range", command = fnButtonClicked)
inputField = tk.Entry(root)
listBox = tk.Listbox(root, height = 20)

button.pack(padx = 20, pady = (30, 3))
inputField.pack(padx = 20, pady = 3)
listBox.pack(padx = 20, pady = 3)
root.mainloop()



