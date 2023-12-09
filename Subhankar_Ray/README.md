# GUI-Documentation

## Classes:
1. Configure : keyword --> config_{module}
```
                           config_tk()
                           config_package(package_name)
```
2. SharedSpace : keyword --> set_{global variables}
```
                             set_height_width(height,width)
                             set_title(title)
```
4. ColorPalette : keyword --> get_{p|s}_color
```
                              get_p_color()
                              get_s_color()
```
6. Window : keyword --> set_{resolution}
```
                        set_res()
```
8. WinFrame : keyword --> {main|child}_frame_{gen|pos|del}
```
                           main_frame_gen()
                           child_frame_gen(int,int,int,int,str)
                           child_frame_gen(int,list,int,int,int,str)
                           child_frame_pos()
                           child_frame_del(obj_list)
                           main_frame_del()
```
10. WinButton : keyword --> button_{cre|del}
```
                           button_cre()
                           button_del(obj)
```
11. WinLabel : keyword --> label_{cre|pos|del}
```
                          label_pos()
                          label_del(obj)
```
12. WinEntry : keyword --> entry_{cre|pos|del}
```
                          entry_cre(frame, entry_count, font, hlb, hlt)
                          entry_pos()
                          entry_del()
```
13. Authorize : keyword --> auth_{execute script}
```
                           auth_exe()
                           child_frame_pos() ---> two types of frame-list
                           design_frame_list=[]
                           frame_list = []
```
14. Orchestrate : keyword --> orchs_{execute script}
```
                              orchs_exe()
```
15. EnforcePol : keyword --> enfrc_{execute scripts}
```
                             enfrc_exe()
                             grid_frame_list --> third type of frame-list
```
16. FireWallPol:  

# Remote-Desktop-Connection:(Using ThinLinc)

1. Download ThinLinc(Administrative Version) from the official website
```
		https://www.cendio.com/thinlinc/download/
```

2. Extract file & Open Terminal within that file itself.
3. Run through all the steps & (choose: Master) then once it is finished
4. Type these commands
```
		sudo systemctl status vsmserver
```
```
		sudo systemctl status vsmagent
```
```
		ifconfig
```
5. Then check the static ip given there (search for the keyword: inet)
6. Then using the given static ip, open a browser(like Chrome,Edge,etc)
```
		static_ip:300
```
7. Then once connected, it will ask for the username(Ubuntu system user name) and a paswword which has to be given by you
8. Once it is authenticated, the Remote-Desktop-Connection is established.
9. You will be logged out of the existing session and then you will get to see the GUI in your browser, provided you are in the same local network.


There is a way out of distrbuting work using this Remote-Desktop-Protocol by actually creating a set of sudo users.(Experimental).

# Issues to solve
1. Creation of nested groupings to form specified organizational structures
2. Creation of new user without opening the terminals for password information and all
3. usb for the ubuntu system itself
