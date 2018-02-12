from tkinter import *
from tkinter import ttk

import math
import statistics
import random

from stattk import *
from mathtk import *
from randomtk import *

class Program:
    def __init__(self):

        self.root = Tk()
        self.mainframe = Frame(self.root,width=50,height=50)
        self.mainframe.pack()
        start1=Label(self.mainframe,text='시작 메뉴를 선택해 주세요')
        start2=Label(self.mainframe,text='1. Statistics')
        start3 = Label(self.mainframe, text='2. Math')
        start4= Label(self.mainframe, text='3. Random')
        start1.pack()
        start2.pack()
        start3.pack()
        start4.pack()

        menubar = Menu(self.root)
        funcmenu = Menu(menubar, tearoff=0)
        funcmenu.add_command(label='Statistics', command=self.openstat)
        funcmenu.add_command(label='Math', command=self.openmath)
        funcmenu.add_command(label='Random', command=self.openrandom)
        funcmenu.add_separator()
        funcmenu.add_command(label='Exit', command=self.root.destroy)
        menubar.add_cascade(label='시작', menu=funcmenu)
        self.root.config(menu=menubar)
        self.root.mainloop()

    def openstat(self):
        self.stat = Stats(self.mainframe)

    def openmath(self):
        self.math = Maths(self.mainframe)

    def openrandom(self):
        self.random = Randoms(self.mainframe)

b=Program()
