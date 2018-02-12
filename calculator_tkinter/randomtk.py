from tkinter import *
from tkinter import ttk
import random

def myrandom(ob):
    value = (ob.Xvar.get())
    ob.Yvar.set(str(random.random()))
def seed(ob):
    random.seed()
    try:
        value = (ob.Xvar.get())
        random.seed(value)
    except:
        pass
    ob.Yvar.set("random.seed() 완료")

def uniform(ob) :
    value = (ob.Xvar.get())
    print(ob.Xvar.get())
    value=value.split(',')
    ob.Yvar.set(random.uniform(float(value[0]),float(value[1])))
def randint(ob):
    value = (ob.Xvar.get())
    value=value.split(',')
    ob.Yvar.set(random.randint(int(value[0]),int(value[1])))
def randrange(ob):
    value = (ob.Xvar.get())
    value=value.split(',')
    if len(value)==2:
        ob.Yvar.set(random.randint(float(value[0]),float(value[1])))
    else:
        ob.Yvar.set(random.randint(float(value[0]),float(value[1]),float(value[2])))
def choice(ob):
    value = ob.Xvar.get()
    value = value[1:-1].split(',')
    value = list(map(lambda x: float(x), value))
    ob.Yvar.set(random.choice(value))
def shuffle(ob):
    value = ob.Xvar.get()
    value = value[1:-1].split(',')
    value = list(map(lambda x: float(x), value))
    random.shuffle(value)
    ob.Yvar.set(value)
def sample(ob): #list,정수
    value = ob.Xvar.get()
    value=value.split('],')
    n_sample=int(value[-1])
    pop=value[0][1:]
    pop=pop.split(',')
    ob.Yvar.set(random.sample(pop,n_sample))

randdict={
    'seed()':seed,
    'uniform()':uniform,
    'randint()':randint,
    'randrange()':randrange,
    'choice()':choice,
    'shuffle()':shuffle,
    'sample()':sample
}




class Randoms:
    def __init__(self,master):
        self.Xvar = StringVar()
        self.Yvar = StringVar()
        self.master=master
        win=Frame(master)
        win.pack()
        can = Canvas(win, width=100, height=10)
        can.create_line(0, 0, 10, 0, fill='black')
        can.pack()
        self.str = StringVar()
        title_label = Label(win, text='<Random Module>')
        title_label.pack()
        combo = ttk.Combobox(win, width=20, textvariable=self.str)
        combo['values'] = tuple(randdict.keys())
        combo.pack()

        combo.current(0)
        input_label = Label(win, text='uniform,randint는 2개의 수 a,b')
        input_label.pack()
        input_label = Label(win, text='randrange는 2 or 3개의 수')
        input_label.pack()
        input_label = Label(win, text='choice,shuffle은 리스트')
        input_label.pack()
        input_label = Label(win, text='sample은 리스트,정수')
        input_label.pack()
        input_label = Label(win, text='parameter를 입력해주세요 : ')
        input_label.pack()
        input_entry = Entry(win,textvariable=self.Xvar)
        input_entry.pack()
        randombutton = ttk.Button(win, text="random()", command=self.clickrandom)
        randombutton.pack()
        action = ttk.Button(win, text="계산!",command=self.clickMe)
        action.pack()
        label1=Label(win,text='계산 결과 : ')
        label1.pack()
        label2=Label(win,textvariable=self.Yvar) #########
        label2.pack()
        self.master.mainloop()
    def clickrandom(self):
        myrandom(self)

    def clickMe(self):
        try:
            randdict[self.str.get()](self)
        except:
            self.Yvar.set("다시 입력해주세요")
