from tkinter import *
from tkinter import messagebox

import pymysql

def clear():
	emailEntry.delete(0,END)
	UsernameEntry.delete(0,END)
	PasswordEntry.delete(0,END)
	confirmpasswordEntry.delete(0,END)
	check.set(0)


def connect_database():
	if emailEntry.get()=='' or UsernameEntry.get()=='' or PasswordEntry.get()==''or confirmpasswordEntry.get()=='':
		messagebox.showerror('Error','All Fields Are Required')
	elif PasswordEntry.get() != confirmpasswordEntry.get():
		messagebox.showerror('Error','Passwor Mismatch')
	elif check.get()==0:
		messagebox.showerror('Error','Please Accept Terms & conditions ')
	else:
		try:
			con=pymysql.connect(host='localhost',user='root',password='')
			mycursor=con.cursor()
		except:
			messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
			return
		try:
			query='create Database userdata'
			mycursor.execute(query)
			query='use userdata'
			mycursor.execute(query)
			query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(50),password varchar(20))'
			mycursor.execute(query)
		except:
			mycursor.execute('Use userdata')
		query='select * from data where username=%s'
		mycursor.execute(query,(UsernameEntry.get()))
		row=mycursor.fetchone()
		if row !=None:
			messagebox.showerror('Error','Username Already exists')
		else:
			query='insert into data(email,username,password)values(%s,%s,%s)'
			mycursor.execute(query,(emailEntry.get(),UsernameEntry.get(),PasswordEntry.get()))
			con.commit()
			con.close()
			messagebox.showinfo('Success','Registration is sucessful')
			clear()
			signup_window.destroy()
			import Railway.py


def login_page():
	signup_window.destroy()
	import Railway.py


#GUI PART
signup_window=Tk()
signup_window.title("IRCTC")
signup_window.geometry("1830x1490")
signup_window.iconbitmap("icon.ico")

# train photo
photo = PhotoImage(file='t.py')
lb = Label(signup_window,image=photo)
lb.pack()
# white bg
white=Label(signup_window,text='  ',font=('microsoft yahei UI Light',400,"bold"),bg='white',fg='firebrick1')
white.place(height=400,width=350,x=1050,y=50)
#userlogin
heading=Label(signup_window,text='CREATE AN ACCOUNT',font=('arial',22,"bold"),bg='white',fg='firebrick1')
heading.place(x=1057,y=60)
# G MAIL
emaillabel=Label(signup_window,text='Email',font=('microsoft yahei UI Light',12,"bold"),bg='white',fg='firebrick1')
emaillabel.place(x=1090,y=110)
emailEntry=Entry(signup_window,width=25,font=('microsoft yahei UI Light',13,"bold"),fg='white',bg='firebrick1')
emailEntry.place(x=1089,y=135)
# username
Usernamelabel=Label(signup_window,text='Username',font=('microsoft yahei UI Light',12,"bold"),bg='white',fg='firebrick1')
Usernamelabel.place(x=1090,y=162)
UsernameEntry=Entry(signup_window,width=25,font=('microsoft yahei UI Light',13,"bold"),fg='white',bg='firebrick1')
UsernameEntry.place(x=1089,y=190)
# password
Passwordlabel=Label(signup_window,text='Password',font=('microsoft yahei UI Light',12,"bold"),bg='white',fg='firebrick1')
Passwordlabel.place(x=1090,y=217)
PasswordEntry=Entry(signup_window,width=25,font=('microsoft yahei UI Light',13,"bold"),fg='white',bg='firebrick1')
PasswordEntry.place(x=1089,y=245)
# confirmpassword
confirmpasswordlabel=Label(signup_window,text='Confirm Password',font=('microsoft yahei UI Light',12,"bold"),bg='white',fg='firebrick1')
confirmpasswordlabel.place(x=1090,y=272)
confirmpasswordEntry=Entry(signup_window,width=25,font=('microsoft yahei UI Light',13,"bold"),fg='white',bg='firebrick1')
confirmpasswordEntry.place(x=1089,y=300)
# term S condition
check=IntVar()
termandconditions=Checkbutton(signup_window,text='I agree to the terms & conditions',font=('microsoft yahei UI Light',11,"bold"),fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
termandconditions.place(x=1075,y=335)
#signupbutton
signupbutton=Button(signup_window,text='Signup',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=1,width=23,command=connect_database)
signupbutton.place(x=1067,y=370)
# dont have account
donthaveaclabel=Label(signup_window,text='Dont have an account?',font=('Open Sans',11,'bold'),fg='firebrick1',bg='white')
donthaveaclabel.place(x=1083,y=417)
loginbutton=Button(signup_window,text='Log_in',font=('Open Sans',10,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=login_page)
loginbutton.place(x=1260,y=417)




signup_window.mainloop()
