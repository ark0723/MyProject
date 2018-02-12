from tkinter import *
from tkinter import ttk
import statistics
def median(ob,value):
    ob.Yvar.set(statistics.median(value))
    ob.Zvar.set("숫자 list를 입력 : ")
def mean(ob,value):
    ob.Yvar.set(statistics.mean(value))
def mode(ob,value):
    ob.Yvar.set(statistics.mode(value))
def pdv(ob,value):
    ob.Yvar.set(statistics.pstdev(value))
def pvar(ob,value):
        ob.Yvar.set(statistics.pvariance(value))
def sdv(ob,value):
    ob.Yvar.set(statistics.stdev(value))
def var(ob,value):
    ob.Yvar.set(statistics.variance(value))
statdict={
    'mean()':mean,
    'median()':median,
    'mode()':mode,
    'pstdev()':pdv,
    'pvariance()':pvar,
    'stdev()':sdv,
    'variance()':var
}

class Stats:
    def __init__(self,master):
        self.Xvar = StringVar()
        self.Yvar = StringVar()
        self.Zvar=StringVar()
        self.master=master
        win=Frame(master)
        win.pack()
        can=Canvas(win,width=100,height=10)
        can.create_line(0,0,10,0,fill='black')
        can.pack()
        title_label = Label(win, text='<Statistics Module>')
        title_label.pack()
        self.str = StringVar()
        combo = ttk.Combobox(win, width=20, textvariable=self.str)
        combo['values'] = ('mode()', 'mean()', 'median()','mode()',
                           'pstdev()','pvariance()','stdev()','variance()')
        combo.pack()
        combo.current(0)
        input_label = Label(win, text="숫자 리스트를 입력 : ")
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
            value = self.Xvar.get()
            if value[0]=="[":
                value = value[1:-1].split(',')
            else:
                value = value.split(',')
            value = list(map(lambda x: float(x), value))
            statdict[self.str.get()](self,value)
        except:
            self.Yvar.set("다시 입력해주세요")

