import pkg_resources
import subprocess

class Configure:
    def config_tk(self):
        print("Config-Chk")
        # Check if python3-tk is already installed
        try:
            subprocess.run(["python3", "-c", "import tkinter"], check=True)
            print("python3-tk is already installed.")
        except subprocess.CalledProcessError:
            # If an error occurred, it means tkinter is not installed, so we'll try to install it
            try:
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "python3-tk"], check=True)
                print("python3-tk has been installed.")
            except subprocess.CalledProcessError:
                print("Failed to install python3-tk. Please check your internet connection or try manually.")

    def config_package(self,package_name):
        try:
            pkg_resources.get_distribution(package_name)
        except pkg_resources.DistributionNotFound:
            try:
                subprocess.check_call(["pip3", "install", package_name])
                print(f"{package_name} has been successfully installed.")
            except subprocess.CalledProcessError as e:
                print(f"Error installing {package_name}: {e}")

Configure().config_tk()
Configure().config_package(package_name = "multipledispatch")

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
from abc import ABC , abstractmethod
from multipledispatch import dispatch
import threading


win=Tk()

class DIFace:
    class ColorParameters: 
        def color_loader(self):
            pass

    class HeightWidthParameters:
        def set_height_width(self,height,width):
            self.height=height
            self.width=width

        def set_title(self,title):
            self.title = title


class Window(DIFace.HeightWidthParameters,DIFace.ColorParameters):
    def __init__(self):
        super().set_height_width(500,500)
        super().set_title("Xenon")

    def set_res(self):
        win.geometry("500x500")
        win.maxsize(self.width, self.height)
        win.minsize(self.width, self.height)
        win.title(self.title)
        win.configure(bg="#FFFFFF")

class LIFace:
    class WinFrame(ABC,DIFace.HeightWidthParameters):
        @dispatch()
        def main_frame_gen(self):
            self.main_frame=Frame(win ,borderwidth=1 ,relief=SUNKEN ,width=self.width ,height=self.height)
            self.main_frame.pack(fill = BOTH, expand = True)
            self.main_frame.pack_propagate(0)
            self.main_frame.place(anchor = 'center', relx = 0.5, rely = 0.5)
            return self.main_frame

        @dispatch(float,float)
        def main_frame_gen(self,height_factor,width_factor):
            self.main_frame=Frame(win ,borderwidth=1 ,relief=SUNKEN ,width=int(self.width * width_factor) ,height= int(self.height * height_factor))
            self.main_frame.pack(fill = BOTH, expand = True)
            self.main_frame.pack_propagate(0)
            self.main_frame.place(anchor = 'center', relx = 0.5, rely = 0.5)
            return self.main_frame
    
        @dispatch(int ,int ,float ,float ,str)
        def child_frame_gen(self, frame_count, borderwidth, height_factor, width_factor, color):
            gen_frame_list = []
            for i in range(1,frame_count+1):
                gen_frame_list.append(Frame(self.main_frame, bg=color ,borderwidth=borderwidth, relief=SUNKEN, width=int(self.width*width_factor), height= int(self.height*height_factor)))
            return gen_frame_list
    
        @dispatch(int ,list ,int ,float ,float ,str)
        def child_frame_gen(self, frame_count, frame_list,  borderwidth, height_factor, width_factor, color):
            gen_frame_list=[]
            for i in range(1,frame_count+1):
                gen_frame_list.append(Frame(frame_list[0], bg=color ,borderwidth=borderwidth, relief=SUNKEN, width= int(self.width*width_factor), height= int(self.height*height_factor)))
            return gen_frame_list
        
        @abstractmethod
        def child_frame_pos(self):
            pass

        def child_frame_del(self,obj_list):
            for obj in obj_list:
                obj.destroy()

        def main_frame_del(self):
            self.main_frame.destroy()

    class WinButton(ABC):
        @abstractmethod
        def button_cre(self ,frame ,thickness ,backgroundcolor):
            pass

        def button_del(self,obj):
            obj.destroy()

    class WinLabel(ABC):
        @abstractmethod
        def label_pos(self):
            pass

        def label_del(self,obj):
            obj.destroy()

    class WinEntry(ABC):
        def entry_cre(self ,frame ,frame_count, font, hlb, hlt, color):
            entry_list=[]
            for i in range(1, frame_count+1):
                entry_list.append(Entry(frame, font = font, highlightbackground = hlb, highlightthickness = hlt, fg = color))
            return entry_list

        @abstractmethod
        def entry_pos(self):
            pass

        def entry_del(self,obj):
            obj.destroy()

        @abstractmethod
        def entry_erase(self,obj):
            pass        

    class WinRadial(ABC):
        @abstractmethod
        def radial_cre(self,frame,frame_count):
            pass

        def radial_del(self,obj_list):
            for obj in obj_list:
                obj.destroy()

    class WinMenu(ABC):
        @abstractmethod
        def menu_cre(self):
            pass

        def menu_del(self):
            win.configure(menu = "")

    class WinTextBox(ABC,DIFace.HeightWidthParameters):
        def textbox_cre(self,frame,height_factor,width_factor):
            obj = Text(frame, height = int(self.height*height_factor), width = int(self.width*width_factor))
            return obj

        @abstractmethod
        def textbox_pos(self):
            pass

        def textbox_del(self,obj):
            obj.destroy()


