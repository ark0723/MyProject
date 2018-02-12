from tkinter import *
from tkinter import ttk
import math

def ceil(ob) :
    value = float(ob.Xvar.get())
    ob.Yvar.set(math.ceil(value))
def floor(ob) :
    value = float(ob.Xvar.get())
    ob.Yvar.set(math.floor(value))
def fac(ob) :
    try :
        value = float(ob.Xvar.get())
        ob.Yvar.set(math.factorial(value))
    except :
        ob.Yvar.set("only integer,plz")
def fabs(ob) :
    value = float(ob.Xvar.get())
    ob.Yvar.set(math.fabs(value))
def sqrt(ob) :
    value = float(ob.Xvar.get())
    ob.Yvar.set(math.sqrt(value))
def sin(ob) :
    value = float(ob.Xvar.get())
    ob.set(math.sin(value))
def cos(ob) :
    value = float(ob.Xvar.get())
    ob.Yvar.set(math.cos(value))
def tan(ob) :
    value = float(ob.Xvar.get())
    ob.Yvar.set(math.tan(value))
def deg(ob) :
    value = float(ob.Xvar.get())
    ob.Yvar.set(math.degrees(value))
def radi(ob) :
    value = float(ob.Xvar.get())
    ob.Yvar.set(math.radians(value))
def cosh(ob) :
    value = float(ob.Xvar.get())
    ob.Yvar.set(math.cosh(value))
def sinh(ob) :
    value = float(ob.Xvar.get())
    ob.Yvar.set(math.sinh(value))
def tanh(ob) :
    value = float(ob.Xvar.get())
    ob.Yvar.set(math.tanh(value))
def fmod(ob) :
    value = ob.Xvar.get()
    value= value.split(',')
    value=list(map(lambda x:float(x),value))
    ob.Yvar.set(math.fmod(value[0],value[1]))
def log(ob) :
    value = ob.Xvar.get()
    value= value.split(',')
    value=list(map(lambda x:float(x),value))
    ob.Yvar.set(math.log(value[0],value[1]))
def pow(ob) :
    value = ob.Xvar.get()
    value= value.split(',')
    value=list(map(lambda x:float(x),value))
    ob.Yvar.set(math.pow(value[0],value[1]))

mathdict = {
    'ceil()':ceil,'floor()':floor,'ceil()':ceil,
    'factorial()':fac , 'fabs()':fabs, 'sqrt()':sqrt,
    'sin()':sin, 'cos()':cos, 'tan()':tan,'degrees()':deg,
    'radians()':radi, 'cosh()':cosh, 'sinh()':sinh, 'tanh()':tanh,
    'fmod()':fmod, 'log()':log, 'pow()':pow
}

class Maths:
    def __init__(self,master):
        self.Xvar = StringVar()
        self.Yvar = StringVar()
        self.master=master
        win=Frame(master)
        win.pack()
        can = Canvas(win, width=100, height=10)
        can.create_line(0, 0, 10, 0, fill='black')
        can.pack()
        title_label = Label(win, text='<Math Module>')
        title_label.pack()
        self.str = StringVar()
        combo = ttk.Combobox(win, width=20, textvariable=self.str)
        combo['values'] = list(mathdict.keys())
        combo.pack()
        combo.current(0)
        input_label = Label(win, text='fmod,pow,log는 두 개의 숫자를 a,b 형태로 입력,')
        input_label.pack()
        input_label = Label(win, text='나머지 함수는 숫자 한개를 입력 : ')
        input_label.pack()
        input_entry = Entry(win,textvariable=self.Xvar)
        input_entry.pack()
        action = ttk.Button(win, text="계산!", command=self.clickMe)
        action.pack()
        label1=Label(win,text='계산 결과 : ')
        label1.pack()
        label2=Label(win,textvariable=self.Yvar) #########
        label2.pack()
        self.master.mainloop()

    def clickMe(self):
        try:
            mathdict[self.str.get()](self)
        except:
            self.Yvar.set("다시 입력해주세요")