from tkinter import *
from tkinter import ttk


class Calculator:
    calval = 0.0
    divT = False
    mulT = False
    addT = False
    subT = False

    def numpress(self, value):
        entry_val = self.number_entry.get()
        entry_val += value
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, entry_val)

    def isfloat(self, str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def mathpress(self, value):

        if self.isfloat(str(self.number_entry.get())):
            self.divT = False
            self.mulT = False
            self.addT = False
            self.subT = False

            self.calval = float(self.entry_val.get())
            if value == "/":
                self.divT = True
            elif value == "*":
                self.mulT = True
            elif value == "+":
                self.addT = True
            else:
                self.subT = True

            self.number_entry.delete(0, "end")
    def eqpress(self):
        if self.addT or self.subT or self.mulT or self.divT:
            if self.addT:
                solution = self.calval + float(self.entry_val.get())
            elif self.subT:
                solution = self.calval - float(self.entry_val.get())
            elif self.mulT:
                solution = self.calval * float(self.entry_val.get())
            else:
                solution = self.calval / float(self.entry_val.get())

            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, solution)

    def __init__(self, root):
        self.entry_val = StringVar(root, value="")
        root.title("Calculator")

        root.geometry("595x250")
        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton",font="Serif 15",padding=10)
        style.configure("TEntry", font="Serif 18", padding=10)

        self.number_entry = ttk.Entry(root, textvariable=self.entry_val, width=100)
        self.number_entry.grid(row=0, columnspan=4)

        self.button7 = ttk.Button(root, text = "7", command=lambda: self.numpress('7'))
        self.button7.grid(row=1, column=0)
        self.button8 = ttk.Button(root, text="8", command=lambda: self.numpress('8'))
        self.button8.grid(row=1, column=1)
        self.button9 = ttk.Button(root, text="9", command=lambda: self.numpress('9')).grid(row=1, column=2)
        self.divis = ttk.Button(root, text="/", command=lambda: self.mathpress('/')).grid(row=1, column=3)

        self.button4 = ttk.Button(root, text="4", command=lambda: self.numpress('4')).grid(row=2, column=0)
        self.button5 = ttk.Button(root, text="5", command=lambda: self.numpress('5')).grid(row=2, column=1)
        self.button6 = ttk.Button(root, text="6", command=lambda: self.numpress('6')).grid(row=2, column=2)
        self.multi = ttk.Button(root, text="*", command=lambda: self.mathpress('*')).grid(row=2, column=3)

        self.button1 = ttk.Button(root, text="1", command=lambda: self.numpress('1')).grid(row=3, column=0)
        self.button2 = ttk.Button(root, text="2", command=lambda: self.numpress('2')).grid(row=3, column=1)
        self.button3 = ttk.Button(root, text="3", command=lambda: self.numpress('3')).grid(row=3, column=2)
        self.plus = ttk.Button(root, text="+", command=lambda: self.mathpress('+')).grid(row=3, column=3)

        self.button0 = ttk.Button(root, text="0", command=lambda: self.numpress('0')).grid(row=4, column=0)
        self.button_equal = ttk.Button(root, text="=", command=lambda: self.eqpress("=")).grid(row=4, column=1)
        self.buttonAC = ttk.Button(root, text="AC", command=lambda: self.numpress('AC')).grid(row=4, column=2)
        self.sub = ttk.Button(root, text="-", command=lambda: self.mathpress('-')).grid(row=4, column=3)


root = Tk()
calc = Calculator(root)
root.mainloop()