import pkg_resources
import subprocess

class Configure:
    def config_tk(self):
        print("Config-Chk")
        """
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
                """

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
from abc import ABC , abstractmethod
from multipledispatch import dispatch


win=Tk()


class SharedSpace:
    def set_height_width(self,height,width):
        self.height=height
        self.width=width

    def set_title(self,title):
        self.title = title


class DIFace:
    class ColorParameters(ABC): 
        @abstractmethod
        def color_loader(self):
            pass


class Window(SharedSpace):
    def __init__(self):
        super().set_height_width(500,500)
        super().set_title("Xenon")

    def set_res(self):
        win.geometry("500x500")
        win.maxsize(self.width, self.height)
        win.minsize(self.width, self.height)
        win.title(self.title)

class LIFace:
    class WinFrame(ABC,SharedSpace):
        @dispatch()
        def main_frame_gen(self):
            self.main_frame=Frame(win ,borderwidth=1 ,relief=SUNKEN ,width=self.width ,height=self.height)
            self.main_frame.pack(fill = BOTH, expand = True)
            self.main_frame.pack_propagate(0)
            self.main_frame.place(anchor = 'center', relx = 0.5, rely = 0.5)
            return self.main_frame

        @dispatch(int)
        def main_frame_gen(self,height_factor):
            self.main_frame=Frame(win ,borderwidth=1 ,relief=SUNKEN ,width=self.width ,height= self.height - height_factor)
            self.main_frame.pack(fill = BOTH, expand = True)
            self.main_frame.pack_propagate(0)
            self.main_frame.place(anchor = 'center', relx = 0.5, rely = 0.5)
            return self.main_frame
    
        @dispatch(int ,int ,int ,int ,str)
        def child_frame_gen(self, frame_count, borderwidth, height, width, color):
            gen_frame_list = []
            for i in range(1,frame_count+1):
                gen_frame_list.append(Frame(self.main_frame, bg=color ,borderwidth=borderwidth, relief=SUNKEN, width=width, height=height))
            return gen_frame_list
    
        @dispatch(int ,list ,int ,int ,int ,str)
        def child_frame_gen(self, frame_count, frame_list,  borderwidth, height, width, color):
            gen_frame_list=[]
            for i in range(1,frame_count+1):
                gen_frame_list.append(Frame(frame_list[0], bg=color ,borderwidth=borderwidth, relief=SUNKEN, width=width, height=height))
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
        def button_cre(self ,f ,t ,bcl):
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

        def menu_del(self, obj):
            obj.destroy()

    class WinTextBox(ABC):
        def textbox_cre(self,frame,ht,wd):
            obj = Text(frame, height = ht, width = wd)
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

class Authorize(Window,LIFace.WinFrame,LIFace.WinButton,LIFace.WinEntry,DIFace.ColorParameters):
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

        self.main_frame_gen()
        self.design_frame_list = self.child_frame_gen(2, 1, int(0.2*self.height), self.width,  self.d_grey)
        self.frame_list = self.child_frame_gen(1, 1, int(0.6*self.height), self.width, self.white)

        self.design_frame_list[0].pack(side="top", expand=False)
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list[0].pack(side="top", expand=False)
        self.frame_list[0].pack_propagate(0)

        self.design_frame_list[1].pack(side="top", expand=False)
        self.design_frame_list[1].pack_propagate(0)
        print("Frame positioned")
        
        #self.entry_pos()
        
        self.button_cre(self.frame_list[0] ,"Login", self.white)
        print("Button positioned")
    


    def entry_pos(self):
        self.entry_list = self.entry_cre(self.frame_list[0], 3, "Bitter", self.l_grey, 1, self.grey)
        '''
        self.entry_list[0].insert(0,"Username")
        self.entry_list[0].bind("<FocusIn>", lambda event: self.entry_erase(self.entry_list[0]))
        self.entry_list[0].pack()
        self.entry_list[0].place(anchor = 'center', relx = 0.5, rely = 0.2)
        
        self.entry_list[1].insert(0,"Role")
        self.entry_list[1].bind("<FocusIn>", lambda event: self.entry_erase(self.entry_list[1]))
        self.entry_list[1].pack()
        self.entry_list[1].place(anchor = 'center', relx = 0.5, rely = 0.4)

        self.entry_list[2].insert(0,"Password")
        self.entry_list[2].bind("<FocusIn>", lambda event: self.entry_erase(self.entry_list[2]))
        self.entry_list[2].pack()
        self.entry_list[2].place(anchor = 'center', relx = 0.5, rely = 0.6)
        '''
        print("Entry positioned")

    def entry_erase(self,obj):
        obj.delete(0, "end")
        obj.configure(fg = self.black)

    def button_cre(self ,f ,t ,bcl):
        btn1 = Button(f ,text=t ,bg=bcl ,command = lambda: self.auth_exe())
        btn1.pack()
        btn1.place(anchor = 'center', relx = 0.5, rely = 0.8)

    def auth_exe(self):
        #Auth-Script
        print("Executing-Auth-Script")
        z = 1
        if z:
            print("Authenticated")
            self.child_frame_del(self.design_frame_list)
            self.child_frame_del(self.frame_list)
            self.main_frame_del()
            Orchestrate().child_frame_pos()

