import glob
import os

class changemenu:
    def __init__(self,parent):
        self.goon=True
        self.parent=parent
        while self.goon:
            try:
                self.getpath()
            except PermissionError:
                print('permission error, go to the previous directory')
                self.parent.gotoprev()
                self.parent.printcurrent()
    def getpath(self):
        print('\nchange directory')
        print('enter a directory or path')
        pathtochange=input("(enter '..' for the parent dir, and q to exit): ")
        if pathtochange=='q':
            self.goon=False
        elif pathtochange=='..':
            self.parent.gotoprev()
            self.parent.printcurrent()
        else:
            self.parent.current+="\d"[0]+pathtochange
            self.parent.printcurrent()
    def gotoprev(self):
        #print(self.parent.current)
        a=self.parent.current.split('\\')
        s=a[0]
        for i in range(1,len(a)-1):
            s+='\\'+a[i]
        self.parent.current=s
        self.parent.printcurrent()

class searchmenu:
    def __init__(self,parent):
        self.parent=parent
        self.goon=True
        while self.goon:
            print('\nsearch file')
            print('\ncurrent dir : '+self.parent.current)
            self.searchkey = input('enter a keyword to search file or directory (enter q to exit) : ')
            self.search(self.parent.current)

    def search(self,current):
        if self.searchkey=='q':
            self.goon=False
        else:
            if glob.glob(current + "/**/*%s*" % self.searchkey,
                                recursive=True)==[]:
                print("There's no such file or directory.")
                return
            for f in glob.iglob(current + "/**/*%s*" % self.searchkey,
                                recursive=True):  # generator, search immediate subdirectories
                print(f)

class deletemenu: #os.mkdir os.unlink

    def __init__(self,parent):
        self.parent=parent
        self.goon=True
        self.homedirs = os.listdir(self.parent.current)
        while self.goon:
            self.parent.printcurrent()
            print('\ndelete directory or file')
            self.delpath = input('enter a directory or file (enter q to exit): ')
            if self.delpath=='q':
                break
            try:
                self.delpath=self.parent.current+'\\'+self.delpath
                os.rmdir(self.delpath)
            except FileNotFoundError:
                print("There's no such file or directory.")
            except OSError:
                print('this directory is not empty.')
                print('do you really want to delete this directory?')
                yn=input('enter(y/n) : ')
                if yn=='y':
                    self.deleteinsides(self.delpath)
                    print('successfully deleted')
                else:
                    pass
    def deletesth(self,path):


        if os.path.isfile(path):
            os.unlink(path)
        else:
            self.deleteinsides(path)
    def deleteinsides(self,path):
        inside=os.listdir(path)
        if len(inside)==0:
            os.rmdir(path)
            return
        else:
            for file in inside:
                self.deletesth(path+'\\'+file)
        os.rmdir(path)

class quitmenu:
    def __init__(self):
        quit()
