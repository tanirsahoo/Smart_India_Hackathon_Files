# GUI-Documentation

## Classes:
1. Configure : keyword --> config_{module}
                           config_tk()
                           config_package(package_name)
2. SharedSpace : keyword --> set_{global variables}
                             set_height_width(height,width)
                             set_title(title)
3. ColorPalette : keyword --> get_{p|s}_color
                              get_p_color()
                              get_s_color()
4. Window : keyword --> set_{resolution}
                        set_res()
5. WinFrame : keyword --> {main|child}_frame_{gen|pos|del}
                           main_frame_gen()
                           child_frame_gen(int,int,int,int,str)
                           child_frame_gen(int,list,int,int,int,str)
                           child_frame_pos()
                           child_frame_del(obj_list)
                           main_frame_del()
6. WinButton : keyword --> button_{cre|del}
                           button_cre()
                           button_del(obj)
7. WinLabel : keyword --> label_{cre|pos|del}
                          label_pos()
                          label_del(obj)
8. WinEntry : keyword --> entry_{cre|pos|del}
                          entry_cre(frame, entry_count, font, hlb, hlt)
                          entry_pos()
                          entry_del()

9. Authorize : keyword --> auth_{execute script}
                           auth_exe()
                           child_frame_pos() ---> two types of frame-list
                           design_frame_list=[]
                           frame_list = []
10. Orchestrate : keyword --> orchs_{execute script}
                              orchs_exe()
11. EnforcePol : keyword --> enfrc_{execute scripts}
                             enfrc_exe()
                             grid_frame_list --> third type of frame-list
12. FireWallPol:  

