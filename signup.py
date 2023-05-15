import sys
sys.path.append("C:/users/abinaya/appdata/roaming/python/python311/site-packages")

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import re


def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def Login_page():
    signup_window.destroy()
    import signin
def connect_database():
    username=usernameEntry.get()
    email=emailEntry.get()
    password=passwordEntry.get()
    confirmpassword=confirmEntry.get()

    if not username:
        messagebox.showerror("Error", "Please enter a username.")
    elif not email:
        messagebox.showerror("Error", "Please enter an email.")
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Please enter a valid email address.")
    elif not password:
        messagebox.showerror("Error", "Please enter a password.")
    elif not confirmpassword:
        messagebox.showerror("Error", "Please confirm the password.")
    elif password != confirmpassword:
        messagebox.showerror("Error", "Passwords do not match.")
    elif check.get()==0:
        messagebox.showerror("Error","Please accept Terms and Conditions")
    

    else:
        try:
            con=pymysql.connect(host="localhost",user="root",password="")
            mycursor=con.cursor()
        except:
            messagebox.showerror("Error","Database Connectivity Issue, Please Try Again")
            return
        try:
            query="Create database Userdata"
            mycursor.execute(query)
            query="use userdata"
            mycursor.execute(query)
            query="create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))"
            mycursor.execute(query)
        except:
            mycursor.execute("use userdata")

        query="select * from data where username=%s"
        mycursor.execute(query,(usernameEntry.get()))
        row=mycursor.fetchone()
        if row!= None:
            messagebox.showerror("Error","Username already exists")
        query="select * from data where password=%s"
        mycursor.execute(query,(passwordEntry.get()))
        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror("Error","Password already exists")
        query="select * from data where email=%s"
        mycursor.execute(query,(emailEntry.get()))
        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror("Error","Email already exists")

        else:

            query="insert into data(email,username,password) values(%s,%s,%s)"
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("success","Registration is succesccful")

            clear()
            signup_window.destroy()
            import signin 



signup_window=Tk()
signup_window.title("Signup Page")
signup_window.resizable
#background image
background=ImageTk.PhotoImage(file="D:\python tkinter prjct\static\greentree.jpg")
bgLabel=Label(signup_window,image=background)
bgLabel.grid()
frame=Frame(signup_window,bg="white")
frame.place(x=654,y=190)
#heading block
heading=Label(frame,text="START JOURNEY WITH US",font=('Microsoft Yahei UI Light',18,"bold"),bg='white',fg='dark green')
heading.grid(row=0,column=0,padx=8,pady=10)
#Email block
emailLabel=Label(frame,text="Email",font=('Microsoft Yahei UI Light',10,"bold"),bg="white",fg="dark green")
emailLabel.grid(row=1,column=0,sticky="w",padx=25,pady=(10,0))
emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,"bold"),fg="black",bg="SeaGreen1")
emailEntry.grid(row=2,column=0,sticky="w",padx=25)
# Username block
usernameLabel=Label(frame,text="Username",font=('Microsoft Yahei UI Light',10,"bold"),bg="white",fg="dark green")
usernameLabel.grid(row=3,column=0,sticky="w",padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,"bold"),fg="black",bg="SeaGreen1")
usernameEntry.grid(row=4,column=0,sticky="w",padx=25)
#Password block
passwordLabel=Label(frame,text="Password",font=('Microsoft Yahei UI Light',10,"bold"),bg="white",fg="dark green")
passwordLabel.grid(row=5,column=0,sticky="w",padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,"bold"),fg="black",bg="SeaGreen1")
passwordEntry.grid(row=6,column=0,sticky="w",padx=25)
#confirm password block
confirmLabel=Label(frame,text="Confirm Password",font=('Microsoft Yahei UI Light',10,"bold"),bg="white",fg="dark green")
confirmLabel.grid(row=7,column=0,sticky="w",padx=25,pady=(10,0))
confirmEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,"bold"),fg="black",bg="SeaGreen1")
confirmEntry.grid(row=8,column=0,sticky="w",padx=25)
# checkbutton in built class in tkinter
check=IntVar()
termsandconditions=Checkbutton(frame,text="I agree to the Terms & Conditions",font=('Microsoft Yahei UI Light',10,"bold"),fg="dark green",bg="white",activebackground="white",activeforeground="dark green",cursor="hand2",variable=check)
termsandconditions.grid(row=9,column=0,pady=10,padx=15)
# signup button
signupButton=Button(frame,text="JOIN",font=("opens sans",16,"bold"),bd=0,bg="dark green",activebackground="dark green",fg="white",activeforeground="white",command=connect_database)
signupButton.grid(row=10,column=0,pady=10)
# already have an account
alreadyaccount=Label(frame,text="Already have an account?",font=("open sans","9","bold"),bg="white",fg="dark green")
alreadyaccount.grid(row=11,column=0,sticky="w",padx=25,pady=10)
#Login button
LoginButton=Button(frame,text="Log in",font=("open sans","9","bold underline"),bg="dark green",fg="white",bd=0,cursor="hand2",activebackground="dark green",activeforeground='white',command=Login_page)
LoginButton.place(x=180,y=406)
