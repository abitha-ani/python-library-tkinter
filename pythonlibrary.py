#tkinter
'''It is the standard graphical user interphase  (gui) library in python.It provides a simple way to create desktop applications
with graphical elements like windows buttons,labels ,textboxes and more.tkinter comes preinstalled python so you dont need to 
install it separately'''
#to develop desktop application,gui

#1)import tkinter library
#2) create windows
#3)add widgets like labels,buttons, to the windows
#4) call the main event loop so that the actions can takeplace on the users computer screen

# from tkinter import *
# from tkinter import messagebox
# window=Tk()
# #where to add widges after this object creation
# window.title("FIRST") #CREATE title for window
# window.geometry("500x500") #set the size of the window 500 wide 500 hight

# #now add widges
# #creating label
# #GEOMETRY METHOD POSITION TO PLACE,GRID,PACK
# #Grid row,column
# lb1=Label(window,text="FIRST NAME",font=("Arial",16,"bold"),fg="white",bg="blue",padx=20,pady=10,borderwidth=5,relief="ridge") #styling
# lb1.grid(row=0,column=0)
# # entry  box
# en1=Entry(window,bg="lightgrey",width=25,borderwidth=3,relief="sunken")
# en1.grid(row=0,column=1)
# #relife="sunken,ridge,flat,solid,raised,groove"
# lb2=Label(window,text="LAST NAME",font=("Arial",16,"bold"),fg="white",bg="blue",padx=20,pady=10,borderwidth=5,relief="ridge")
# lb2.grid(row=1,column=0)
# en2=Entry(window)
# en2.grid(row=1,column=1)

# def hello():
#     # print("okk...")
#     # lb2.configure(text="clicked")
#     # messagebox.showinfo("info","login successfull")
#     # messagebox.showerror("error","login failed")
#     messagebox.showwarning("warning","login cancelled")


# #creating button
# btn1=Button(window,text="click me",font=("Arial",16,"bold"),fg="white",bg="blue",padx=20,pady=10,borderwidth=5,
#  relief="raised",activebackground="lightblue",activeforeground="red",cursor="hand2",command=hello)
# btn1.grid(row=2,column=1)

# window.mainloop()



#command-in tkinter the command option in a button widget is used to specify a function that will be executed when the button is clicked


#################################################################################################################################################

# from tkinter import *
# from tkinter import messagebox
# window=Tk()
# window.title("SECOND") 
# window.geometry("500x500")
# def  confirm():
#     response=messagebox.askyesno("Exit","are ypu sure want to exit")
#     print(response)
#     if response:
#         window.destroy()
# btn1=Button(window,text="Exit",command=confirm)
# btn1.grid(row=0,column=0)

# def ask():
#     response=messagebox.askquestion("confirm","do you like tkinter?")
#     print(response)
#     if response=="yes":
#         messagebox.showinfo("response","great!")
#     else:
#         messagebox.showinfo("response","oh no")


# btn2=Button(window,text='ASK QUESTION',command=ask)
# btn2.grid(row=0,column=1)
# window.mainloop()

#######################################################################################################################
# username 
# pwd page login page


# from tkinter import *
# from tkinter import messagebox
# window=Tk()
# window.title("login page") 
# window.geometry("500x500") 

# lb1=Label(window,text="Username",font=("Arial",16,"bold"),fg="white",bg="green",padx=20,pady=10,borderwidth=5,relief="solid") #styling
# lb1.grid(row=0,column=0)

# en1=Entry(window,bg="lightgrey",width=25,borderwidth=3,relief="sunken")
# en1.grid(row=0,column=1)

# lb2=Label(window,text="Password",font=("Arial",16,"bold"),fg="white",bg="green",padx=20,pady=10,borderwidth=5,relief="solid")
# lb2.grid(row=1,column=0)
# en2=Entry(window,bg="lightgrey",width=25,borderwidth=3,relief="sunken")
# en2.grid(row=1,column=1)

# def hello():
#     messagebox.showinfo("info","login successfull")
#     # messagebox.showerror("error","login failed")
#     # messagebox.showwarning("warning","login cancelled")

# btn1=Button(window,text="Login",font=("Arial",16,"bold"),fg="white",bg="red",padx=20,pady=10,borderwidth=5,
#  relief="raised",activebackground="orange",activeforeground="red",cursor="hand2",command=hello)
# btn1.grid(row=2,column=1)

# window.mainloop()