class Orchestrate(Window,LIFace.WinFrame,LIFace.WinMenu,LIFace.WinRadial,DIFace.ColorParameters):
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
        self.main_frame = self.main_frame_gen(20)

        self.design_frame_list = self.child_frame_gen(1, 1, 480, int(0.3*self.width), self.d_grey)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, 480, int(0.7*self.width), self.white)
        self.frame_list[0].pack(side="left")
        self.frame_list[0].pack_propagate(0)
        
        print("Frame positioned")
        self.radial_cre(self.frame_list[0], 2)

    def menu_cre(self):
        menu_obj_1 = Menu(win)
        menu_obj_1.add_command(label = "Orchestrate")
        menu_obj_1.add_command(label = "Policies", command = lambda: self.orchs_exe())
        win.config(menu = menu_obj_1)

    def radial_cre(self ,f, k):
        decision = IntVar()
        radial_list = []
        for i in range(1,k+1):
            radial_list.append(Radiobutton(f, text = "Files", activebackground = self.black, activeforeground = "green", bg = self.white, cursor = "target", value = i, variable = decision, command = lambda: self.decide(decision.get())))
        
        radial_list[0].pack(side = "top")
        radial_list[1].pack(side = "top")

    def decide(self,x):
        #Logic
        print(x)

    def orchs_exe(self):
        print("Go to Policy Frame")
        self.child_frame_del(self.design_frame_list)
        self.child_frame_del(self.frame_list)
        self.main_frame_del()
        EnforcePol().child_frame_pos()

