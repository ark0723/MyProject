import os
from selectmenu import *

class mainclass:
    def __init__(self):
        self.current='C:'+os.environ['HOMEPATH']
        while True:
            self.printcurrent()
            self.mainmenu()

    def printcurrent(self):
        try:
            homedirs = os.listdir(self.current)
            print('\ncurrent dir : ', end='')
            print(self.current)
            for i in range(int(len(homedirs) / 3) + 1):
                print("\t\t\t".join( homedirs[i * 3:(i + 1) * 3]))
        except:
            print('\ninvalid path. try again')
            self.gotoprev()

    def mainmenu(self):
        print('\nSelect Menu')
        print('1) Change directory \
        \n2) Search file \
        \n3) Delete directory or file \
        \n0) Quit')
        selection = input('Enter: ')
        if selection == '0':
            selected = quitmenu()
        elif selection == '1':
            selected = changemenu(self)
        elif selection == '2':
            selected = searchmenu(self)
        elif selection =='3':
            selected = deletemenu(self)
        else:
            print('Try again.')

    def gotoprev(self):
        #print(self.parent.current)
        a=self.current.split('\\')
        s=a[0]
        for i in range(1,len(a)-1):
            s+='\\'+a[i]
        self.current=s

m=mainclass()
