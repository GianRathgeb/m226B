import tkinter as tk
import random

root = tk.Tk()

def fnButtonClicked():
    listBox.delete(0,'end')
    for i in range(7):
        rand = random.randint(1, 45)
        listBox.insert(i, rand)



button = tk.Button(root, text = "Show Numbers", command = fnButtonClicked)
listBox = tk.Listbox(root)

button.pack()
listBox.pack()
root.mainloop()