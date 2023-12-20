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
import subprocess
import os
import pwd


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
        
        txt = ["NEXT","QUIT"]
        
        print("Frame positioned")
        self.button_cre(self.child_frame_list_2[0],txt,self.white)
        print("Button created")
        
        self.label_pos()
        
    
    def label_pos(self):
        head_label_font = font.Font(size = 30)
        
        self.head_label = Label(self.child_frame_list_1[0], text = "Kaizen \n ", bg=self.white, font = head_label_font)
        
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
            for col in range(0,2):
                self.grid_frame_list[count].grid(row = r, column = col)
                self.grid_frame_list[count].propagate(0)
                count = count + 1
        
        
        print("Frame positioned")
        user_count = ["Init Setup","Services  ","Config Net","Log-Audit","  AAA  ","System M"]
        self.button_cre(self.grid_frame_list , user_count, self.white)
        
        self.label_pos()

    
    def label_pos(self):
        pass

    
    def button_cre(self ,frame ,txt ,bcl):
        self.btn = []
        
        self.back_button = Button(self.design_frame_list[0], text="back", bg=self.d_grey, command = lambda: self.back_entry_exe())
        self.back_button.place(x = 35, y = 400)

        self.btn.append(Button(frame[0], text=txt[0] ,bg=bcl , padx = 25, pady = 20, command = lambda: self.initial_setup()))
        self.btn.append(Button(frame[1], text=txt[1] ,bg=bcl , padx = 20, pady = 20, command = lambda: self.service()))
        self.btn.append(Button(frame[2], text=txt[2] ,bg=bcl , padx = 20, pady = 20, command = lambda: self.config_network()))
        self.btn.append(Button(frame[3], text=txt[3] ,bg=bcl , padx = 20, pady = 20, command = lambda: self.log_audit()))
        self.btn.append(Button(frame[4], text=txt[4] ,bg=bcl , padx = 25, pady = 20, command = lambda: self.aaa()))
        self.btn.append(Button(frame[5], text=txt[5] ,bg=bcl , padx = 20, pady = 20, command = lambda: self.system_m()))
        
        
        self.btn[0].grid(row = 0, column = 0, sticky = "nsew", pady = 25, padx = 20)
        self.btn[1].grid(row = 0, column = 1, sticky = "nsew", pady = 20, padx = 20)
        self.btn[2].grid(row = 1, column = 0, sticky = "nsew", pady = 20, padx = 20)
        self.btn[3].grid(row = 1, column = 1, sticky = "nsew", pady = 20, padx = 20)
        self.btn[4].grid(row = 2, column = 0, sticky = "nsew", pady = 25, padx = 20)
        self.btn[5].grid(row = 2, column = 2, sticky = "nsew", pady = 20, padx = 20)
    

    def back_entry_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Entry().child_frame_pos()

    def initial_setup(self):
        print("Go to Policy Frame")
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Init_Setup().child_frame_pos()
        
    def service(self):
        print("Go to Policy Frame")
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Service().child_frame_pos()
        
    def config_network(self):
        print("Go to Policy Frame")
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Config_Network().child_frame_pos() 
        
    def log_audit(self):
        print("Go to Policy Frame")
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Log_Audit().child_frame_pos()
        
    def aaa(self):
        print("Go to Policy Frame")
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        AAA().child_frame_pos()
        
    def system_m(self):
        print("Go to Policy Frame")
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        System_M().child_frame_pos()

