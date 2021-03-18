import vehicleClasses as vc
import tkinter as tk
root = tk.Tk()


def fnvehicleacc():
    tesla.accelerate_up(int(txtInputSpeedChange.get()))
    tesla.print_speedometer()


def fnvehicleslo():
    tesla.slow_down(int(txtInputSpeedChange.get()))
    tesla.print_speedometer()


tesla = vc.PW(True, 'SH 1', 4, 5, 'Electro')
lkw = vc.LKW(False, 'SH 2', 8, '10t')


txtInputSpeedChange = tk.Entry(root)
btnCarAcc = tk.Button(root, text="Accelerate vehicle", command=fnvehicleacc)
btnCarSlo = tk.Button(root, text="Slow vehicle down", command=fnvehicleslo)
txtInputSpeedChange.grid(column=0, row=0)
btnCarAcc.grid(column=0, row=1)
btnCarSlo.grid(column=1, row=1)
root.mainloop()


