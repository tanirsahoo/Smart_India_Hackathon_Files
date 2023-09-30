from tkinter import *
from tkinter import ttk
from abc import ABC , abstractmethod

win=Tk()

class Window:
    def __init__(self):
        self.width=500
        self.height= 500
        self.title="Xenon"

    def window_res(self):
        win.geometry("500x500")
        win.maxsize(self.width, self.height)
        win.minsize(self.width, self.height)
        win.title(self.title)
        win.configure(bg="#FFFFFF")

class Win_frames(ABC):
    def frames_gen(self, k, bd, wd, ht):
        flist=[]
        for i in range(k+1):
            flist.append(Frame(win, bg="#808080" ,borderwidth=bd, relief=SUNKEN, width=wd, height=ht))
        return flist

    @abstractmethod
    def frames_pos(self):
        pass

    def frames_del(self,obj):
        obj.destroy()

class Win_buttons(ABC):
    @abstractmethod
    def button_create(self ,f ,t ,bcl):
        pass

    def button_del(self,obj):
        obj.destroy()

class AuthWindow(Window,Win_frames,Win_buttons):
    def __init__(self):
        super().__init__()
        super().window_res()
        self.frames_list=[]
    

    def frames_pos(self):
        self.frames_list = self.frames_gen(1,1,400,400)
        self.frames_list[0].pack(side="top", expand=False)
        print("Frame positioned")
        self.button_create(self.frames_list[0] ,"Sign In", "#FFFFFF")
    
    def button_create(self ,f ,t ,bcl):
        btn1 = Button(f ,text=t ,bg=bcl ,command = lambda: self.auth_script())
        btn1.pack()
        Button(f, text="Delete_btn", bg =bcl, command = lambda: self.button_del(btn1)).pack()

    def auth_script(self):
        #Auth-Script
        print("Executing-Auth-Script")
        z = 1
        if z:
            print("Authenticated")
            self.frames_del(self.frames_list[0])
            ViewWindow().frames_pos()

class ViewWindow(Window,Win_frames):
    def __init__(self):
        super().__init__()
        super().window_res()

    def frames_pos(self):
        self.text_list = ["Password Chk", "Blocking SSH"]
        self.frames_list = self.frames_gen(2,1,400,400)
        self.frames_list[0].pack(side="top", expand = False)
        self.frames_list[1].pack(side="top", expand = False)
        print("Frame positioned")
        self.button_create(self.frames_list , self.text_list, "#FFFFFF")

    def button_create(self ,f ,t ,bcl):
        btn1 = Button(f[0] ,text=t[0] ,bg=bcl ,command = lambda: self.pass_script())
        btn1.pack()
        btn2 = Button(f[1], text=t[1] ,bg=bcl ,command = lambda: self.secure_ssh())
        btn2.pack()
        Button(f[0], text="Delete_btn", bg =bcl, command = lambda: self.button_del(btn1)).pack()
        Button(f[1], text="Delete_btn", bg =bcl, command = lambda: self.button_del(btn2)).pack()

    def pass_script(self):
        print("Password Policy Script")

    def secure_ssh(self):
        print("Secure shell ssh")


if __name__=="__main__":
    AuthWindow().frames_pos()
    win.mainloop()