###########################################################################################################################

# from tkinter import *
# from tkinter.scrolledtext import ScrolledText
# from tkinter.ttk import Combobox,Progressbar
# window=Tk()
# window.title("THIRD")
# window.geometry("500x500")

# lb1=Label(window,text="Gender")
# lb1.grid(row=0,column=0)

# # first=IntVar()
# first=StringVar(value=None)
# def show():
#     lb2.config(text=f"selected:{first.get()}")

# rb1=Radiobutton(window,text="Male",variable=first,value="male",command=show)
# rb1.grid(row=0,column=1)

# rb2=Radiobutton(window,text="Female",variable=first,value="female",command=show)
# rb2.grid(row=0,column=2)

# lb2=Label(window,text="Selected:None")
# lb2.grid(row=1,column=0)

# # creating checkbox
# lb2=Label(window,text='Language')
# lb2.grid(row=1,column=0)

# chb1=Checkbutton(window,text='English')
# chb1.grid(row=1,column=1)

# chb2=Checkbutton(window,text='Malayalam')
# chb2.grid(row=1,column=2)

# chb2=Checkbutton(window,text='Hindi')
# chb2.grid(row=1,column=3)

# lb3=Label(window,text="Age")
# lb3.grid(row=2,column=0)
# def get_value():
#     lb4.config(text=f"Selected:{sp.get()}")
# s=IntVar()
# s.set(25)

# sp=Spinbox(window,from_=1,to=50,width=25,textvariable=s)
# sp.grid(row=2,column=1)
# btn1=Button(window,text='GET VALUE',command=get_value)
# btn1.grid(row=3,column=1)
# lb4=Label(window,text="selected:None")
# lb4.grid(row=4,column=0)

# lb3=Label(window,text='address')
# lb3.grid(row=0,column=0)

# sc=ScrolledText(window,width=40,height=10)
# sc.grid(row=0,column=1)

# def click():
#     lb4.config(text=f"selected:{cm.get()}")


# cm=Combobox(window,values=["abc","def","ghi"])
# # cm['values']=("abc","cdf","ghi")
# cm.current(1)
# cm.grid(row=1,column=0)

# btn=Button(window,text='click',command=click)
# btn.grid(row=2,column=0)
 
# lb4=Label(window,text='selected:None')
# lb4.grid(row=3,column=0)

# #indeterminate progressbar
# def start_progress():
#     pr.start()

# def stop_progress():
#     pr.stop()


# pr=Progressbar(window,mode='indeterminate',length=200)
# pr.grid(row=4,column=0)

# start1=Button(window,text='start',command=start_progress)
# start1.grid(row=5,column=0)

# stop1=Button(window,text='stop',command=stop_progress)
# stop1.grid(row=5,column=1)

# ## determinate
# def update_progress():
#     current=pr1["value"]
#     if current<100:
#         pr1["value"]+=10
#         window.after(500,update_progress)


# pr1=Progressbar(window,mode='determinate',length=200)
# pr1.grid(row=4,column=0)
# pr1['maximum']=100
# startbtn=Button(window,text='start',command=update_progress)
# startbtn.grid(row=5,column=1)

# ###list
# lst1=Listbox(window)
# lst1.insert(1,"india")
# lst1.insert(2,"japan")
# lst1.insert(1,"usa")
# lst1.grid(row=6,column=0)

# ###menubar create sub menus

# menu1=Menu(window)
# filemenu=Menu(menu1)
# menu1.add_cascade(label='File',menu=filemenu)
# filemenu.add_command(label='New Text File')
# filemenu.add_command(label='New File')
# filemenu.add_command(label='New Folder')
# filemenu.add_separator()
# filemenu.add_command(label='Open Folder')
# filemenu.add_command(label='Open File')
# filemenu.add_command(label='Exit',command=window.quit)

# editmenu=Menu(menu1,tearoff=False)
# menu1.add_cascade(label='Edit',menu=editmenu)
# editmenu.add_command(label='Undo')
# editmenu.add_command(label='Redo')

# window.configure(menu=menu1,)


# window.mainloop()

#######################################################################################################################
# Registration page


# from tkinter import *
# from tkinter import messagebox
# from tkinter.scrolledtext import ScrolledText
# from tkinter.ttk import Combobox
# window=Tk()
# window.title("Register") 
# window.geometry("500x500")


