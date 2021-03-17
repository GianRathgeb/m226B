import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

strFileName = ""
while strFileName == "":
    strFileName = filedialog.askopenfilename()


objFile = open(strFileName, "r")
strFileContent = objFile.read()

print(strFileContent)