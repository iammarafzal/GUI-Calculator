from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+30+30')
        master.config(bg='#000000')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#FFF0D2', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        Button(width=11, height=4, font=('Coldera', 9), text='(', relief='flat', bg='#FFE3AA', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, font=('Coldera', 9), text=')', relief='flat', bg='#FFE3AA', command=lambda: self.show(')')).place(x=90, y=50)        
        Button(width=11, height=4, font=('Coldera', 9), text='%', relief='flat', bg='#FFE3AA', command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, font=('Coldera', 9), text='9', relief='flat', bg='#FFE3AA', command=lambda: self.show(9)).place(x=180, y=125)
        Button(width=11, height=4, font=('Coldera', 9), text='8', relief='flat', bg='#FFE3AA', command=lambda: self.show(8)).place(x=90, y=125)
        Button(width=11, height=4, font=('Coldera', 9), text='7', relief='flat', bg='#FFE3AA', command=lambda: self.show(7)).place(x=0, y=125)   
        Button(width=11, height=4, font=('Coldera', 9), text='6', relief='flat', bg='#FFE3AA', command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, font=('Coldera', 9), text='5', relief='flat', bg='#FFE3AA', command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, font=('Coldera', 9), text='4', relief='flat', bg='#FFE3AA', command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, font=('Coldera', 9), text='3', relief='flat', bg='#FFE3AA', command=lambda: self.show(3)).place(x=180, y=275)     
        Button(width=11, height=4, font=('Coldera', 9), text='2', relief='flat', bg='#FFE3AA', command=lambda: self.show(2)).place(x=90, y=275)
        Button(width=11, height=4, font=('Coldera', 9), text='1', relief='flat', bg='#FFE3AA', command=lambda: self.show(1)).place(x=0, y=275)
        Button(width=11, height=4, font=('Coldera', 9), text='0', relief='flat', bg='#FFE3AA', command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, font=('Coldera', 9), text='.', relief='flat', bg='#FFE3AA', command=lambda: self.show('.')).place(x=180, y=350)       
        Button(width=11, height=4, font=('Coldera', 9), text='+', relief='flat', bg='#F1AF60', command=lambda: self.show('+')).place(x=270, y=275)
        Button(width=11, height=4, font=('Coldera', 9), text='-', relief='flat', bg='#F1AF60', command=lambda: self.show('-')).place(x=270, y=200)
        Button(width=11, height=4, font=('Coldera', 9), text='/', relief='flat', bg='#F1AF60', command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, font=('Coldera', 9), text='X', relief='flat', bg='#F1AF60', command=lambda: self.show('*')).place(x=270, y=125)        
        Button(width=11, height=4, font=('Coldera', 9), text='=', relief='flat', bg='#F1AF60', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, font=('Coldera', 9), text='C', relief='flat', bg='#FFE3AA', command=self.clear).place(x=0, y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()
