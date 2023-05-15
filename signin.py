import sys
sys.path.append("C:/users/abinaya/appdata/roaming/python/python311/site-packages")
from tkinter import *
from PIL import ImageTk,Image
import webbrowser
from tkinter import messagebox
import pymysql
#Functionality part

def forgat_pass():
    def change_password():
        if user_entry.get()=="" or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror("Error","All fields are Required",parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror("Error","Password and Confirm Password Are Not Matching")
        else:           
            con=pymysql.connect(host="localhost",user="root",password="",database="userdata")
            mycursor=con.cursor()
            query="select * from data where username=%s"
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Incorrect Username",parent=window)
            else:
                query="update data set password=%s where username=%s"
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Password is Reseted, Please login with new password",parent=window)
                window.destroy()

    window=Toplevel()
    window.title("Change Password")
    bgpic=ImageTk.PhotoImage(file="D:\Tkinter\mount.jpeg")
    bglabel=Label(window,image=bgpic)
    bglabel.grid()
# Heading Block of Forgot Password
    heading_label=Label(window,text="RESET PASSWORD",font=("arial","18","bold"),bg="skyblue",fg="magenta2")
    heading_label.place(x=480,y=60)
#Username Block
    userlabel=Label(window,text="Username",font=("arial","12","bold"),bg="skyblue",fg="magenta2")
    userlabel.place(x=470,y=130)

    user_entry=Entry(window,width=31,fg="magenta2",font=("arial","11","bold"),bd=0)
    user_entry.place(x=470,y=160)

    #Frame(window,width=250,height=2,bg="orchid1").place(x=470,y=180)
#NewPassword Block
    passwordlabel=Label(window,text="Password",font=("arial","12","bold"),bg="skyblue",fg="magenta2")
    passwordlabel.place(x=470,y=210)

    newpass_entry=Entry(window,width=31,fg="magenta2",font=("arial","11","bold"),bd=0)
    newpass_entry.place(x=470,y=240)

    #Frame(window,width=250,height=2,bg="orchid1").place(x=470,y=260)
#ConfirmPassword Block
    confirmpasslabel=Label(window,text="Confirm Password",font=("arial","12","bold"),bg="skyblue",fg="magenta2")
    confirmpasslabel.place(x=470,y=290)

    confirmpass_entry=Entry(window,width=31,fg="magenta2",font=("arial","11","bold"),bd=0)
    confirmpass_entry.place(x=470,y=320)

    #Frame(window,width=250,height=2,bg="orchid1").place(x=470,y=340)
#Submit Button
    submitButton=Button(window,text="SUBMIT",bd=0,bg="skyblue",fg="white",font=("open sans","16","bold"),width=19,cursor="hand2",activebackground="magenta2",activeforeground="white",command=change_password)
    submitButton.place(x=470,y=390)



    window.mainloop()
def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror("Error","All Fileds Are Required")
    else:
        try:
            con=pymysql.connect(host="localhost",user="root",password="")
            mycursor=con.cursor()
        except:
            messagebox.showerror("Error","Connection is Not Established Try Again")
            return
        query="use userdata"
        mycursor.execute(query)
        query="select * from data where username=%s and password=%s"
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid username or Password")
        else:
            messagebox.showinfo("Success","Login is Successful")       

def open_twitter():
    webbrowser.open("https://twitter.com/AgroEr?t=y9lCY8KWTk-WPfnH3Z-aFA&s=08")
def open_facebook():
    webbrowser.open("https://www.facebook.com/abimani.abimanipolagam")
def open_google():
    webbrowser.open("https://www.linkedin.com/in/abirami-m-l-47170a17a")
def user_enter(event):
    if usernameEntry.get()=="Username":
        usernameEntry.delete(0,END)
def password_enter(event):
    if passwordEntry.get()=="Password":
        passwordEntry.delete(0,END)
def hide():
    openeye.config(file="closeye.png")
    passwordEntry.config(show="*")
    eyeButton.config(command=show) 
def show():
    openeye.config(file="openeye.png")
    passwordEntry.config(show="")  
    eyeButton.config(command=hide)
def signup_page():
    login_window.destroy()
    import signup

# GUI part
login_window=Tk()
login_window.geometry("1027x686+50+50")
login_window.resizable(0,0)
login_window.title("Sign Up")
bg=ImageTk.PhotoImage(file="D:\Tkinter\greentree.jpg")
bglabel=Label(login_window,image=bg)
bglabel.grid(row=0,column=0)
heading=Label(login_window,text="USER LOGIN",font=('Microsoft Yahei UI Light',23,"bold"),fg='green',bg="white")
heading.place(x=605,y=120)
#For username tab
usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',12,'bold'),border=0,fg="magenta4")
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,"Username")
usernameEntry.bind('<FocusIn>',user_enter)
#Frame(login_window,width=250,height=7,bg="firebrick1").place(x=580,y=200) # for underline
# for password 
passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',13,'bold'),border=1,fg="magenta4")
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,"Password")
passwordEntry.bind('<FocusIn>',password_enter)
#Frame(login_window,width=250,height=10,bg="white").place(x=580,y=280)
# eye button block
openeye=PhotoImage(file="D:\python tkinter prjct\static\openeye.png")
eyeButton=Button(login_window,image=openeye,bd=0,bg="white",activebackground="white",cursor="hand2",command=hide)
eyeButton.place(x=800,y=260)
# forget button block
forgetButton=Button(login_window,text="Forgot Password?",bd=0,bg="white",activebackground="white",cursor="hand2",font=('Microsoft Yahei UI Light',12,'bold'),fg="red",command=forgat_pass)
forgetButton.place(x=675,y=295)
# Login button
LoginButton=Button(login_window,text="Login",font=("opens sans",16,"bold"),fg="white",bg="light green",cursor="hand2",bd=0,width=19,command=login_user).place(x=578,y=350)
# OR Label
orLabel=Label(login_window,text="----------------OR---------------",font=("open sans",16),fg="black",bg="white").place(x=578,y=400)
# Facebook logo
facebook_logo=PhotoImage(file="D:\python tkinter prjct\static\\facebook.png")
fbLabel=Label(login_window,image=facebook_logo,fg="black",bg="white")
fbLabel.place(x=640,y=440)
fbLabel.bind("<Button-1>",lambda e: open_facebook())
# Google logo
google_logo=PhotoImage(file="D:\python tkinter prjct\static\google.png")
gglLabel=Label(login_window,image=google_logo,fg="black",bg="white")
gglLabel.place(x=690,y=440)
gglLabel.bind("<Button-1>", lambda e: open_google() )
# Twitter logo
twitter_logo=PhotoImage(file="D:\python tkinter prjct\static\\twitter.png")
twtrLabel=Label(login_window,image=twitter_logo,fg="black",bg="white")
twtrLabel.place(x=740,y=440)
twtrLabel.bind("<Button-1>",lambda event: open_twitter())
# Dont have an account
signupLabel=Label(login_window,text="Don't have an account?",font=("open sans",9,"bold"),fg="black",bg="white").place(x=590,y=500)
newaccountButton=Button(login_window,text="Create new one",font=("opens sans",9,"bold underline"),fg="blue",bg="white",activebackground="white",activeforeground="blue",cursor="hand2",bd=0,command=signup_page).place(x=727,y=500)
login_window.mainloop() 