class EIFace:
    class FSManager(ABC):
        def is_path_exist(self,path):
            return

        @abstractmethod
        def show_inner(self,path):
            pass


class LBuilder(LIFace.WinFrame,LIFace.WinButton,LIFace.WinEntry,LIFace.WinMenu,LIFace.WinTextBox,LIFace.WinRadial):
    def __init__(self):
        return

    def child_frame_pos(self):
        pass
            
    def button_cre(self ,frame ,text ,backgroundcolor):
        pass

    def label_pos(self):
        pass

    def entry_pos(self):
        pass

    def entry_erase(self,obj):
        pass        

    def radial_cre(self,frame,frame_count):
        pass

    def menu_cre(self):
        pass

    def textbox_pos(self):
        pass
        


class Entry(Window,LBuilder):
    def __init__(self):
        super().__init__()
        super().set_res()
    
    def color_loader(self):
        self.black ="#000000"
        self.white = "#FFFFFF"
        self.grey = "#808080"
        self.d_grey = "#008080"
        self.l_grey = "#CDCDCD"

    def child_frame_pos(self):
        self.color_loader()

        self.main_frame = self.main_frame_gen(1.0,1.0)
        print(int(self.height*0.96))

        self.design_frame_list = self.child_frame_gen(1, 1, 1.0, 0.3, self.d_grey)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, 1.0, 0.7, self.white)
        self.frame_list[0].pack(side="left")
        self.frame_list[0].pack_propagate(0)
        
        self.child_frame_list_1 = self.child_frame_gen(1,self.frame_list,1,0.9,0.7,self.white)
        self.child_frame_list_1[0].pack(side="top")
        self.child_frame_list_1[0].pack_propagate(0)
        
        self.child_frame_list_2 = self.child_frame_gen(1,self.frame_list,1,0.1,0.7,self.white)
        self.child_frame_list_2[0].pack(side="top")
        self.child_frame_list_2[0].pack_propagate(0)
        
        txt = ["next","quit"]
        
        print("Frame positioned")
        self.button_cre(self.child_frame_list_2[0],txt,self.white)
        print("Button created")
        
        self.label_pos()
        
    
    def label_pos(self):
        head_label_font = font.Font(size = 15)
        
        self.head_label = Label(self.child_frame_list_1[0], text = "Policy", bg=self.white, font = head_label_font)
        
        self.head_label.place(x = 40, y = 60)
    
    def decide(self,x):
        #Logic
        print(x)
        
    def button_cre(self,frame,txt,bcl):
        btn1 = Button(frame ,text=txt[0] ,bg=bcl ,command = lambda: self.entry_exe())
        btn1.pack()
        btn1.place(anchor = 'center', relx = 0.8 , rely = 0.4)
        
        btn2 = Button(frame ,text=txt[1] ,bg=bcl ,command = lambda: self.entry_exe())
        btn2.pack()
        btn2.place(anchor = 'center', relx = 0.2 , rely = 0.5)



    def entry_exe(self):
        print("Go to Policy Frame")
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()