# lb=Label(window,text="Name",font=("Arial",10,"bold"),fg="white",bg="green",padx=10,pady=10,borderwidth=2,relief="solid") #styling
# lb.grid(row=0,column=0)
# en=Entry(window,bg="lightgrey",width=25,borderwidth=3,relief="sunken")
# en.grid(row=0,column=1)


# lb1=Label(window,text="Username",font=("Arial",10,"bold"),fg="white",bg="green",padx=10,pady=10,borderwidth=2,relief="solid") #styling
# lb1.grid(row=1,column=0)
# en1=Entry(window,bg="lightgrey",width=25,borderwidth=3,relief="sunken")
# en1.grid(row=1,column=1)


# lb2=Label(window,text="Password",font=("Arial",10,"bold"),fg="white",bg="green",padx=10,pady=10,borderwidth=2,relief="solid")
# lb2.grid(row=2,column=0)
# en2=Entry(window,bg="lightgrey",width=25,borderwidth=3,relief="sunken")
# en2.grid(row=2,column=1)

# lb3=Label(window,text="Age",font=("Arial",10,"bold"),fg="white",bg="green",padx=10,pady=10,borderwidth=2,relief="solid")
# lb3.grid(row=3,column=0)
# sp=Spinbox(window,from_=1,to=50,width=25)
# sp.grid(row=3,column=1)

# lb4=Label(window,text="Email",font=("Arial",10,"bold"),fg="white",bg="green",padx=10,pady=10,borderwidth=2,relief="solid")
# lb4.grid(row=4,column=0)
# en3=Entry(window,bg="lightgrey",width=25,borderwidth=3,relief="sunken")
# en3.grid(row=4,column=1)

# lb5=Label(window,text="Phone number",font=("Arial",10,"bold"),fg="white",bg="green",padx=10,pady=10,borderwidth=2,relief="solid")
# lb5.grid(row=4,column=0)
# en4=Entry(window,bg="lightgrey",width=25,borderwidth=3,relief="sunken")
# en4.grid(row=4,column=1)

# lb6=Label(window,text='Address',font=("Arial",10,"bold"),fg="white",bg="green",padx=10,pady=10,borderwidth=2,relief="solid")
# lb6.grid(row=5,column=0)
# sc=ScrolledText(window,width=40,height=5,bg="lightgrey",borderwidth=3,relief="sunken")
# sc.grid(row=5,column=1)

# lb7=Label(window,text="Gender",font=("Arial",10,"bold"),fg="white",bg="green",padx=10,pady=10,borderwidth=2,relief="solid")
# lb7.grid(row=6,column=0)
# first=StringVar(value=None)
# rb1=Radiobutton(window,text="Male",variable=first,value="male",bg="lightgrey",width=25,borderwidth=3,relief="sunken")
# rb1.grid(row=6,column=1)
# rb2=Radiobutton(window,text="Female",variable=first,value="female",bg="lightgrey",width=25,borderwidth=3,relief="sunken")
# rb2.grid(row=6,column=2)


# lb8=Label(window,text='Languages',font=("Arial",10,"bold"),fg="white",bg="green",padx=10,pady=10,borderwidth=2,relief="solid")
# lb8.grid(row=7,column=0)
# chb1=Checkbutton(window,text='English',bg="lightgrey",borderwidth=3,relief="sunken")
# chb1.grid(row=7,column=1)
# chb2=Checkbutton(window,text='Malayalam',bg="lightgrey",borderwidth=3,relief="sunken")
# chb2.grid(row=7,column=2)
# chb2=Checkbutton(window,text='Hindi',bg="lightgrey",borderwidth=3,relief="sunken")
# chb2.grid(row=7,column=3)

# lb9=Label(window,text='College',font=("Arial",10,"bold"),fg="white",bg="green",padx=10,pady=10,borderwidth=2,relief="solid")
# lb9.grid(row=8,column=0)
# cm=Combobox(window,values=["GHSS","BVHSS","SMHSS"])
# cm.current(1)
# cm.grid(row=8,column=1)


# def hello():
#     messagebox.showinfo("info","login successfull")
#     # messagebox.showerror("error","login failed")
#     # messagebox.showwarning("warning","login cancelled")

# btn1=Button(window,text="Register",font=("Arial",10,"bold"),fg="white",bg="red",padx=10,pady=10,borderwidth=2,
#  relief="raised",activebackground="orange",activeforeground="red",cursor="hand2",command=hello)
# btn1.grid(row=9,column=1)

# window.mainloop()