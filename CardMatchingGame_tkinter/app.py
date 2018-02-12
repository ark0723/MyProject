from maintable import *
from conveyor import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sys
import os

class App(Frame):   #프레임을 상속 받는 클래스  
    picture_image = [] # 메인 테이블용 도형 이미지
    alphabet_image = [] # 메인 테이블용 알파벳 이미지
    resized_picture = [] # 컨베이어용 도형 이미지
    continue_game = 1
    
    def __init__(self, master, n): #constructor : 부모가 마스터, n이라는 것을 보유
        super(App, self).__init__() #Frame()을 실행. 
        self.master = master # root를 parent로
        self.n = n
        self.create_images()

        # 이미지 읽어와서 저장: pictureimage,alphabetimage,reizedimage 저장됨
        # n*n 게임판의 그림을 저장하는 리스트이다.

        # Maintable frame widget 생성 #self.table에 메인테이블이라는 객체 생성함 (maintable.py로)
        self.table = Maintable(self, self.picture_image, self.alphabet_image, self.n)
        self.table.grid(row=0, column=0, pady=(10, 20))  # 테이블은 위 공백 10, 아래 공백 20
        # 테이블을 프레임 안에 위치시킨다.

        # Conveyor frame widget 생성
        self.conveyor = Conveyor(self, self.resized_picture, self.n)  # (conveyor.py로)
        self.conveyor.grid(row=1, column=0)  # 콘베이어는 아래편에 넣는다
        # 콘베이어를 프레임 안에 위치시킨다.

        self.table.conveyor=self.conveyor

    # 이미지 파일을 읽어와서 이미지 객체를 생성하고 리스트에 저장하는 부분
    # 생성된 이미지 객체 리스트에는 추가적인 변경이 없고, index를 통해 randomize
    def create_images(self):
        self.picture_image = list(Image.open("picture\\%d.JPG" % (i+1)) for i in range(self.n*self.n))
        #게임판 n*n개 만큼 1~n*n번까지 오픈해서 그림리스트로 만듦
        self.alphabet_image = list(PhotoImage(file="alphabet\\%d.GIF" % (i+1)) for i in range(self.n*self.n))
        # 게임판 n*n개 만큼 1~n*n번까지 오픈해서 알파벳그림리스트로 만듦
        self.resized_picture = list(self.picture_image[i].resize((50,50), Image.ANTIALIAS) for i in range(self.n*self.n))
        #picture image를 리사이즈해서 다시 리스트로 만듦
        self.resized_picture = list(ImageTk.PhotoImage(self.resized_picture[i]) for i in range(self.n*self.n))
        self.picture_image = list(ImageTk.PhotoImage(self.picture_image[i]) for i in range(self.n*self.n))

    # 게임 종료시 처리 부분
    def quit_game(self, win):
        if win == True:
            messagebox.showinfo("게임 종료", "성공하였습니다")
        else:
            messagebox.showinfo("게임 종료", "실패하였습니다")

        result = messagebox.askquestion("다시 시작", "다시 시작하시겠습니까?", icon='warning')
        if result == 'no':
        	App.continue_game = 0

        self.conveyor.quit()
        self.table.quit()
        self.quit()


        