class EnforcePol(Window,LIFace.WinFrame,LIFace.WinMenu,LIFace.WinTextBox,DIFace.ColorParameters):
    def __init__(self):
        super().__init__()
        super().set_res()

    class FirewallPolicy:
        def enable_ufw(self):
            try:
                subprocess.run(["sudo", "ufw", "enable"], check=True)
                print("UFW enabled.")
            except subprocess.CalledProcessError as e:
                print(f"Error enabling UFW: {e}")

        def allow_ssh(self):
            try:
                subprocess.run(["sudo", "ufw", "allow", "OpenSSH"], check=True)
                print("SSH access allowed.")
            except subprocess.CalledProcessError as e:
                print(f"Error allowing SSH: {e}")

        def allow_custom_ports(self,ports):
            for port in ports:
                try:
                    subprocess.run(["sudo", "ufw", "allow", str(port)], check=True)
                    print(f"Port {port} allowed.")
                except subprocess.CalledProcessError as e:
                    print(f"Error allowing port {port}: {e}")

    def color_loader(self):
        self.black ="#000000"
        self.white = "#FFFFFF"
        self.grey = "#808080"
        self.d_grey = "#008080"
        self.l_grey = "#CDCDCD"

    def child_frame_pos(self):
        self.color_loader()
        
        self.menu_cre()
        self.main_frame_gen(20)
        
        self.design_frame_list = self.child_frame_gen(1, 1, self.height, int(0.3*self.width), self.d_grey)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, self.height, int(0.7*self.width), self.white)
        self.frame_list[0].pack(side="left", expand = True, fill = BOTH)
        self.frame_list[0].pack_propagate(0)

        self.grid_frame_list = self.child_frame_gen(9, self.frame_list, 1, int(0.5*self.height), int(0.7*self.width), self.white)
        
        count = 0
        for r in range(0,3):
            for col in range(0,3):
                self.grid_frame_list[count].grid(row = r, column = col)
                self.grid_frame_list[count].propagate(0)
                count = count + 1
        
        
        print("Frame positioned")
        self.button_cre(self.grid_frame_list , "Policy", self.white)
        
        self.textbox_frame_list = self.child_frame_gen(1, self.frame_list, 1, int(0.5*self.height), int(0.7*self.width), self.black)
        self.textbox_frame_list[0].grid(row = 3, column = 0, columnspan = 3)
        self.textbox_frame_list[0].grid_propagate(0)

        self.textbox = self.textbox_cre(self.textbox_frame_list[0], 6,42)
        self.textbox_pos()

    def menu_cre(self):
        menu_obj_1 = Menu(win)
        menu_obj_1.add_command(label = "Orchestrate", command = lambda:self.back_orchs_exe())
        menu_obj_1.add_command(label = "Policies")
        win.config(menu = menu_obj_1)

    def textbox_pos(self):
        self.textbox.pack()

    def button_cre(self ,f ,t ,bcl):
        self.btn = []

        self.btn.append(Button(f[0], text=t ,bg=bcl ,command = lambda: self.secure_ssh(), padx = 31, pady = 34))
        self.btn.append(Button(f[1], text=t ,bg=bcl ,command = lambda: self.secure_ssh(), padx = 31, pady = 34))
        self.btn.append(Button(f[2], text=t ,bg=bcl ,command = lambda: self.secure_ssh(), padx = 31, pady = 34))
        self.btn.append(Button(f[3], text=t ,bg=bcl ,command = lambda: self.secure_ssh(), padx = 31, pady = 34))
        self.btn.append(Button(f[4], text=t ,bg=bcl ,command = lambda: self.secure_ssh(), padx = 31, pady = 34))
        self.btn.append(Button(f[5], text=t ,bg=bcl ,command = lambda: self.secure_ssh(), padx = 31, pady = 34))
        self.btn.append(Button(f[6], text=t ,bg=bcl ,command = lambda: self.secure_ssh(), padx = 31, pady = 34))
        self.btn.append(Button(f[7], text=t ,bg=bcl ,command = lambda: self.secure_ssh(), padx = 31, pady = 34))
        self.btn.append(Button(f[8], text=t ,bg=bcl ,command = lambda: self.secure_ssh(), padx = 31, pady = 34))

        for cursor in range(0,9):
            self.btn[cursor].grid(row = cursor//3, column = cursor%3, sticky = "nsew", pady = 15, padx = 5)


    def secure_ssh(self):
        pol = self.FirewallPolicy()

        print("Secure shell ssh")

        """
        # Enable UFW
        pol.enable_ufw()

        # Allow SSH
        pol.allow_ssh()

        # Define additional ports to allow (e.g., 80 for HTTP, 443 for HTTPS)
        custom_ports = [80, 443]

        # Allow custom ports
        pol.allow_custom_ports(custom_ports)
        """
    def back_orchs_exe(self):
            self.child_frame_del(self.design_frame_list)
            self.child_frame_del(self.grid_frame_list)
            self.child_frame_del(self.frame_list)
            self.main_frame_del()
            Orchestrate().child_frame_pos()


if __name__=="__main__":
    #Pop-Up Configuration
    Authorize().child_frame_pos()
    win.mainloop()




