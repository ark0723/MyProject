from tkinter import *
from random import *
from time import *

class Conveyor(Frame):
    def __init__(self, master, picture, width):
        #self.conveyor = Conveyor(self, self.resized_picture, self.n) #(conveyor.py로)
        super(Conveyor, self).__init__()
        self.image_number_list = [] # 셔플된 이미지의 번호를 저장하기 위한 리스트. 13개
        self.labels = [] # 컨베이어 frame에 추가되는 이미지 label 위젯의 리스트
        self.master = master # 컨베이어 frame의 parent 설정
        self.width = width # 메인 테이블의 가로 길이. = 4
        self.n = width*(width-1)+1 # 컨베이어에 넣을 이미지의 수. = 13
        self.picture = picture # app에서 생성한 이미지 받아와서 저장
        self.image_flags = list(False for i in range(self.width*self.width)) # 이미지가 컨베이어에 올라갔는지 아닌지 체크하기 위한 리스트. 초기 세팅은 모두 FALSE.
        #현재 가리키는 그림의 번호 =  image_number_list[self.cur_idx]
        #현재 가리키는 그림객체 = self.picture[image_number_list[self.cur_idx]]
        self.conveyor_canvas = Canvas(self, height=30,width=50) # 현재 위치 표시를 위한 캔버스 위젯 생성

        # 컨베이어에 올릴 이미지 셔플링
        self.random_shuffle()

        # TODO
        # 셔플 결과대로 이미지 label 생성하여 리스트에 저장
        self.finallabel=Label(self,text='final',fg='red')
        self.finallabel.grid(row=0,column=12)

        for i in range(self.n):
            self.labels.append(Label(self,image=self.picture[self.image_number_list[i]]))
            self.labels[i].grid(row=1,column=i)

        # 현재 index 설정 = 시작 위치 설정
        self.cur_idx = int(self.n/self.width*(self.width-1)) #13/4*3=9

        # 현재 이미지 설정 = 시작 이미지 설정

        # 선택한 이미지와 비교 목적으로 저장
        self.cur_image = self.picture.index(self.picture[self.image_number_list[self.cur_idx]])
        #현재 화살표 그림의 원래 번호
        #[self.image_number_list[self.cur_idx]]: 10번째를 가리킨다면, 열번째인 그림의 원래 번호
        #self.picture.index(self.picture[가리킨 수의 원래 번호]): 원래의 그림 객체가 picture 원본에서는 몇번째였는지

        # TODO
        # 캔버스 세팅
        self.conveyor_canvas.grid(row=0, column=self.cur_idx)
        self.pointer=self.conveyor_canvas.create_polygon(10, 2, 40, 2, 25, 30, fill='yellow', outline='black', width=2)

    # TODO
    # 이미지 셔플 함수
    def random_shuffle(self):
        self.image_number_list=sample(list(range(16)),13) #[0,1,2,....15] 중 임의의 13개의 숫자를 선택함
        for i in self.image_number_list:
            self.image_flags[i]=True
        # 0~15 숫자 중 임의로 중복되지 않는 13개의 숫자 선택

    # TODO
    # 선택한 그림이 현재 위치의 그림과 일치하는 경우
    def correct_match(self):
        # 마지막 이미지를 찾은 경우
        if self.cur_idx == self.n-1:
            self.master.quit_game(True)
        #최종 그림 상태에서 정답을 맞췄다

        # 캔버스 위젯
        # 현재 위치 표시 도형 우측 이동

        # 현재 이미지 및 현재 위치 재설정
        # canvas.itemconfig(도형의객체, outline='white', fill='white', + 추가적인 parameter 세팅) 기존에 생성된 도형 객체의 변경 가능
        else:
            # 현재 위치가 컨베이어의 가장 우측 도형을 지목할 때
            # FINAL 글씨를 가리지 않도록 도형 수정
            if self.cur_idx == self.n-2:
                self.conveyor_canvas.delete(self.pointer)
                self.finallabel.destroy()
                self.finallabel = Label(self, text='final', fg='red',bg='yellow')
                self.finallabel.grid(row=0, column=12)
                self.cur_idx+=1
            #끝 두번째 상태에서 정답을 맞춰서 final로 화살표가 가야 한다

            # 그 외 도형 이동
            else:
                self.conveyor_canvas.grid(row=0, column=self.cur_idx + 1)
                self.cur_idx += 1
            # 현재 이미지 및 현재 위치 수정

    # TODO
    # 선택한 그림이 현재 위치의 그림과 일치하지 않는 경우
    def wrong_match(self):
        # 마지막 기회에서 틀린 경우
        if(self.cur_idx == 0):
            self.master.quit_game(False)
            #마지막에서 틀려서 게임 오버 해야함

        # 캔버스 위젯
        # 가장 왼쪽의 이미지를 제거
        # 기존 이미지들 좌측으로 한 칸씩 이동
        # 컨베이어에 추가되지 않은 이미지 중 하나 선택하여 가장 우측에 추가
        # 현재 위치 재설정
        # canvas.itemconfig(도형의객체, outline='white', fill='white', + 추가적인 parameter 세팅) 기존에 생성된 도형 객체의 변경 가능
        else:
            # FINAL에서 오답 선택했을 때 도형 복구
            if self.cur_idx == self.n-1:
                self.cur_idx-=1
                self.pointer = self.conveyor_canvas.create_polygon(10, 2, 40, 2, 25, 30, fill='yellow', outline='black',
                                                                   width=2)
                self.finallabel.destroy()
                self.finallabel = Label(self, text='final', fg='red')
                self.finallabel.grid(row=0, column=12)

            # 그 외 도형 이동
            else:#그냥 틀려서 왼쪽으로 이동 해야함.
                self.conveyor_canvas.grid(row=0,column=self.cur_idx-1)
                self.cur_idx-=1

            # 새 이미지 추가
            while True:
                new_image = randint(0, self.width*self.width-1)
                if new_image not in self.image_number_list :
                    break #랜덤 사진 뽑기해서 기존 사진에 없으면 새 이미지로 채택

            # 기존 이미지 좌측으로 한 칸씩 이동
            # label.config(parameter = configuration) 기존의 label 위젯 변경 가능
            for i in range(0,self.n-1):
                self.labels[i].config(image=self.picture[self.image_number_list [i+1]])
                #모든 레이블에 대해 그 뒤 레이블로 바꿔치기 한다.
                self.image_number_list [i] = self.image_number_list [i+1]
                #그림 숫자 리스트도 바꿔치기 한다

            # 새 이미지 추가
            self.image_number_list[self.n-1] = new_image #새이미지 리스트 끝에 새 번호를 넣는다
            self.labels[self.n-1].config(image=self.picture[self.image_number_list [self.n-1]])
            #레이블 리스트의 마지막을 새 이미지로 바꾼다.

