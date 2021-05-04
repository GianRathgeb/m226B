from tkinter import *


class window(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("CAD")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.Button1 = Button(self, text='Draw', command=self.draw)
        self.Button1.pack(side=TOP)

    def draw(self):
        self.canvas.create_arc(50, 50, 200, 200, start=0, extent=180, fill="", style=ARC)
        self.canvas.create_line(50, 120, 50, 230)
        self.canvas.create_arc(50, 150, 200, 300, start=180, extent=180, fill="", style=ARC)
        self.canvas.create_line(200, 300, 200, 200)
        self.canvas.create_line(200, 200, 150, 200)
        self.canvas.pack(fill=BOTH, expand=True)


def main():
    root = Tk()
    ex = window()
    root.geometry("700x400")
    root.mainloop()


if __name__ == '__main__':
    main()
