'''Optimization has done been done'''
'''Screen values are personalized'''
'''Rought draft as to the basic structure of pages'''

'''Dyuti - The previous window closing when new window opens
            will not allow reduce flexibility'''
'''Option to go back - include'''

'''To be integrated into xenon'''


import tkinter as tk
'''
def main_window(root):
#creating window    
    #getting screen width and height of display
    width_s= root.winfo_screenwidth() -80
    height_s= root.winfo_screenheight()-80
    root.resizable(0,0)
    #setting tkinter window size
    root.geometry("%dx%d" % (width_s, height_s))
    root.title("Hardening Script - GUI")
    '''
def page_2():
    root=tk.Tk()
    width_s= 1366
    height_s= 768
    frame1 = tk.LabelFrame(root, bg="#0000FF", height = 100, width= width_s) 
    lf_label = tk.Label(frame1, text="Available Users",fg='white',bg='blue',font=('Times New Roman',60))
    lf_label.place(relx=.5, rely=.5, anchor="c")
    frame1.grid(row=0, column=0)
    frame2 = tk.LabelFrame(root, bg="#FFFFFF", height = height_s-100, width= width_s)
    frame2.grid(row=1,column=0)
    '''
    error in design - for dynamic number of users - page not fixed
    '''

    '''
    drop down stuff?- data needs to becollected from sql
    '''
    texti = ["Dyutiprovo Sarkar","Soumyadeep Samanta","Tanir Sahooo","Subhankar Ray"]
    button1 = tk.Button(frame2, text=texti[0],bg='blue',fg='white',font = ('Times New Roman',20),width=25,command=lambda:[close(root),page_3(texti[0])])
    button1.grid(row=0,column=0,padx=(10,10),pady=10)
    button1 = tk.Button(frame2, text=texti[1],bg='blue',fg='white',font = ('Times New Roman',20),width=25,command=lambda:[close(root),page_3(texti[1])])
    button1.grid(row=0,column=1,padx=(0,630),pady=10)
    button1 = tk.Button(frame2, text=texti[2],bg='blue',fg='white',font = ('Times New Roman',20),width=25,command=lambda:[close(root),page_3(texti[2])])
    button1.grid(row=1,column=0,padx=10,pady=(0,800))
    button1 = tk.Button(frame2, text=texti[3],bg='blue',fg='white',font = ('Times New Roman',20),width=25,command=lambda:[close(root),page_3(texti[3])])
    button1.grid(row=1,column=1,padx=(0,630),pady=(0,800))
    
    root.mainloop()

def en_disen(i):
    '''data extracted'''
    lis = [True,True,False]
    return lis[i]
  
def page_3(textio):
    root=tk.Tk()
    width_s= 1366
    height_s= 768
    frame1 = tk.LabelFrame(root, bg="#0000FF", height = 100, width= width_s) 
    lf_label = tk.Label(frame1, text=textio,fg='white',bg='blue',font=('Times New Roman',60))
    lf_label.place(relx=.5, rely=.5, anchor="c")
    frame1.grid(row=0, column=0)
    frame2 = tk.LabelFrame(root, bg="#FFFFFF", height = height_s-100, width= width_s)
    frame2.grid(row=1,column=0)
    lf_label = tk.Label(frame2,bg='white', justify='left',text="1. TOR POLICY ",font=('Times New Roman',30))
    lf_label.grid(row=1,column=0, pady=(100,80),padx=(100,300))
    if en_disen(0) is True:
        texti='Disable'
    else:
        texti='Enable'
    '''stand-in for now'''
    button1 = tk.Button(frame2, text=texti,bg='blue',fg='white',font = ('Times New Roman',20),width=15)
    button1.grid(row=1,column=1, pady=(100,60),padx=(20,310))
    if en_disen(1) is True:
        texti='Disable'
    else:
        texti='Enable'
    lf_label = tk.Label(frame2,bg='white', justify='left',text="2. USB POLICY ",font=('Times New Roman',30))
    lf_label.grid(row=2,column=0, pady=(0,80),padx=(100,300))
    button2 = tk.Button(frame2, text=texti,bg='blue',fg='white',font = ('Times New Roman',20),width=15)
    button2.grid(row=2,column=1, pady=(0,80),padx=(20,310))
    if en_disen(2) is True:
        texti='Disable'
    else:
        texti='Enable'
    lf_label = tk.Label(frame2,bg='white', justify='left',text="3. FIREWALL POLICY ",font=('Times New Roman',30))
    lf_label.grid(row=3,column=0, pady=(0,200),padx=(100,300))
    button3 = tk.Button(frame2, text=texti,bg='blue',fg='white',font = ('Times New Roman',20),width=15)
    button3.grid(row=3,column=1, pady=(0,200),padx=(20,310))

    root.mainloop()

def close(root):
    root.destroy()

def page_1():
    root=tk.Tk()
    width_s= 1366
    height_s= 768
    frame1 = tk.LabelFrame(root, bg="#0000FF", height = 150, width= width_s) 
    lf_label = tk.Label(frame1, text="KAIZEN",fg='white',bg='blue',font=('Times New Roman',80))
    lf_label.place(relx=.5, rely=.5, anchor="c")
    frame1.grid(row=0, column=0)
    frame2 = tk.LabelFrame(root, bg="#FFFFFF", height = height_s-380, width= width_s)
    frame2.grid(row=1,column=0)
    lf_label = tk.Label(frame2, text="POLICIES",font=('Times New Roman',40))
    lf_label.grid(row=0,column=1, pady=(30,50),padx=(100,630))
    lf_label = tk.Label(frame2,bg='white', justify='left',text="1. TOR POLICY - ...",font=('Times New Roman',20))
    lf_label.grid(row=1,column=0, pady=(0,20))
    lf_label = tk.Label(frame2,bg='white', justify='left',text="2. USB POLICY - ...",font=('Times New Roman',20))
    lf_label.grid(row=2,column=0, pady=(0,20))
    lf_label = tk.Label(frame2,bg='white', justify='left',text="           3. FIREWALL POLICY - ...",font=('Times New Roman',20))
    lf_label.grid(row=3,column=0, pady=(0,100))
    frame3 = tk.LabelFrame(root, bg="#0000FF", height = 150, width= width_s)
    frame3.grid(row=2,column=0)
    button1 = tk.Button(frame3, text="Proceed",bg='blue',fg='white',font = ('Times New Roman',20),width=15,command=lambda:[close(root),page_2()])
    button1.pack(side=tk.LEFT, padx=(width_s//6, width_s//3+10),pady=(60,70))  # Add padding to the right of Button 1
    button2 = tk.Button(frame3, text="Scan",bg='blue',fg='white',font = ('Times New Roman',20),width=15)
    button2.pack(side=tk.RIGHT,padx=(0,width_s//6),pady=(60,70)) 

    root.mainloop()

if __name__ == "__main__":
    page_1()