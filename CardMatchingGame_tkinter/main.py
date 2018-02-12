from app import * #app 모듈을 임포

def on_closing():
    global interrupt
    if messagebox.askokcancel("Quit", "Quit?"):
        root.quit()
        interrupt = 0

if __name__ == "__main__":
    global interrupt #인터럽트
    interrupt = 1 
    width = 4
    root = Tk() #root 생성

    while True: 
        app = App(root, width) ####app 모듈의 App을 실행한다.
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()
        if app.continue_game == 0 or interrupt == 0:
            break 
    root.destroy()
