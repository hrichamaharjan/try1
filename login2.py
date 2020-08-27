
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox, ttk
import mysql.connector
import signin
import welcome
import loginclass


class Login:
    def __init__(self, window):
        self.window = window

        self.window.title('User Form')
        self.window.geometry('1100x790+100+0')
        self.window.resizable(0, 0)

        self.bg = ImageTk.PhotoImage(file='C:\\Users\\Dell\\PycharmProjects\\untitled3\\project\\Webp.net-resizeimage (5).jpg')
        self.bg_Image = Label(self.window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.frame1 = Frame(self.window, bg='white')
        self.frame1.place(x=380, y=260, height=330, width=450)
        self.frame3=Frame(self.window,bg='lightgrey')
        self.frame3.place(x=0,y=0,height=100,width=1100)
        self.head=Label(self.frame3,text='Online Flight Booking System', font=('Goudy old style', 29,'bold'),fg='#4F3A65',bg='lightgrey').place(x=270,y=10)


        self.frame2 = Frame(self.window, bg='grey')
        self.frame2.place(x=0, y=70, height=55, width=1100)
        self.title = Label(self.frame1, text='Login Here', font=('Impact', 20, 'bold'), fg="#4F3A65", bg='white').place(
            x=50, y=15)
        self.desc = Label(self.frame1, text='Airline Ticket Login Area', font=('Goudy old style', 12), fg="#52437B",
                          bg='white').place(x=50, y=50)

        self.lb_code = Label(self.frame1, text='Email', font=('Goudy old style', 15, 'bold'), fg='#52437B',
                             bg='white').place(x=50, y=90)
        self.ent_code = Entry(self.frame1, font=('times new roman', 10), bg='lightgray')
        self.ent_code.place(x=150, y=90, width=200, height=30)
        self.pw_code = Label(self.frame1, text='Password', font=('Goudy old style', 15, 'bold'), fg='#52437B',
                             bg='white').place(x=50, y=160)
        self.ent_pw = Entry(self.frame1, font=('times new roman', 10), bg='lightgray')
        self.ent_pw.place(x=150, y=160, width=200, height=30)
        self.btn1 = Button(self.frame2, text='signup', relief=RAISED, bg='grey', font=('arial', 14, 'bold'),
                           fg='white', bd=0,command=self.sign_up)
        self.btn1.place(x=150, y=6)
        self.btn2 = Button(self.frame2, text='Home', relief=RAISED, bg='grey', font=('arial', 14, 'bold'),
                           fg='white',bd=0)
        self.btn2.place(x=10, y=6)
        self.btn3 = Button(self.frame1, text='Login', relief=RAISED, bg='#48284A', font=('arial', 14, 'bold'),
                           fg='white', command=self.login_function)
        self.btn3.place(x=160, y=260, width=180)
        self.bg1 = ImageTk.PhotoImage(file='C:\\Users\\Dell\\PycharmProjects\\untitled3\\project\\Webp.net-resizeimage (3).png')
        self.btn4 = Button(self.window, image=self.bg1,text='Exit', relief=RAISED, bg='grey', font=('arial', 14, 'bold'),
                           fg='white',bd=0, command=exit)
        self.btn4.place(x=1000, y=70, width=90)
        self.btn5 = Button(self.frame1, text='Forget password?', bg='white', font=('times new roman', 12, 'bold'),
                           fg='#52437B', bd=0, command=self.forget_password)
        self.btn5.place(x=50, y=220)
        # self.window.mainloop()

    def login_function(self):
        email = self.ent_code.get()
        password = self.ent_pw.get()


        if self.ent_code.get() == "" or self.ent_pw.get() == "":
            messagebox.showerror('error', 'all fields are required', parent=self.window)

        # elif self.ent_code.get() != "Hricha" or self.ent_pw.get() != "123456":
        #     messagebox.showerror('error', 'Invalid username or password', parent=self.window)
        else:
            try:
                # con = mysql.connector.connect(host='localhost', user='root', password='', database='register')
                # cur = con.cursor()
                # cur.execute('select * from users where email=%s and password=%s',
                #             (self.ent_code.get(), self.ent_pw.get()))


                usr = loginclass.Login().login_user(email,password)
                if usr:
                    if loginclass.Login().login_user(email,password):
                        messagebox.showinfo('Success', 'Welcome', parent=self.window)

                        self.window.withdraw()
                        dd = Toplevel(self.window)
                        welcome.welcome(usr[0], dd)
                    # self.window.destroy()
                    # ItemView(usr[0])
                else:
                    messagebox.showerror('Error', 'Wrong id or password')
                print(usr)


            except Exception as e:
                messagebox.showerror('error', f'error:{str(e)}', parent=self.window)
            # print(self.ent_code.get(), self.ent_pw.get())
            # messagebox.showinfo('welcome user', parent=self.window)

    def forget_password(self):
        self.window2 = Toplevel()
        self.window2.title('Forget Password')
        self.window2.geometry('350x300+490+150')
        self.window2.config(bg='white')
        self.window2.focus_force()
        self.window2.grab_set()
        t = Label(self.window2, text='Verify Email', font=('times new roman', 20, 'bold'), bg='white',
                  fg='#52437B').place(x=0, y=10, relwidth=1)

        self.lb_email = Label(self.window2, text='Email', font=('Goudy old style', 15, 'bold'), fg='grey',
                              bg='white').place(x=50, y=90)
        self.ent_code = Entry(self.window2, font=('times new roman', 10), bg='lightgray')
        self.ent_code.place(x=50, y=140, width=260, height=30)

        self.btn1 = Button(self.window2, text='Login', relief=RAISED, bg='#273043', font=('arial', 14, 'bold'),
                           fg='white', command=self.verification)
        self.btn1.place(x=100, y=210, width=180)

    def verification(self):

        if self.ent_code.get() == "":
            messagebox.showerror('Error', 'Please enter the email address to reset your password', parent=self.window)

        else:
            try:
                # con = mysql.connector.connect(host='localhost', user='root', password='', database='register')
                # cur = con.cursor()
                # cur.execute('select * from users where email=%s', (self.ent_code.get(),))
                # row = cur.fetchone()
                usr=loginclass.Recover_pw().forget_pw(self.ent_code.get())
                if usr == None:
                    messagebox.showerror('Error', 'Please enter valid email', parent=self.window)

                else:
                    self.window2 = Toplevel()
                    self.window2.title('Forget Password')
                    self.window2.geometry('350x400+490+150')
                    self.window2.config(bg='white')
                    self.window2.focus_force()
                    self.window2.grab_set()
                    t = Label(self.window2, text='Forget Password', font=('times new roman', 20, 'bold'), bg='white',
                              fg='red').place(x=0, y=10, relwidth=1)
                    qst = Label(self.window2, text='Security Question', font=('times new roman', 15, 'bold'),
                                     bg='white',
                                     fg='gray').place(x=50, y=100)

                    txt_qst = ttk.Combobox(self.window2, font=('times new roman', 13), state='readonly',
                                                justify=CENTER)
                    txt_qst['values'] = ('Select', 'Your First Pet Name?', 'Your Birth Place?', 'Your NickName?')
                    txt_qst.place(x=50, y=130, width=250)
                    txt_qst.current(0)
                    answer = Label(self.window2, text='Answer', font=('times new roman', 15, 'bold'), bg='white',
                                        fg='gray').place(
                        x=50, y=180)
                    txt_answer = Entry(self.window2, font=('times new roman', 15), bg='lightgrey')
                    txt_answer.place(x=50, y=210, width=250)
                    new_pw = Label(self.window2, text='New Password', font=('times new roman', 15, 'bold'),
                                        bg='white',
                                        fg='gray').place(
                        x=50, y=260)
                    txt_new_pw = Entry(self.window2, font=('times new roman', 15), bg='lightgrey')
                    txt_new_pw.place(x=50, y=290, width=250)
                    lambda_function = lambda : self.answer_match(self.ent_code.get(),txt_qst, txt_answer,txt_new_pw)
                    btn_change_password = Button(self.window2, text='Reset Password', bg='#52437B', fg='white',
                                                 font=('times new roman', 15, 'bold'), command=lambda_function).place(
                        x=90, y=340)



            except Exception as e:
                messagebox.showerror('error', f'error:{str(e)}', parent=self.window)
            # print(self.ent_code.get(), se

    def answer_match(self,ent_code,txt_qst,txt_answer,txt_new_pw):

        if txt_qst.get() == "Select" or txt_answer.get() == "" or txt_new_pw.get() == "":

            messagebox.showerror('Error', 'All fields are required', parent=self.window2)

        else:
            try:

                # con = mysql.connector.connect(host='localhost', user='root', password='', database='register')
                # cur = con.cursor()
                #
                # cur.execute('select * from users where email=%s and question=%s and answer=%s',
                #             (ent_code, txt_qst.get(), txt_answer.get(),))
                # print(ent_code, txt_qst.get(), txt_answer.get())
                usr=loginclass.Answer_match().check_ans(ent_code, txt_qst.get(), txt_answer.get())
                if usr== None:
                    messagebox.showerror('Error', 'Please select correct security question', parent=self.window)
                else:
                    # cur.execute('update users set password=%s where email=%s ',
                    #             (txt_new_pw.get(),ent_code,))
                    # print('password',txt_new_pw.get())
                    # print(row)
                    # con.commit()
                    loginclass.Answer_match().update_pw(txt_new_pw.get(), ent_code)

                    messagebox.showinfo('Success')

            except Exception as e:
                messagebox.showerror('error', f'error:{str(e)}', parent=self.window)


    def sign_up(self):
        self.window.withdraw()
        dd = Toplevel(self.window)
        signin.User_Form(dd)


window = Toplevel()
obj = Login(window)
window.mainloop()
