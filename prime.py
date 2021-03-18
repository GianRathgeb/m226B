import tkinter as tk
root = tk.Tk()
root.geometry("200x400")

def fnButtonClicked():
    primes = [x for x in range(2, int(inputField.get())) if all(x % y != 0 for y in range(2, x))]
    for position, primeNumber in enumerate(primes):
        listBox.insert(position, f"{position}: {primeNumber}")


button = tk.Button(root, text = "Show Primes in range", command = fnButtonClicked)
inputField = tk.Entry(root)
listBox = tk.Listbox(root, height = 20)

button.pack(padx = 20, pady = (30, 3))
inputField.pack(padx = 20, pady = 3)
listBox.pack(padx = 20, pady = 3)
root.mainloop()