class Orchestrate(Window,LBuilder):
    def __init__(self):
        super().__init__()
        super().set_res()
    
    def color_loader(self):
        self.black ="#000000"
        self.white = "#FFFFFF"
        self.grey = "#808080"
        self.d_grey = "#008080"
        self.l_grey = "#CDCDCD"

    def child_frame_pos(self):
        self.color_loader()
        
        self.menu_cre()
        self.main_frame_gen(0.96,1.0)
        
        self.design_frame_list = self.child_frame_gen(1, 1, 1.0, 0.3, self.d_grey)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, 1.0, 0.7, self.white)
        self.frame_list[0].pack(side="left", expand = True, fill = BOTH)
        self.frame_list[0].pack_propagate(0)

        self.grid_frame_list = self.child_frame_gen(9, self.frame_list, 1, 0.5, 0.7, self.white)
        
        count = 0
        for r in range(0,3):
            for col in range(0,3):
                self.grid_frame_list[count].grid(row = r, column = col)
                self.grid_frame_list[count].propagate(0)
                count = count + 1
        
        
        print("Frame positioned")
        user_count = ["User::1","User::2","User::3","User::4","User::5","User::6","User::7","User::8","User::9"]
        self.button_cre(self.grid_frame_list , user_count, self.white)
        
        self.label_pos()

    
    def label_pos(self):
        active_user_label_font = font.Font(size = 11)
        
        self.active_user_label = Label(self.design_frame_list[0], text = "Active User:", bg=self.d_grey, font = active_user_label_font)
        
        self.active_user_label.place(x = 20, y = 40)

    
    def button_cre(self ,frame ,txt ,bcl):
        self.btn = []
        
        self.back_button = Button(self.design_frame_list[0], text="back", bg=self.d_grey, command = lambda: self.back_entry_exe())
        self.back_button.place(x = 35, y = 400)

        self.btn.append(Button(frame[0], text=txt[0] ,bg=bcl , padx = 25, pady = 32, command = lambda: self.execute_next_win()))
        self.btn.append(Button(frame[1], text=txt[1] ,bg=bcl , padx = 25, pady = 32))
        self.btn.append(Button(frame[2], text=txt[2] ,bg=bcl , padx = 25, pady = 32))
        self.btn.append(Button(frame[3], text=txt[3] ,bg=bcl , padx = 25, pady = 32))
        self.btn.append(Button(frame[4], text=txt[4] ,bg=bcl , padx = 25, pady = 32))
        self.btn.append(Button(frame[5], text=txt[5] ,bg=bcl , padx = 25, pady = 32))
        self.btn.append(Button(frame[6], text=txt[6] ,bg=bcl , padx = 25, pady = 32))
        self.btn.append(Button(frame[7], text=txt[7] ,bg=bcl , padx = 25, pady = 32))
        self.btn.append(Button(frame[8], text=txt[8] ,bg=bcl , padx = 28, pady = 32))

        for cursor in range(0,9):
            self.btn[cursor].grid(row = cursor//3, column = cursor%3, sticky = "nsew", pady = 15, padx = 5)
    
    def menu_cre(self):
        menu_obj_1 = Menu(win)
        menu_obj_1.add_command(label = "User")
        menu_obj_1.add_command(label = "Group", command = lambda: self.orchs_exe())
        win.config(menu = menu_obj_1)

    def back_entry_exe(self):
        self.menu_del()
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Entry().child_frame_pos()

    def orchs_exe(self):
        print("Go to Policy Frame")
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        EnforcePol().child_frame_pos()
        
    def execute_next_win(self):
        win_thread = threading.Thread(target = win_exe_2)
        win_thread.start()
        win_thread.join()

class EnforcePol(Window,LBuilder):
    def __init__(self):
        super().__init__()
        super().set_res()

    def color_loader(self):
        self.black ="#000000"
        self.white = "#FFFFFF"
        self.grey = "#808080"
        self.d_grey = "#008080"
        self.l_grey = "#CDCDCD"

    def child_frame_pos(self):
        self.color_loader()
        
        self.menu_cre()
        self.main_frame_gen(0.96,1.0)
        
        self.design_frame_list = self.child_frame_gen(1, 1, 1.0, 0.3, self.d_grey)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, 1.0, 0.7, self.white)
        self.frame_list[0].pack(side="left", expand = True, fill = BOTH)
        self.frame_list[0].pack_propagate(0)

        self.grid_frame_list = self.child_frame_gen(9, self.frame_list, 1, 0.5, 0.7, self.white)
        
        count = 0
        for r in range(0,3):
            for col in range(0,3):
                self.grid_frame_list[count].grid(row = r, column = col)
                self.grid_frame_list[count].propagate(0)
                count = count + 1
        
        
        print("Frame positioned")
        group_count = ["Group::1","Group::2","Group::3","Group::4","Group::5","Group::6","Group::7","Group::8","Group::9"]
        self.button_cre(self.grid_frame_list , group_count, self.white)
        
        self.label_pos()

    
    def label_pos(self):
        active_user_label_font = font.Font(size = 11)
        
        self.active_user_label = Label(self.design_frame_list[0], text = "Active User:", bg=self.d_grey, font = active_user_label_font)
        
        self.active_user_label.place(x = 20, y = 40)
        

    def menu_cre(self):
        menu_obj_1 = Menu(win)
        menu_obj_1.add_command(label = "User", command = lambda:self.back_orchs_exe())
        menu_obj_1.add_command(label = "Group")
        win.config(menu = menu_obj_1)


    def button_cre(self ,frame ,txt ,bcl):
        self.btn = []

        self.back_button = Button(self.design_frame_list[0], text="back", bg=self.d_grey, command = lambda: self.back_entry_exe())
        self.back_button.place(x = 35, y = 400)


        self.btn.append(Button(frame[0], text=txt[0] ,bg=bcl , padx = 21, pady = 32, command = lambda: self.execute_next_win()))
        self.btn.append(Button(frame[1], text=txt[1] ,bg=bcl , padx = 21, pady = 32))
        self.btn.append(Button(frame[2], text=txt[2] ,bg=bcl , padx = 21, pady = 32))
        self.btn.append(Button(frame[3], text=txt[3] ,bg=bcl , padx = 21, pady = 32))
        self.btn.append(Button(frame[4], text=txt[4] ,bg=bcl , padx = 21, pady = 32))
        self.btn.append(Button(frame[5], text=txt[5] ,bg=bcl , padx = 21, pady = 32))
        self.btn.append(Button(frame[6], text=txt[6] ,bg=bcl , padx = 21, pady = 32))
        self.btn.append(Button(frame[7], text=txt[7] ,bg=bcl , padx = 21, pady = 32))
        self.btn.append(Button(frame[8], text=txt[8] ,bg=bcl , padx = 21, pady = 32))

        for cursor in range(0,9):
            self.btn[cursor].grid(row = cursor//3, column = cursor%3, sticky = "nsew", pady = 15, padx = 5)

    def back_entry_exe(self):
        self.menu_del()
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Entry().child_frame_pos()

    def back_orchs_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.grid_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()
        
    def execute_next_win(self):
        win_thread = threading.Thread(target = win_exe_1)
        win_thread.start()
        win_thread.join()

       
def win_exe_1():
       win_1 = Tk()
       win_1.mainloop()
       
def win_exe_2():
       win_2 = Tk()
       win_2.mainloop()

if __name__=="__main__":
    #Pop-Up Configuration
    Entry().child_frame_pos()
    win.mainloop()



