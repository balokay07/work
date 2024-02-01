from tkinter import *
from tkinter import messagebox


def Ok():
    uname = t1.get()
    password = t2.get()
     
    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")

    elif(uname == "Admin" and password == "123"):
        messagebox.showinfo("","Login Success")

    else :
        messagebox.showinfo("", "incorrent useername and password")    


root = Tk()
root.title("login")
root.geometry("300x200")
global t1
global t2
Label(root, text="UserName"). place(x=10, y=10)
Label(root, text="password"). place(x=10, y=40)

t1 = Entry(root)
t1.place(x=140, y=10)

t2 = Entry(root)
t2.place(x=140, y=40)
t2.config(show="*")

Button(root, text="Login", command=Ok ,height =3, width = 13).place(x=10, y=100)






root.mainloop()
            