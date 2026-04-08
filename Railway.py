from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
from tkcalendar import DateEntry
from tkinter import ttk 
import tkinter
import qrcode

#FUNCTIONALITY PART

def create_booking_table():
    con = pymysql.connect(host='localhost',user='root',password='',database='Traindata')
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50),
            passenger VARCHAR(50),
            train_name VARCHAR(50),
            source VARCHAR(50),
            destination VARCHAR(50),
            status VARCHAR(20)
        )
    """)
    con.commit()
    con.close()


def Forget_pass():
    def Change_password():
        if usernamefEntry.get()=='' or newpassEntry.get()=='' or confirmpassEntry.get()=='':
            messagebox.showerror('Error','All Fields Are Required', parent=window)
        elif newpassEntry.get()!=confirmpassEntry.get():
            messagebox.showerror('Error','Password and Confirm Password are not matching', parent=window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='',database='userdata')
            mycursor=con.cursor()
            query='select * from data where Username=%s'
            mycursor.execute(query, (usernamefEntry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username', parent=window)
            else:
                query='Update data set password=%s where Username=%s'
                mycursor.execute(query,(newpassEntry.get(),usernamefEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, please login with new password', parent=window)
                window.destroy()



    window = Toplevel()
    window.geometry("1830x1490")
    window.title('Change Password')
    window.iconbitmap("icon.ico")


    bgpic = PhotoImage(file='t.py')
    bglabel = Label(window,image=bgpic)
    bglabel.place(width=1550,height=835)

    # white bg
    white=Label(window,text='  ',font=('microsoft yahei UI Light',400,"bold"),bg='white',fg='firebrick1')
    white.place(height=290,width=330,x=1050,y=50)


    headingfogret=Label(window,text='RESET PASSWORD',font=('arial',25,"bold"),bg='white',fg='firebrick1')
    headingfogret.place(x=1057,y=60)

    #username
    usernameflabel=Label(window,text='Username',font=('arial',12,"bold"),bg='white',fg='orchid1')
    usernameflabel.place(x=1090,y=110)
    usernamefEntry=Entry(window,width=25,fg='magenta2',font=('arial',13,"bold"),bd=3)
    usernamefEntry.place(x=1089,y=135)
    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=155)

    newpasslabel=Label(window,text='New Password',font=('arial',12,"bold"),bg='white',fg='orchid1')
    newpasslabel.place(x=1089,y=162)
    newpassEntry=Entry(window,width=25,fg='magenta2',font=('arial',13,"bold"),bd=3)
    newpassEntry.place(x=1089,y=185)
    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=155)

    confirmpasslabel=Label(window,text='Confirm Password',font=('arial',12,"bold"),bg='white',fg='orchid1')
    confirmpasslabel.place(x=1088,y=210)
    confirmpassEntry=Entry(window,width=25,fg='magenta2',font=('arial',13,"bold"),bd=3)
    confirmpassEntry.place(x=1089,y=233)
    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=155)


    Submitbutton=Button(window,text='Submit',font=('Open Sans',9,'bold'),fg='white',bg='magenta2',width=39,height=2,activeforeground='white',activebackground='magenta2',cursor='hand2',command=Change_password)
    Submitbutton.place(x=1073,y=281)



    window.mainloop()


def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return

        query='use userdata'
        mycursor.execute(query)
        query='select * from data where Username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid Username and password')
        else:
            messagebox.showerror('Welcome','Login is Successful')
            create_booking_table()
            login = Toplevel()
            login.geometry("1833x1490")
            login.title('IRCTC')
            login.iconbitmap("icon.ico")



            def home_1():
                home_1 = Toplevel()
                home_1.geometry("1033x990")
                home_1.resizable(False, False)
                home_1.title('Home')
                home_1.iconbitmap("icon.ico")
                homepic = PhotoImage(file='h.py')
                homelabel = Label(home_1,image=homepic)
                homelabel.place(x=0,y=0,relwidth=1,relheight=1)

                home_1.mainloop()


            def help_1(): 
                help_1 = Toplevel()
                help_1.title('Help')
                help_1.geometry("530x790")
                help_1.resizable(False, False)
                help_1.iconbitmap("icon.ico")
                help_1pic = PhotoImage(file='he.py')
                help_1label = Label(help_1,image=help_1pic)
                help_1label.image = help_1pic
                help_1label.place(x=0,y=0,relwidth=1,relheight=1)

                help_1.mainloop()


            def emp_1():
                emp_1 = Toplevel()
                emp_1.geometry("1085x698")
                emp_1.resizable(False, False)
                emp_1.title('Employee')
                emp_1.iconbitmap("icon.ico")
                emp_1pic = PhotoImage(file='p.py')
                emp_1label = Label(emp_1,image=emp_1pic)
                emp_1label.pack()

                emp_1.mainloop()

            def t_find():
                t_find = Toplevel()
                t_find.geometry("1085x698")
                t_find.iconbitmap("icon.ico")
                t_find.resizable(False, False)
                t_find.title("Available Trains") 

                from_city = from_var.get()
                to_city = to_var.get()
                if from_city == 'From*' or to_city == 'To*':
                    messagebox.showerror("Error", "Please select From and To")
                    return

                con = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='Traindata'
                )
                cur = con.cursor()
           
                cur.execute(
                    "SELECT Train_no, Train_name, source, destination, classes FROM Data WHERE source=%s AND destination=%s",
                    (from_city, to_city)
                )
                rows = cur.fetchall()
           
                columns = ("Train No", "Train Name", "From", "To", "Class")
                tree = ttk.Treeview(t_find, columns=columns, show="headings")
                tree.pack(fill=BOTH, expand=True)
           
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=150)
           
                for row in rows:
                    tree.insert("", END, values=row)
           
                con.close()

                def book_ticket():
                     selected = tree.focus()
                     if not selected:
                         messagebox.showerror("Error", "Select a train")
                         return
                     data = tree.item(selected)['values']
                     passenger_page(data)
             
                Button(t_find, text="Book Ticket",
                        bg="green", fg="white",
                        font=("Arial",12,"bold"),
                        command=book_ticket).pack(pady=20)

                def passenger_page(train):
                    p = Toplevel()
                    p.geometry("400x400")
                    p.title("Passenger Details")
                    Label(p, text="Name").pack()
                    name = Entry(p)
                    name.pack()
                    Label(p, text="Age").pack()
                    age = Entry(p)
                    age.pack()
                    Label(p, text="Gender").pack()
                    gender = ttk.Combobox(p, values=["Male","Female","Other"])
                    gender.pack()
                    Button(p, text="Proceed to Payment",bg="firebrick1", fg="white",command=lambda: payment_page(train, name.get())).pack(pady=20)
                def payment_page(train, passenger):
                    pay = Toplevel()
                    pay.geometry("400x450")
                    pay.title("Payment")
    
                    Label(pay, text="Scan & Pay", font=("Arial",16,"bold")).pack()
                    qr = qrcode.make("https://youtu.be/xvFZjo5PgG0?si=_sj0UGtT4wRwTtgz")
                    qr.save("qr.png")
                    img = Image.open("qr.png").resize((200,200))
                    photo = ImageTk.PhotoImage(img)
                    lbl = Label(pay, image=photo)
                    lbl.image = photo
                    lbl.pack()
                    Button(pay, text="Payment Done",bg="green", fg="white",font=("Arial",12,"bold"),command=lambda: ticket_page(train, passenger)).pack(pady=20)

                def ticket_page(train, passenger):
                    t = Toplevel()
                    t.geometry("400x300")
                    t.title("Ticket")                    
                    Label(t, text="🎉 Ticket Confirmed 🎉",
                          fg="green", font=("Arial",16,"bold")).pack()                    
                    Label(t, text=f"Passenger: {passenger}").pack()
                    Label(t, text=f"Train: {train[1]}").pack()
                    Label(t, text=f"{train[2]} → {train[3]}").pack()
                    Label(t, text="Status: CONFIRMED").pack(pady=10)                    
                    # 🔴 SAVE BOOKING IN DATABASE
                    con = pymysql.connect(
                        host='localhost',
                        user='root',
                        password='',
                        database='Traindata'
                    )
                    cur = con.cursor()                    
                    cur.execute("""
                        INSERT INTO bookings
                        (username, passenger, train_name, source, destination, status)
                        VALUES (%s,%s,%s,%s,%s,%s)
                    """, (
                        usernameEntry.get(),   # logged in user
                        passenger,
                        train[1],
                        train[2],
                        train[3],
                        "CONFIRMED"
                    ))                    
                    con.commit()
                    con.close()

    
    
                t_find.mainloop()

            def exit_ji():
                login.destroy()
                import railway.py

            def booking_history():
                bh = Toplevel()
                bh.geometry("900x400")
                bh.title("Booking History")
        
                columns = ("Passenger", "Train", "From", "To", "Status")
                tree = ttk.Treeview(bh, columns=columns, show="headings")
                tree.pack(fill=BOTH, expand=True)
        
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=150)
        
                con = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='Traindata'
                 )
                cur = con.cursor()
            
                cur.execute("""
                     SELECT passenger, train_name, source, destination, status
                     FROM bookings
                     WHERE username=%s
                 """, (usernameEntry.get(),))
            
                rows = cur.fetchall()
                con.close()
        
                for row in rows:
                    tree.insert("", END, values=row)

            def cancel_ticket():
                ct = Toplevel()
                ct.geometry("900x400")
                ct.title("Cancel Ticket")
            
                columns = ("ID", "Passenger", "Train", "From", "To", "Status")
                tree = ttk.Treeview(ct, columns=columns, show="headings")
                tree.pack(fill=BOTH, expand=True)
            
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=140)
            
                con = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='Traindata'
                )
                cur = con.cursor()
            
                cur.execute("""
                    SELECT id, passenger, train_name, source, destination, status
                    FROM bookings
                    WHERE username=%s AND status='CONFIRMED'
                """, (usernameEntry.get(),))
            
                rows = cur.fetchall()
                con.close()
            
                for row in rows:
                    tree.insert("", END, values=row)
            
                def do_cancel():
                    selected = tree.focus()
                    if not selected:
                        messagebox.showerror("Error", "Pehle ticket select kar bhai")
                        return
            
                    booking_id = tree.item(selected)['values'][0]
            
                    con = pymysql.connect(
                        host='localhost',
                        user='root',
                        password='',
                        database='Traindata'
                    )
                    cur = con.cursor()
            
                    cur.execute(
                        "UPDATE bookings SET status='CANCELLED' WHERE id=%s",
                        (booking_id,)
                    )
            
                    con.commit()
                    con.close()
            
                    messagebox.showinfo("Done", "Ticket Cancel ho gayi 😌")
                    ct.destroy()
                    cancel_ticket()   # refresh
            
                Button(
                    ct,
                    text="Cancel Selected Ticket",
                    bg="red",
                    fg="white",
                    font=("Arial",12,"bold"),
                    command=do_cancel
                ).pack(pady=20)
            

            def t_add():
                t_add = Toplevel()
                t_add.geometry("259x294")
                t_add.resizable(False, False)
                t_add.title('Admin')
                t_add.iconbitmap("icon.ico")

                def Add_t():
                    if (trainnameEntry.get()=='' or trainnoEntry.get()=='' or sourceEntry.get()=='' or destinationEntry.get()=='' or classEntry.get()==''):
                        messagebox.showerror('Error','All Fields Are Required')
                        return
                    try:
                        con = pymysql.connect(host='localhost', user='root', password='', database='Traindata')
                        mycursor = con.cursor()
                    except:
                        messagebox.showerror('Error','Database Connectivity Issue')
                        return

                 # Create table if not exists
                    mycursor.execute("""
                        CREATE TABLE IF NOT EXISTS Data(
                            Train_no INT PRIMARY KEY,
                            Train_name VARCHAR(50),
                            source VARCHAR(50),
                            destination VARCHAR(50),
                            classes VARCHAR(50)
                             )
                             """)
                     # Check duplicate train name
                    mycursor.execute("SELECT * FROM Data WHERE Train_name=%s",(trainnameEntry.get(),))
                    if mycursor.fetchone():
                        messagebox.showerror('Error','Train name already exists')
                        con.close()
                        return
                    # Insert data
                    mycursor.execute("""INSERT INTO Data(Train_no, Train_name, source, destination, classes)
                        VALUES (%s,%s,%s,%s,%s)
                        """, (
                    trainnoEntry.get(),
                    trainnameEntry.get(),
                    sourceEntry.get(),
                    destinationEntry.get(),
                    classEntry.get()
                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success','Train added successfully')
                    t_add.destroy()

                # train no
                trainnolabel=Label(t_add,text='Train_no',font=('microsoft yahei UI Light',12,"bold"),bg='white',fg='firebrick1')
                trainnolabel.place(x=1,y=0)
                trainnoEntry=Entry(t_add,width=25,font=('microsoft yahei UI Light',13,"bold"),fg='white',bg='firebrick1')
                trainnoEntry.place(x=1,y=21)
                # username
                trainnamelabel=Label(t_add,text='Train_name',font=('microsoft yahei UI Light',12,"bold"),bg='white',fg='firebrick1')
                trainnamelabel.place(x=1,y=48)
                trainnameEntry=Entry(t_add,width=25,font=('microsoft yahei UI Light',13,"bold"),fg='white',bg='firebrick1')
                trainnameEntry.place(x=1,y=70)
                # source
                sourcelabel=Label(t_add,text='source',font=('microsoft yahei UI Light',12,"bold"),bg='white',fg='firebrick1')
                sourcelabel.place(x=1,y=97)
                sourceEntry=Entry(t_add,width=25,font=('microsoft yahei UI Light',13,"bold"),fg='white',bg='firebrick1')
                sourceEntry.place(x=1,y=117)
                # destination
                destinationlabel=Label(t_add,text='destination',font=('microsoft yahei UI Light',12,"bold"),bg='white',fg='firebrick1')
                destinationlabel.place(x=1,y=145)
                destinationEntry=Entry(t_add,width=25,font=('microsoft yahei UI Light',13,"bold"),fg='white',bg='firebrick1')
                destinationEntry.place(x=1,y=166)
                # all class
                classlabel=Label(t_add,text='classes',font=('microsoft yahei UI Light',12,"bold"),bg='white',fg='firebrick1')
                classlabel.place(x=1,y=193)
                classEntry=Entry(t_add,width=25,font=('microsoft yahei UI Light',13,"bold"),fg='white',bg='firebrick1')
                classEntry.place(x=1,y=215)
                #addbutton
                addbutton=Button(t_add,text='Add_tain',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=1,width=19,command=Add_t)
                addbutton.place(x=1,y=250)


                t_add.mainloop()


            loginpic = PhotoImage(file='t.py')
            loginlabel = Label(login,image=loginpic)
            loginlabel.place(width=1550,height=835)

            # white for login
            white1=Label(login,text='  ',font=('microsoft yahei UI Light',400,"bold"),bg='black',fg='firebrick1')
            white1.place(height=30,width=33000,x=0,y=5)
            homebutton=Button(login,text='Home',font=('Open Sans',11,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=1,width=11,command=home_1) 
            homebutton.place(x=0,y=5)
            homebutton=Button(login,text='Help',font=('Open Sans',11,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=1,width=11,command=help_1) 
            homebutton.place(x=107,y=5)
            homebutton=Button(login,text='Employee',font=('Open Sans',11,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=1,width=11,command=emp_1) 
            homebutton.place(x=214,y=5)
            homebutton=Menubutton(login,text='Admin',font=('Open Sans',12,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=1,width=12)
            admin=Menu(homebutton,tearoff=0)
            admin.add_command(label="Train add",command=t_add)
            admin.add_command(label="Booking History",command=booking_history)
            admin.add_command(label="Cancel Ticket",command=cancel_ticket)
            admin.add_command(label="Exit",command=exit_ji)
            homebutton['menu']=admin
            homebutton.place(x=321,y=5)

            # white bg
            white=Label(login,text='  ',font=('microsoft yahei UI Light',400,"bold"),bg='white',fg='firebrick1')
            white.place(height=300,width=330,x=1050,y=50)
            #userlogin
            heading=Label(login,text='Book Your Ticket',font=('chiller',35,"bold"),bg='white',fg='firebrick1')
            heading.place(x=1085,y=60)
            # from
            stations=['Delhi','Mumbai','Jaipur','Kolkata','Mathura',"Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
            from_var=StringVar()
            box=ttk.Combobox(login,values=stations,textvariable=from_var)
            box.set('From*')
            box.place(x=1065,y=152,height=23,width=295)
            Frame(login,width=294,height=2,bg='firebrick1').place(x=1065,y=172)
            # to
            stations1=['Delhi','Mumbai','Jaipur','Kolkata','Mathura',"Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
            to_var=StringVar()
            box1=ttk.Combobox(login,values=stations1,textvariable=to_var)
            box1.set('To*')
            box1.place(x=1065,y=190,height=23,width=295)
            Frame(login,width=294,height=2,bg='firebrick1').place(x=1065,y=210)
            # date
            Date = DateEntry(login,selectmode='everyday',width=45,height=3)
            Date.place(x=1065,y=230)
            Frame(login,width=293,height=3,bg='firebrick1').place(x=1065,y=250)
            # all class
            classes=['1AC','2AC','3AC','SLEEPER','SECOND SEATING']
            class_var3=StringVar()
            box=ttk.Combobox(login,values=classes,textvariable=class_var3)
            box.set('All Classes')
            box.place(x=1065,y=270,height=23,width=295)
            Frame(login,width=294,height=2,bg='firebrick1').place(x=1065,y=290)
            # login button 
            findtrainsbutton=Button(login,text='Find Trains',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=1,width=24,command=t_find) 
            findtrainsbutton.place(x=1055,y=302)
            



            login.mainloop()
    

def hide():
    openeye.config(file='eye.png')
    passwordEntry.config(show='*')
    eyebutton.config(command=show)


def show():
    openeye.config(file='eye.png')
    passwordEntry.config(show='')
    eyebutton.config(command=hide)

def signup_page():
    railway.destroy()
    import signup



def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def PASS_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


#GUI PART
railway=Tk()
railway.title("IRCTC")
railway.geometry("1830x1490")
railway.iconbitmap("icon.ico")

# train photo
photo = PhotoImage(file="t.py")
lb = Label(railway,image=photo)
lb.pack()
# white bg
white=Label(railway,text='  ',font=('microsoft yahei UI Light',400,"bold"),bg='white',fg='firebrick1')
white.place(height=300,width=330,x=1050,y=50)

#heading
headingirctc=Label(railway,text='INDIAN RAILWAYS',font=(' black',35),fg="firebrick1",bg=None)
headingirctc.place(x=110,y=50)

#headingir
headingir=Label(railway,text='Safety.Security.Punctuality',font=('poppins',25,"bold"))
headingir.place(x=105,y=125)

#userlogin
heading=Label(railway,text='USER LOGIN',font=('arial',30,"bold"),bg='white',fg='firebrick1')
heading.place(x=1085,y=60)

# login entry
usernameEntry=Entry(railway,width=32,font=('microsoft yahei UI Light',11,"bold"),bg='white',fg='firebrick1')
usernameEntry.place(x=1065,y=150)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)
Frame(railway,width=290,height=2,bg='firebrick1').place(x=1065,y=172)

# password
passwordEntry=Entry(railway,width=32,font=('microsoft yahei UI Light',11,"bold"),bg='white',fg='firebrick1')
passwordEntry.place(x=1065,y=190)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',PASS_enter)
Frame(railway,width=290,height=2,bg='firebrick1').place(x=1065,y=210)
# hide show password
openeye=PhotoImage(file='eye.png')
eyebutton=Button(railway,image=openeye,bd=50,bg='white',activebackground='white',cursor='hand2',command=hide)
eyebutton.place(width=12,height=21,x=1359,y=190)
# forget password
forgetbutton=Button(railway,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('microsoft yahei UI Light',9,"bold"),fg='firebrick1',activeforeground='firebrick1',command=Forget_pass)
forgetbutton.place(x=1240,y=233)
# login button
loginbutton=Button(railway,text='LOGIN',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=1,width=23,command=login_user)
loginbutton.place(x=1060,y=265)
# create new account button
gnuplabel=Label(railway,text='Dont have an account?',font=('Open Sans',10,'bold'),fg='firebrick1',bg='white')
gnuplabel.place(x=1075,y=321)

newaccountbutton=Button(railway,text='Create New One',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountbutton.place(x=1230,y=321)


railway.mainloop()