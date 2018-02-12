from imagebtn import *
from tkinter import *
from random import *
import time

class Maintable(Frame):
    n=0
    selected_image=0

    def __init__(self, master, picture, alphabet, width):
        #app class에서 콜됨
        #self.table = Maintable(self, self.picture_image, self.alphabet_image, self.n)
        super(Maintable, self).__init__() #frame의 생성.
        self.image_number_list = []  # 셔플된 이미지의 번호를 저장하기 위한 리스트. 16개
        self.master = master # maintable frame의 parent 설정
        self.width = width # maintable의 넓이. = 4
        self.n = width * width # maintable에 추가될 이미지 수. = 16
        self.picture = picture # # app에서 생성한 이미지 받아와서 저장

        self.conveyor=None
        # 숨겨진 이미지 셔플링
        self.random_shuffle() #이미지를 섞음. 아래에서 정의 해야 한다 TODO

        # TODO
        # ImageButton widget 생성하고 각 widget에 숨겨진 이미지 추가
        buttonlst=[]
        for i in range(self.width*self.width):
            abutton=ImageButton(self,image=alphabet[i])
            abutton.add_hidden(alphabet[i],self.picture[self.image_number_list[i]])
            buttonlst.append(abutton)
            abutton.grid(row=i//4,column=i%4)

        # 이미지 클릭시 이벤트 bind
        for i in range(0,self.width):
            for j in range(0,self.width):pass

        for i in range(self.width*self.width):
            buttonlst[i].bind('<Button-1>', self.show_hidden)
            buttonlst[i].bind('<ButtonRelease-1>', self.hide_picture)

    # TODO
    # hidden 이미지 셔플링
    def random_shuffle(self):
        self.image_number_list=list(range(self.width*self.width))
        shuffle(self.image_number_list)


    # 선택된 알파벳 ImageButton의 숨겨진 이미지 출력
    def show_hidden(self, event):
        event.widget.config(image=event.widget.get_hidden())

    # TODO
    # 숨겨진 이미지 숨기고 알파벳 이미지로 변환
    # 선택된 이미지와 컨베이어의 현재 이미지와 비교하고, 비교 결과에 따른 명령어 실행 부분
    def hide_picture(self, event):
        #time.sleep(10)
        #time.sleep(1.5)
        self.selected_image = self.picture.index(event.widget.hidden) #picture에서 어떤 번호인가
        event.widget.config(image=event.widget.alphabet)
        if self.selected_image!=self.conveyor.image_number_list[self.conveyor.cur_idx]:
            self.conveyor.wrong_match()
        else:
            self.conveyor.correct_match()




        
        
