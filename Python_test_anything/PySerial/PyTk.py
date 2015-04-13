# -*- coding: utf-8 -*-

from Tkinter import *
     
class ClearApp:
    def __init__(self, parent=0):
        self.mainWindow = Frame(parent)
        # 엔트리 위젯을 만든다.
        self.entry = Entry(self.mainWindow)
        self.entry.insert(0,"COM1")
        self.entry.pack(fill=X)
        # 이제 버튼 2 개를 추가하고, grooved 효과를 준다.
        fButtons = Frame(self.mainWindow, border=2, relief="groove")
        bClear = Button(fButtons, text="지우기", width=8, height=1, command=self.clearText)
        bQuit = Button(fButtons, text="이제 그만", width=8, height=1, command=self.mainWindow.quit)
        bClear.pack(side="right", padx=15, pady=1)
        bQuit.pack(side="right", padx=15, pady=1)
        fButtons.pack(fill=X)
        self.mainWindow.pack()

        # 제목을 설정한다.
        self.mainWindow.master.title("파이썬")
      
    def clearText(self):
        self.entry.delete(0,END)
        
    def ValueInput(self):
        file = open('c:\\zzz.txt', 'w')
        file.write(text)
      
app = ClearApp()
app.mainWindow.mainloop()