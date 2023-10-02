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


class ColorPalette:
    def get_p_color(self):
        self.black = "#000000"
        self.white = "#FFFFFF"

    def get_s_color(self):
        self.design_color = "#008080"
        self.entry_color = "#CDCDCD"

class Window(SharedSpace):
    def __init__(self):
        super().set_height_width(500,500)
        super().set_title("Xenon")

    def set_res(self):
        win.geometry("500x500")
        win.maxsize(self.width, self.height)
        win.minsize(self.width, self.height)
        win.title(self.title)


class WinFrame(ABC,SharedSpace):
    def main_frame_gen(self):
        self.main_frame=Frame(win ,borderwidth=1 ,relief=SUNKEN ,width=self.width ,height=self.height)
        self.main_frame.pack(fill = BOTH, expand = True)
        self.main_frame.pack_propagate(0)
        self.main_frame.place(anchor = 'center', relx = 0.5, rely = 0.5)
    
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
    def entry_cre(self ,frame ,frame_count, font, hlb, hlt):
        entry_list=[]
        for i in range(1, frame_count+1):
            entry_list.append(Entry(frame, font = font, highlightbackground = hlb, highlightthickness = hlt))
        return entry_list

    @abstractmethod
    def entry_pos(self):
        pass

    def entry_del(self,obj):
        obj.destroy()

class WinRadial(ABC):
    @abstractmethod
    def radial_cre(self):
        pass

    def radial_del(self,obj_list):
        for obj in obj_list:
            obj.destroy()

class Authorize(Window,WinFrame,WinButton,WinEntry,ColorPalette):
    def __init__(self):
        super().__init__()
        super().set_res()
        super().get_p_color()
        super().get_s_color()
    

    def child_frame_pos(self):
        self.main_frame_gen()
        self.design_frame_list = self.child_frame_gen(2, 1, int(0.2*self.height), self.width,  self.design_color)
        self.frame_list = self.child_frame_gen(1, 1, int(0.6*self.height), self.width, self.white)

        self.design_frame_list[0].pack(side="top", expand=False)
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list[0].pack(side="top", expand=False)
        self.frame_list[0].pack_propagate(0)

        self.design_frame_list[1].pack(side="top", expand=False)
        self.design_frame_list[1].pack_propagate(0)
        print("Frame positioned")
        
        self.entry_pos()
        
        self.button_cre(self.frame_list[0] ,"Login", self.white)
        print("Button positioned")
    
    def entry_pos(self):
        self.entry_list = self.entry_cre(self.frame_list[0], 3, "Bitter", self.entry_color, 1)
        
        self.entry_list[0].insert(0,"Username")
        self.entry_list[0].pack()
        self.entry_list[0].place(anchor = 'center', relx = 0.5, rely = 0.2)
        
        self.entry_list[1].insert(0,"Role")
        self.entry_list[1].pack()
        self.entry_list[1].place(anchor = 'center', relx = 0.5, rely = 0.4)

        self.entry_list[2].insert(0,"Password")
        self.entry_list[2].pack()
        self.entry_list[2].place(anchor = 'center', relx = 0.5, rely = 0.6)

        print("Entry positioned")

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

class Orchestrate(Window,WinFrame, ColorPalette):
    def __init__(self):
        super().__init__()
        super().set_res()
        super().get_p_color()
        super().get_s_color()

    def child_frame_pos(self):
        self.main_frame_gen()

        self.design_frame_list = self.child_frame_gen(1, 1, self.height, int(0.3*self.width), self.design_color)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, self.height, int(0.7*self.width), self.white)
        self.frame_list[0].pack(side="left")
        self.frame_list[0].pack_propagate(0)
        
        print("Frame positioned")
        self.button_cre(self.frame_list , "Policies", self.white)

    def button_cre(self ,f ,t ,bcl):
        btn1 = Button(f[0] ,text=t ,bg=bcl ,command = lambda: self.orchs_exe())
        btn1.pack(side = "bottom")

    #def radial_cre(self ,f):


    def orchs_exe(self):
        print("Go to Policy Frame")
        z=1
        if z:

            self.child_frame_del(self.design_frame_list)
            self.child_frame_del(self.frame_list)
            self.main_frame_del()
            EnforcePol().child_frame_pos()

class EnforcePol(Window,WinFrame, ColorPalette):
    def __init__(self):
        super().__init__()
        super().set_res()
        super().get_p_color()
        super().get_s_color()

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

    def child_frame_pos(self):
        self.main_frame_gen()
        
        self.design_frame_list = self.child_frame_gen(1, 1, self.height, int(0.3*self.width), self.design_color)
        self.design_frame_list[0].pack(side="left")
        self.design_frame_list[0].pack_propagate(0)
        
        self.frame_list = self.child_frame_gen(1, 1, self.height, int(0.7*self.width), self.white)
        self.frame_list[0].pack(side="left", expand = True, fill = BOTH)
        self.frame_list[0].pack_propagate(0)

        self.grid_frame_list = self.child_frame_gen(9, self.frame_list, 1, self.height, int(0.7*self.width), self.white)
        
        count = 0
        for r in range(0,3):
            for col in range(0,3):
                self.grid_frame_list[count].grid(row = r, column = col)
                count = count + 1
        
        
        print("Frame positioned")
        self.button_cre(self.grid_frame_list , "Policy", self.white)

    def button_cre(self ,f ,t ,bcl):
        self.btn = []

        self.btn.append(Button(f[0], text=t ,bg=bcl ,command = lambda: self.secure_ssh() ,padx = 31 ,pady = 40))
        self.btn.append(Button(f[1], text=t ,bg=bcl ,command = lambda: self.secure_ssh() ,padx = 31 ,pady = 40))
        self.btn.append(Button(f[2], text=t ,bg=bcl ,command = lambda: self.secure_ssh() ,padx = 31 ,pady = 40))
        self.btn.append(Button(f[3], text=t ,bg=bcl ,command = lambda: self.secure_ssh() ,padx = 31 ,pady = 40))
        self.btn.append(Button(f[4], text=t ,bg=bcl ,command = lambda: self.secure_ssh() ,padx = 31 ,pady = 40))
        self.btn.append(Button(f[5], text=t ,bg=bcl ,command = lambda: self.secure_ssh() ,padx = 31 ,pady = 40))
        self.btn.append(Button(f[6], text=t ,bg=bcl ,command = lambda: self.secure_ssh() ,padx = 31 ,pady = 40))
        self.btn.append(Button(f[7], text=t ,bg=bcl ,command = lambda: self.secure_ssh() ,padx = 31 ,pady = 40))
        self.btn.append(Button(f[8], text=t ,bg=bcl ,command = lambda: self.secure_ssh() ,padx = 31 ,pady = 40))

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


if __name__=="__main__":
    #Pop-Up Configuration
    Authorize().child_frame_pos()
    win.mainloop()