class Init_Setup(Window,LBuilder):
    def __init__(self):
        super().__init__()
        super().set_res()
        
    def fun1(self):
        # Define the path to your batch script 
        bat_script = "/home/tanir/Downloads/1_1_1.bats" 
 
        # Use subprocess to run the batch script 
        result=subprocess.run(['bats', bat_script], capture_output=True, text=True)
        
        if result.returncode == 0:
                print("Bats file executed successfully")
                print("Output:\n", result.stdout)
        else:
                print("Error executing Bats file")
                print("Error message:\n", result.stderr)
                
    def fun2(self):
         # Define the path to your batch script 
         bat_script = "/home/tanir/Downloads/1_1_2.bats" 
 
         # Use subprocess to run the batch script 
         result=subprocess.run(['bats', bat_script], capture_output=True, text=True)
        
         if result.returncode == 0:
                print("Bats file executed successfully")
                print("Output:\n", result.stdout)
         else:
                print("Error executing Bats file")
                print("Error message:\n", result.stderr)
                
    def fun3(self):
         # Define the path to your batch script 
         bat_script = "/home/tanir/Downloads/1_1_3.bats" 
 
         # Use subprocess to run the batch script 
         result=subprocess.run(['bats', bat_script], capture_output=True, text=True)
        
         if result.returncode == 0:
                print("Bats file executed successfully")
                print("Output:\n", result.stdout)
         else:
                print("Error executing Bats file")
                print("Error message:\n", result.stderr)




    def color_loader(self):
        self.black ="#000000"
        self.white = "#FFFFFF"
        self.grey = "#808080"
        self.d_grey = "#008080"
        self.l_grey = "#CDCDCD"

    def child_frame_pos(self):
        self.color_loader()
        
        self.main_frame_gen(0.96,1.0)
        
        self.design_frame_list = self.child_frame_gen(1, 1, 1.0, 0.3, self.d_grey)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, 1.0, 0.7, self.white)
        self.frame_list[0].pack(side="left", expand = True, fill = BOTH)
        self.frame_list[0].pack_propagate(0)

        self.grid_frame_list = self.child_frame_gen(2, self.frame_list, 1, 1.0, 0.35, self.white)
        
        self.grid_frame_list_c1 = self.child_frame_gen(8,self.grid_frame_list,1,0.125,0.35,self.white)
        
        self.grid_frame_list_c2 = self.child_frame_gen(8,self.grid_frame_list[1:],1,0.125,0.35, self.white)
        
        count = 0
        for r in range(0,1):
            for col in range(0,2):
                self.grid_frame_list[count].grid(row = r, column = col)
                self.grid_frame_list[count].propagate(0)
                count = count + 1
                
        count_1 = 0
        for r in range(0,8):
            for col in range(0,1):
                self.grid_frame_list_c1[count_1].grid(row = r, column = col)
                self.grid_frame_list_c1[count_1].propagate(0)
                count_1 = count_1 + 1
         
        count_2 = 0
        for r in range(0,8):
            for col in range(1,2):
                self.grid_frame_list_c2[count_2].grid(row = r, column = col)
                self.grid_frame_list_c2[count_2].propagate(0)
                count_2 = count_2 + 1

        self.final_grid_frame_list = self.grid_frame_list_c1 + self.grid_frame_list_c2
        count_f = count_1 + count_2
        
        print("Frame positioned")
        group_count = ["Config_var_tmp","Config_var_log","Filesystem Int. Pol.","etc_issue","etc_motd","Apparmour"]
        self.button_cre(self.final_grid_frame_list , group_count, self.white)
        
        self.label_pos()

    
    def label_pos(self):
        active_user_label_font = font.Font(size = 11)
        
        self.level_1 = Label(self.grid_frame_list_c1[0], text = "Level-1", bg=self.d_grey, font = active_user_label_font)
        self.level_1.place(x = 12, y = 40)
        
        self.level_2 = Label(self.grid_frame_list_c2[0], text = "Level-2", bg=self.d_grey, font = active_user_label_font)
        self.level_2.place(x = 20, y = 40)


    def button_cre(self ,frame ,txt ,bcl):
        self.btn = []

        self.back_button = Button(self.design_frame_list[0], text="back", bg=self.d_grey, command = lambda: self.back_entry_exe())
        self.back_button.place(x = 35, y = 400)

        check_list_1=[]
	
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
	
        self.btn.append(Checkbutton(frame[1], text=txt[0] ,onvalue =1, offvalue = 0, height =3, width =15, command=lambda: self.fun1()))
        self.btn[0].grid(row = 0, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[2], text=txt[1] ,onvalue =1, offvalue = 0, height =3, width =15, command=lambda: self.fun2()))
        self.btn[1].grid(row = 0, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[3], text=txt[2] ,onvalue =1, offvalue = 0, height =3, width =15, command=lambda: self.fun3()))
        self.btn[2].grid(row = 1, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[4], text=txt[3] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[3].grid(row = 1, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[5], text=txt[4] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[4].grid(row = 2, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[6], text=txt[5] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[5].grid(row = 2, column = 1, sticky="nsew")
        
         
        self.btn.append(Checkbutton(frame[9], text=txt[6] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[6].grid(row = 3, column = 0, sticky="nsew")
         
        self.btn.append(Checkbutton(frame[10], text=txt[7] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[7].grid(row = 3, column = 1, sticky="nsew")
       
        self.btn.append(Checkbutton(frame[11], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[8].grid(row = 4, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[12], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[9].grid(row = 4, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[13], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[10].grid(row = 5, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[14], text=txt[9] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[11].grid(row = 5, column = 1, sticky="nsew")

    def back_entry_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()

    def back_orchs_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.grid_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()
        
class Log_Audit(Window,LBuilder):
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
        
        self.main_frame_gen(0.96,1.0)
        
        self.design_frame_list = self.child_frame_gen(1, 1, 1.0, 0.3, self.d_grey)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, 1.0, 0.7, self.white)
        self.frame_list[0].pack(side="left", expand = True, fill = BOTH)
        self.frame_list[0].pack_propagate(0)

        self.grid_frame_list = self.child_frame_gen(2, self.frame_list, 1, 1.0, 0.35, self.white)
        
        self.grid_frame_list_c1 = self.child_frame_gen(8,self.grid_frame_list,1,0.125,0.35,self.white)
        
        self.grid_frame_list_c2 = self.child_frame_gen(8,self.grid_frame_list[1:],1,0.125,0.35, self.white)
        
        count = 0
        for r in range(0,1):
            for col in range(0,2):
                self.grid_frame_list[count].grid(row = r, column = col)
                self.grid_frame_list[count].propagate(0)
                count = count + 1
                
        count_1 = 0
        for r in range(0,8):
            for col in range(0,1):
                self.grid_frame_list_c1[count_1].grid(row = r, column = col)
                self.grid_frame_list_c1[count_1].propagate(0)
                count_1 = count_1 + 1
         
        count_2 = 0
        for r in range(0,8):
            for col in range(1,2):
                self.grid_frame_list_c2[count_2].grid(row = r, column = col)
                self.grid_frame_list_c2[count_2].propagate(0)
                count_2 = count_2 + 1

        self.final_grid_frame_list = self.grid_frame_list_c1 + self.grid_frame_list_c2
        count_f = count_1 + count_2
        
        print("Frame positioned")
        group_count = ["Audiyd_Install Policy","Auditd_Service Policy","Audit_Log Policy","Audit_Delete Policy","Journald Policy","Group::6","Group::7","Group::8","Group::9","Group::10","Group::11","Group::12"]
        self.button_cre(self.final_grid_frame_list , group_count, self.white)
        
        self.label_pos()

    
    def label_pos(self):
        active_user_label_font = font.Font(size = 11)
        
        self.level_1 = Label(self.grid_frame_list_c1[0], text = "Level-1", bg=self.d_grey, font = active_user_label_font)
        self.level_1.place(x = 12, y = 40)
        
        self.level_2 = Label(self.grid_frame_list_c2[0], text = "Level-2", bg=self.d_grey, font = active_user_label_font)
        self.level_2.place(x = 20, y = 40)


    def button_cre(self ,frame ,txt ,bcl):
        self.btn = []

        self.back_button = Button(self.design_frame_list[0], text="back", bg=self.d_grey, command = lambda: self.back_entry_exe())
        self.back_button.place(x = 35, y = 400)

        check_list_1=[]
	
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
	
        self.btn.append(Checkbutton(frame[1], text=txt[0] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[0].grid(row = 0, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[2], text=txt[1] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[1].grid(row = 0, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[3], text=txt[2] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[2].grid(row = 1, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[4], text=txt[3] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[3].grid(row = 1, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[5], text=txt[4] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[4].grid(row = 2, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[6], text=txt[5] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[5].grid(row = 2, column = 1, sticky="nsew")
        
         
        self.btn.append(Checkbutton(frame[9], text=txt[6] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[6].grid(row = 3, column = 0, sticky="nsew")
         
        self.btn.append(Checkbutton(frame[10], text=txt[7] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[7].grid(row = 3, column = 1, sticky="nsew")
       
        self.btn.append(Checkbutton(frame[11], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[8].grid(row = 4, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[12], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[9].grid(row = 4, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[13], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[10].grid(row = 5, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[14], text=txt[9] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[11].grid(row = 5, column = 1, sticky="nsew")

    def back_entry_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()

    def back_orchs_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.grid_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()
        
class System_M(Window,LBuilder):
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
        
        self.main_frame_gen(0.96,1.0)
        
        self.design_frame_list = self.child_frame_gen(1, 1, 1.0, 0.3, self.d_grey)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, 1.0, 0.7, self.white)
        self.frame_list[0].pack(side="left", expand = True, fill = BOTH)
        self.frame_list[0].pack_propagate(0)

        self.grid_frame_list = self.child_frame_gen(2, self.frame_list, 1, 1.0, 0.35, self.white)
        
        self.grid_frame_list_c1 = self.child_frame_gen(8,self.grid_frame_list,1,0.125,0.35,self.white)
        
        self.grid_frame_list_c2 = self.child_frame_gen(8,self.grid_frame_list[1:],1,0.125,0.35, self.white)
        
        count = 0
        for r in range(0,1):
            for col in range(0,2):
                self.grid_frame_list[count].grid(row = r, column = col)
                self.grid_frame_list[count].propagate(0)
                count = count + 1
                
        count_1 = 0
        for r in range(0,8):
            for col in range(0,1):
                self.grid_frame_list_c1[count_1].grid(row = r, column = col)
                self.grid_frame_list_c1[count_1].propagate(0)
                count_1 = count_1 + 1
         
        count_2 = 0
        for r in range(0,8):
            for col in range(1,2):
                self.grid_frame_list_c2[count_2].grid(row = r, column = col)
                self.grid_frame_list_c2[count_2].propagate(0)
                count_2 = count_2 + 1

        self.final_grid_frame_list = self.grid_frame_list_c1 + self.grid_frame_list_c2
        count_f = count_1 + count_2
        
        print("Frame positioned")
        group_count = ["etc Policy","etc-Policy","root policy","etc_Group Policy","etc_Shadow Policy","etc_Gshadow Policy","Group::7","Group::8","Group::9","Group::10","Group::11","Group::12"]
        self.button_cre(self.final_grid_frame_list , group_count, self.white)
        
        self.label_pos()

    
    def label_pos(self):
        active_user_label_font = font.Font(size = 11)
        
        self.level_1 = Label(self.grid_frame_list_c1[0], text = "Level-1", bg=self.d_grey, font = active_user_label_font)
        self.level_1.place(x = 12, y = 40)
        
        self.level_2 = Label(self.grid_frame_list_c2[0], text = "Level-2", bg=self.d_grey, font = active_user_label_font)
        self.level_2.place(x = 20, y = 40)


    def button_cre(self ,frame ,txt ,bcl):
        self.btn = []

        self.back_button = Button(self.design_frame_list[0], text="back", bg=self.d_grey, command = lambda: self.back_entry_exe())
        self.back_button.place(x = 35, y = 400)

        check_list_1=[]
	
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
	
        self.btn.append(Checkbutton(frame[1], text=txt[0] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[0].grid(row = 0, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[2], text=txt[1] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[1].grid(row = 0, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[3], text=txt[2] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[2].grid(row = 1, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[4], text=txt[3] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[3].grid(row = 1, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[5], text=txt[4] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[4].grid(row = 2, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[6], text=txt[5] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[5].grid(row = 2, column = 1, sticky="nsew")
        
         
        self.btn.append(Checkbutton(frame[9], text=txt[6] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[6].grid(row = 3, column = 0, sticky="nsew")
         
        self.btn.append(Checkbutton(frame[10], text=txt[7] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[7].grid(row = 3, column = 1, sticky="nsew")
       
        self.btn.append(Checkbutton(frame[11], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[8].grid(row = 4, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[12], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[9].grid(row = 4, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[13], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[10].grid(row = 5, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[14], text=txt[9] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[11].grid(row = 5, column = 1, sticky="nsew")

    def back_entry_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()

    def back_orchs_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.grid_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()
        
class AAA(Window,LBuilder):
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
        
        self.main_frame_gen(0.96,1.0)
        
        self.design_frame_list = self.child_frame_gen(1, 1, 1.0, 0.3, self.d_grey)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, 1.0, 0.7, self.white)
        self.frame_list[0].pack(side="left", expand = True, fill = BOTH)
        self.frame_list[0].pack_propagate(0)

        self.grid_frame_list = self.child_frame_gen(2, self.frame_list, 1, 1.0, 0.35, self.white)
        
        self.grid_frame_list_c1 = self.child_frame_gen(8,self.grid_frame_list,1,0.125,0.35,self.white)
        
        self.grid_frame_list_c2 = self.child_frame_gen(8,self.grid_frame_list[1:],1,0.125,0.35, self.white)
        
        count = 0
        for r in range(0,1):
            for col in range(0,2):
                self.grid_frame_list[count].grid(row = r, column = col)
                self.grid_frame_list[count].propagate(0)
                count = count + 1
                
        count_1 = 0
        for r in range(0,8):
            for col in range(0,1):
                self.grid_frame_list_c1[count_1].grid(row = r, column = col)
                self.grid_frame_list_c1[count_1].propagate(0)
                count_1 = count_1 + 1
         
        count_2 = 0
        for r in range(0,8):
            for col in range(1,2):
                self.grid_frame_list_c2[count_2].grid(row = r, column = col)
                self.grid_frame_list_c2[count_2].propagate(0)
                count_2 = count_2 + 1

        self.final_grid_frame_list = self.grid_frame_list_c1 + self.grid_frame_list_c2
        count_f = count_1 + count_2
        
        print("Frame positioned")
        group_count = ["Group::1","Group::2","Group::3","Group::4","Group::5","Group::6","Group::7","Group::8","Group::9","Group::10","Group::11","Group::12"]
        self.button_cre(self.final_grid_frame_list , group_count, self.white)
        
        self.label_pos()

    
    def label_pos(self):
        active_user_label_font = font.Font(size = 11)
        
        self.level_1 = Label(self.grid_frame_list_c1[0], text = "Level-1", bg=self.d_grey, font = active_user_label_font)
        self.level_1.place(x = 12, y = 40)
        
        self.level_2 = Label(self.grid_frame_list_c2[0], text = "Level-2", bg=self.d_grey, font = active_user_label_font)
        self.level_2.place(x = 20, y = 40)


    def button_cre(self ,frame ,txt ,bcl):
        self.btn = []

        self.back_button = Button(self.design_frame_list[0], text="back", bg=self.d_grey, command = lambda: self.back_entry_exe())
        self.back_button.place(x = 35, y = 400)

        check_list_1=[]
	
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
	
        self.btn.append(Checkbutton(frame[1], text=txt[0] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[0].grid(row = 0, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[2], text=txt[1] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[1].grid(row = 0, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[3], text=txt[2] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[2].grid(row = 1, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[4], text=txt[3] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[3].grid(row = 1, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[5], text=txt[4] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[4].grid(row = 2, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[6], text=txt[5] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[5].grid(row = 2, column = 1, sticky="nsew")
        
         
        self.btn.append(Checkbutton(frame[9], text=txt[6] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[6].grid(row = 3, column = 0, sticky="nsew")
         
        self.btn.append(Checkbutton(frame[10], text=txt[7] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[7].grid(row = 3, column = 1, sticky="nsew")
       
        self.btn.append(Checkbutton(frame[11], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[8].grid(row = 4, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[12], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[9].grid(row = 4, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[13], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[10].grid(row = 5, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[14], text=txt[9] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[11].grid(row = 5, column = 1, sticky="nsew")

    def back_entry_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()

    def back_orchs_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.grid_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()
        

class Service(Window,LBuilder):
    def __init__(self):
        super().__init__()
        super().set_res()
        
    def fun1(self):
        # Define the path to your batch script 
        bat_script = "/home/tanir/Downloads/2_2_1.bats" 
 
        # Use subprocess to run the batch script 
        result=subprocess.run(['bats', bat_script], capture_output=True, text=True)
        
        if result.returncode == 0:
                print("Bats file executed successfully")
                print("Output:\n", result.stdout)
        else:
                print("Error executing Bats file")
                print("Error message:\n", result.stderr)
                
    def fun2(self):
         # Define the path to your batch script 
         bat_script = "/home/tanir/Downloads/2_2_2.bats" 
 
         # Use subprocess to run the batch script 
         result=subprocess.run(['bats', bat_script], capture_output=True, text=True)
        
         if result.returncode == 0:
                print("Bats file executed successfully")
                print("Output:\n", result.stdout)
         else:
                print("Error executing Bats file")
                print("Error message:\n", result.stderr)

    def color_loader(self):
        self.black ="#000000"
        self.white = "#FFFFFF"
        self.grey = "#808080"
        self.d_grey = "#008080"
        self.l_grey = "#CDCDCD"

    def child_frame_pos(self):
        self.color_loader()
        
        self.main_frame_gen(0.96,1.0)
        
        self.design_frame_list = self.child_frame_gen(1, 1, 1.0, 0.3, self.d_grey)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, 1.0, 0.7, self.white)
        self.frame_list[0].pack(side="left", expand = True, fill = BOTH)
        self.frame_list[0].pack_propagate(0)

        self.grid_frame_list = self.child_frame_gen(2, self.frame_list, 1, 1.0, 0.35, self.white)
        
        self.grid_frame_list_c1 = self.child_frame_gen(8,self.grid_frame_list,1,0.125,0.35,self.white)
        
        self.grid_frame_list_c2 = self.child_frame_gen(8,self.grid_frame_list[1:],1,0.125,0.35, self.white)
        
        count = 0
        for r in range(0,1):
            for col in range(0,2):
                self.grid_frame_list[count].grid(row = r, column = col)
                self.grid_frame_list[count].propagate(0)
                count = count + 1
                
        count_1 = 0
        for r in range(0,8):
            for col in range(0,1):
                self.grid_frame_list_c1[count_1].grid(row = r, column = col)
                self.grid_frame_list_c1[count_1].propagate(0)
                count_1 = count_1 + 1
         
        count_2 = 0
        for r in range(0,8):
            for col in range(1,2):
                self.grid_frame_list_c2[count_2].grid(row = r, column = col)
                self.grid_frame_list_c2[count_2].propagate(0)
                count_2 = count_2 + 1

        self.final_grid_frame_list = self.grid_frame_list_c1 + self.grid_frame_list_c2
        count_f = count_1 + count_2
        
        print("Frame positioned")
        group_count = ["Group::1","Group::2","Group::3","Group::4","Group::5","Group::6","http policy","DNS Policy","NFS Policy","Telnet Policy","NIS Policy","Group::12"]
        self.button_cre(self.final_grid_frame_list , group_count, self.white)
        
        self.label_pos()

    
    def label_pos(self):
        active_user_label_font = font.Font(size = 11)
        
        self.level_1 = Label(self.grid_frame_list_c1[0], text = "Level-1", bg=self.d_grey, font = active_user_label_font)
        self.level_1.place(x = 12, y = 40)
        
        self.level_2 = Label(self.grid_frame_list_c2[0], text = "Level-2", bg=self.d_grey, font = active_user_label_font)
        self.level_2.place(x = 20, y = 40)


    def button_cre(self ,frame ,txt ,bcl):
        self.btn = []

        self.back_button = Button(self.design_frame_list[0], text="back", bg=self.d_grey, command = lambda: self.back_entry_exe())
        self.back_button.place(x = 35, y = 400)

        check_list_1=[]
	
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
	
        self.btn.append(Checkbutton(frame[1], text=txt[0] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[0].grid(row = 0, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[2], text=txt[1] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[1].grid(row = 0, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[3], text=txt[2] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[2].grid(row = 1, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[4], text=txt[3] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[3].grid(row = 1, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[5], text=txt[4] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[4].grid(row = 2, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[6], text=txt[5] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[5].grid(row = 2, column = 1, sticky="nsew")
        
         
        self.btn.append(Checkbutton(frame[9], text=txt[6] ,onvalue =1, offvalue = 0, height =3, width =15, command=lambda: self.fun1()))
        self.btn[6].grid(row = 3, column = 0, sticky="nsew")
         
        self.btn.append(Checkbutton(frame[10], text=txt[7] ,onvalue =1, offvalue = 0, height =3, width =15, command=lambda: self.fun2()))
        self.btn[7].grid(row = 3, column = 1, sticky="nsew")
       
        self.btn.append(Checkbutton(frame[11], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[8].grid(row = 4, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[12], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[9].grid(row = 4, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[13], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[10].grid(row = 5, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[14], text=txt[9] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[11].grid(row = 5, column = 1, sticky="nsew")

    def back_entry_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()

    def back_orchs_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.grid_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()
        
class Config_Network(Window,LBuilder):
    def __init__(self):
        super().__init__()
        super().set_res()
        
    def fun1(self):
        # Define the path to your batch script 
        bat_script = "/home/tanir/Downloads/3_1_1.bats" 
 
        # Use subprocess to run the batch script 
        result=subprocess.run(['bats', bat_script], capture_output=True, text=True)
        
        if result.returncode == 0:
                print("Bats file executed successfully")
                print("Output:\n", result.stdout)
        else:
                print("Error executing Bats file")
                print("Error message:\n", result.stderr)
                
    def fun2(self):
        # Define the path to your batch script 
        bat_script = "/home/tanir/Downloads/3_1_2.bats" 
 
        # Use subprocess to run the batch script 
        result=subprocess.run(['bats', bat_script], capture_output=True, text=True)
        
        if result.returncode == 0:
                print("Bats file executed successfully")
                print("Output:\n", result.stdout)
        else:
                print("Error executing Bats file")
                print("Error message:\n", result.stderr)
                
    def fun3(self):
        # Define the path to your batch script 
        bat_script = "/home/tanir/Downloads/3_1_3.bats" 
 
        # Use subprocess to run the batch script 
        result=subprocess.run(['bats', bat_script], capture_output=True, text=True)
        
        if result.returncode == 0:
                print("Bats file executed successfully")
                print("Output:\n", result.stdout)
        else:
                print("Error executing Bats file")
                print("Error message:\n", result.stderr)
                
    def fun4(self):
        # Define the path to your batch script 
        bat_script = "/home/tanir/Downloads/3_1_4.bats" 
 
        # Use subprocess to run the batch script 
        result=subprocess.run(['bats', bat_script], capture_output=True, text=True)
        
        if result.returncode == 0:
                print("Bats file executed successfully")
                print("Output:\n", result.stdout)
        else:
                print("Error executing Bats file")
                print("Error message:\n", result.stderr)

    def color_loader(self):
        self.black ="#000000"
        self.white = "#FFFFFF"
        self.grey = "#808080"
        self.d_grey = "#008080"
        self.l_grey = "#CDCDCD"

    def child_frame_pos(self):
        self.color_loader()
        
        self.main_frame_gen(0.96,1.0)
        
        self.design_frame_list = self.child_frame_gen(1, 1, 1.0, 0.3, self.d_grey)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, 1.0, 0.7, self.white)
        self.frame_list[0].pack(side="left", expand = True, fill = BOTH)
        self.frame_list[0].pack_propagate(0)

        self.grid_frame_list = self.child_frame_gen(2, self.frame_list, 1, 1.0, 0.35, self.white)
        
        self.grid_frame_list_c1 = self.child_frame_gen(8,self.grid_frame_list,1,0.125,0.35,self.white)
        
        self.grid_frame_list_c2 = self.child_frame_gen(8,self.grid_frame_list[1:],1,0.125,0.35, self.white)
        
        count = 0
        for r in range(0,1):
            for col in range(0,2):
                self.grid_frame_list[count].grid(row = r, column = col)
                self.grid_frame_list[count].propagate(0)
                count = count + 1
                
        count_1 = 0
        for r in range(0,8):
            for col in range(0,1):
                self.grid_frame_list_c1[count_1].grid(row = r, column = col)
                self.grid_frame_list_c1[count_1].propagate(0)
                count_1 = count_1 + 1
         
        count_2 = 0
        for r in range(0,8):
            for col in range(1,2):
                self.grid_frame_list_c2[count_2].grid(row = r, column = col)
                self.grid_frame_list_c2[count_2].propagate(0)
                count_2 = count_2 + 1

        self.final_grid_frame_list = self.grid_frame_list_c1 + self.grid_frame_list_c2
        count_f = count_1 + count_2
        
        print("Frame positioned")
        group_count = ["Network Parameter","UFW Policy","TCP_SYN Policy","NF Tables","Group::5","Group::6","Group::7","Group::8","Group::9","Group::10","Group::11","Group::12"]
        self.button_cre(self.final_grid_frame_list , group_count, self.white)
        
        self.label_pos()

    
    def label_pos(self):
        active_user_label_font = font.Font(size = 11)
        
        self.level_1 = Label(self.grid_frame_list_c1[0], text = "Level-1", bg=self.d_grey, font = active_user_label_font)
        self.level_1.place(x = 12, y = 40)
        
        self.level_2 = Label(self.grid_frame_list_c2[0], text = "Level-2", bg=self.d_grey, font = active_user_label_font)
        self.level_2.place(x = 20, y = 40)


    def button_cre(self ,frame ,txt ,bcl):
        self.btn = []

        self.back_button = Button(self.design_frame_list[0], text="back", bg=self.d_grey, command = lambda: self.back_entry_exe())
        self.back_button.place(x = 35, y = 400)

        check_list_1=[]
	
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
        check_list_1.append(IntVar())
	
        self.btn.append(Checkbutton(frame[1], text=txt[0] ,onvalue =1, offvalue = 0, height =3, width =15, command=lambda: self.fun1()))
        self.btn[0].grid(row = 0, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[2], text=txt[1] ,onvalue =1, offvalue = 0, height =3, width =15, command=lambda: self.fun2()))
        self.btn[1].grid(row = 0, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[3], text=txt[2] ,onvalue =1, offvalue = 0, height =3, width =15, command=lambda: self.fun3()))
        self.btn[2].grid(row = 1, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[4], text=txt[3] ,onvalue =1, offvalue = 0, height =3, width =15, command=lambda: self.fun4()))
        self.btn[3].grid(row = 1, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[5], text=txt[4] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[4].grid(row = 2, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[6], text=txt[5] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[5].grid(row = 2, column = 1, sticky="nsew")
        
         
        self.btn.append(Checkbutton(frame[9], text=txt[6] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[6].grid(row = 3, column = 0, sticky="nsew")
         
        self.btn.append(Checkbutton(frame[10], text=txt[7] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[7].grid(row = 3, column = 1, sticky="nsew")
       
        self.btn.append(Checkbutton(frame[11], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[8].grid(row = 4, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[12], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[9].grid(row = 4, column = 1, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[13], text=txt[8] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[10].grid(row = 5, column = 0, sticky="nsew")
        
        self.btn.append(Checkbutton(frame[14], text=txt[9] ,onvalue =1, offvalue = 0, height =3, width =15))
        self.btn[11].grid(row = 5, column = 1, sticky="nsew")

    def back_entry_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()

    def back_orchs_exe(self):
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.grid_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        Orchestrate().child_frame_pos()



if __name__=="__main__":
    #Pop-Up Configuration
    Entry().child_frame_pos()
    win.mainloop()
