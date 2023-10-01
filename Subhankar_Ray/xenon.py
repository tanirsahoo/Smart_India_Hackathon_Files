import tkinter as tk
from tkinter import *
from tkinter import ttk
from abc import ABC , abstractmethod
import subprocess

win=tk.Tk()

class Preconfig:
    def auto_config_tk(self):
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



class ShareVar:
    def setHeightWidth(self,height,width):
        self.height=height
        self.width=width

class Window(ShareVar):
    def __init__(self):
        super().setHeightWidth(500,500)
        self.title="Xenon"

    def window_res(self):
        win.geometry("500x500")
        win.maxsize(self.width, self.height)
        win.minsize(self.width, self.height)
        win.title(self.title)
        win.configure(bg="#FFFFFF")


class Win_frames(ABC,ShareVar):
    def main_frame_gen(self):
        self.main_frame=Frame(win ,bg="#808080" ,borderwidth=1 ,relief=SUNKEN ,width=self.width ,height=self.height)
        self.main_frame.pack(fill = tk.BOTH, expand = True)
        self.main_frame.pack_propagate(0)
        self.main_frame.place(anchor = 'center', relx = 0.5, rely = 0.5)
        
    def child_frames_gen(self, k, bd, ht, wd, cl):
        flist=[]
        for i in range(1,k+1):
            flist.append(Frame(self.main_frame, bg=cl ,borderwidth=bd, relief=SUNKEN, width=wd, height=ht))
        return flist

    @abstractmethod
    def child_frames_pos(self):
        pass

    def child_frames_del(self,obj):
        obj.destroy()

class Win_buttons(ABC):
    @abstractmethod
    def button_create(self ,f ,t ,bcl):
        pass

    def button_del(self,obj):
        obj.destroy()

class Win_label(ABC):
    @abstractmethod
    def label_pos(self):
        pass

    def label_del(self,obj):
        obj.destroy()

class Win_entry(ABC):
    def entry_cre(self ,fr ,k, ft, hlb, hlt):
        elist=[]
        for i in (1,k+1):
            elist.append(Entry(fr, font = k, highlightbackground = hlb, highlightthickness = hlt))
        return elist

    @abstractmethod
    def entry_pos(self):
        pass

    def entry_del(self,obj):
        obj.destroy()



class AuthWindow(Window,Win_frames,Win_buttons,Win_entry):
    def __init__(self):
        super().__init__()
        super().window_res()
    

    def child_frames_pos(self):
        self.main_frame_gen()
        self.design_frames_list = self.child_frames_gen(2,1,int(0.2*self.height),self.width, "#008080")
        self.frames_list = self.child_frames_gen(1,1,300,self.width, "#FFFFFF")

        self.design_frames_list[0].pack(side="top", expand=False)
        self.design_frames_list[0].pack_propagate(0)
        
        self.frames_list[0].pack(side="top", expand=False)
        self.frames_list[0].pack_propagate(0)

        self.design_frames_list[1].pack(side="top", expand=False)
        self.design_frames_list[1].pack_propagate(0)
        print("Frame positioned")
        
        self.entry_pos()
        
        self.button_create(self.frames_list[0] ,"Sign In", "#FFFFFF")
        print("Button positioned")
    
    def entry_pos(self):
        self.entry_list = self.entry_cre(self.frames_list[0], 1, "Bitter", "#CDCDCD", 1)
        self.entry_list[0].pack()
        self.entry_list[0].place(anchor = 'center', relx = 0.5, rely = 0.3)
        print("Entry positioned")

    def button_create(self ,f ,t ,bcl):
        btn1 = Button(f ,text=t ,bg=bcl ,command = lambda: self.auth_script())
        btn1.pack()
        btn1.place(anchor = 'center', relx = 0.5, rely = 0.6)

    def auth_script(self):
        #Auth-Script
        print("Executing-Auth-Script")
        z = 1
        if z:
            print("Authenticated")
            self.child_frames_del(self.frames_list[0])
            ViewWindow().child_frames_pos()

class ViewWindow(Window,Win_frames):
    def __init__(self):
        super().__init__()
        super().window_res()

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

    def child_frames_pos(self):
        self.main_frame_gen()
        self.text_list = ["Password Chk", "Blocking SSH"]
        
        self.design_frames_list = self.child_frames_gen(1, 1, self.height, 0.3*self.width, "#008080")
        self.design_frames_list[0].pack(side="left")
        self.design_frames_list[0].pack_propagate(0)
        
        self.frames_list = self.child_frames_gen(1, 1, self.height, 0.7*self.width, "#FFFFFF")
        self.frames_list[0].pack(side="left")
        self.frames_list[0].pack_propagate(0)
        
        print("Frame positioned")
        #self.button_create(self.frames_list , self.text_list, "#FFFFFF")

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
    Preconfig().auto_config_tk()
    AuthWindow().child_frames_pos()
    win.mainloop()


