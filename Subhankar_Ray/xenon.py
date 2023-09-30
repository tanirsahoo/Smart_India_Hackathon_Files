from tkinter import *
from tkinter import ttk
from abc import ABC , abstractmethod
import subprocess

win=Tk()

class Preconfig:
    def auto_config_tk(self):
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
        pol = self.FirewallPolicy()

        print("Secure shell ssh")
        # Enable UFW
        pol.enable_ufw()

        # Allow SSH
        pol.allow_ssh()

        # Define additional ports to allow (e.g., 80 for HTTP, 443 for HTTPS)
        custom_ports = [80, 443]

        # Allow custom ports
        pol.allow_custom_ports(custom_ports)


if __name__=="__main__":
    #Pop-Up Configuration
    Preconfig().auto_config_tk()
    AuthWindow().frames_pos()
    win.mainloop()


