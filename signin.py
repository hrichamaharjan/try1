from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import loginclass
#from login2 import *

class User_Form:
    def __init__(self, window):
        # self.my_connection = mysql.connector.connect(
        #     host='localhost',
        #     user='root',
        #
        #     password='',
        #     database='register'
        #
        # )
        # self.my_cursor = self.my_connection.cursor()
        self.window = window

        self.window.title('User Form')
        self.window.geometry('1200x630+0+0')

        self.bg = ImageTk.PhotoImage(file='C:\\Users\\Dell\\Desktop\\jarvis\\default_wallpaper.webp')
        self.bg_Image = Label(self.window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file='C:\\Users\\Dell\\Desktop\\jarvis\\Webp.net-resizeimage (3).jpg')

        self.lefty = Label(self.window, image=self.left).place(x=80, y=100, width=400)
        self.btnleft = Button(self.window, text='Login', relief=RAISED, bg='green', font=('arial', 14, 'bold'),
                              fg='white',command=self.login_back)
        self.btnleft.place(x=200, y=450, width=100)

        self.frame = Frame(self.window, bg='white')
        self.frame.place(x=480, y=100, width=600, height=400)
        self.title = Label(self.frame, text='Register Here', font=('times new roman', 20, 'bold'), bg='white',
                           fg='green').place(x=50, y=20)

        self.f_name = Label(self.frame, text='First Name', font=('times new roman', 15, 'bold'), bg='white',
                            fg='gray').place(x=50, y=60)
        self.txt_f_name = Entry(self.frame, font=('times new roman', 15), bg="lightgray")
        self.txt_f_name.place(x=50, y=90, width=250)
        self.l_name = Label(self.frame, text='Lastt Name', font=('times new roman', 15, 'bold'), bg='white',
                            fg='gray').place(x=330, y=60)

        self.txt_l_name = Entry(self.frame, font=('times new roman', 15), bg="lightgray")
        self.txt_l_name.place(x=330, y=90, width=250)
        self.contact = Label(self.frame, text='Contact No', font=('times new roman', 15, 'bold'), bg='white', fg='gray')
        self.contact.place(x=50, y=120)
        self.txt_contact = Entry(self.frame, font=('times new roman', 15), bg="lightgray")
        self.txt_contact.place(x=50, y=150, width=250)
        self.email = Label(self.frame, text='Email', font=('times new roman', 15, 'bold'), bg='white', fg='gray')
        self.email.place(x=330, y=120)
        self.txt_email = Entry(self.frame, font=('times new roman', 15), bg="lightgray")
        self.txt_email.place(x=330, y=150, width=250)
        self.password = Label(self.frame, text='Password', font=('times new roman', 15, 'bold'), bg='white',
                              fg='gray').place(x=50, y=180)
        self.txt_password = Entry(self.frame, font=('times new roman', 15),show='*', bg="lightgray")
        self.txt_password.place(x=50, y=210, width=250)
        self.pw = Label(self.frame, text='Confirm Password', font=('times new roman', 15, 'bold'), bg='white',
                        fg='gray').place(x=330, y=180)
        self.txt_pw = Entry(self.frame, font=('times new roman', 15),show='*', bg="lightgray")
        self.txt_pw.place(x=330, y=210, width=250)
        self.qst = Label(self.frame, text='Security Question', font=('times new roman', 15, 'bold'), bg='white',
                             fg='gray').place(x=50, y=240)
        self.txt_qst = ttk.Combobox(self.frame, font=('times new roman', 13),state='readonly',justify=CENTER)
        self.txt_qst['values']=('Select','Your First Pet Name?','Your Birth Place?','Your NickName?')
        self.txt_qst.place(x=50, y=270, width=250)
        self.txt_qst.current(0)
        self.answer = Label(self.frame, text='Answer', font=('times new roman', 15, 'bold'), bg='white', fg='gray').place(
            x=330, y=240)
        self.txt_answer = Entry(self.frame, font=('times new roman', 15), bg="lightgray")
        self.txt_answer.place(x=330, y=270, width=250)
        self.var_chk = IntVar()
        self.chk = Checkbutton(self.frame, text='I Agree The Terms And Conditions', variable=self.var_chk, onvalue=1,
                               offvalue=0, bg='white').place(x=50, y=310)
        self.btn1 = Button(self.frame, text='Register', relief=RAISED, bg='green', font=('arial', 14, 'bold'),
                           fg='white', command=self.register_data)
        self.btn1.place(x=160, y=358,width=250)
    def clear(self):
        self.txt_f_name.delete(0,END)
        self.txt_l_name.delete(0,END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_pw.delete(0, END)
        self.txt_qst.set('')
        self.txt_answer.delete(0, END)

    def login_back(self):
        import login2
        self.window.withdraw()
        dd = Toplevel(self.window)

        login2.Login(dd)

    def register_data(self):
        if self.txt_f_name.get() == "" or self.txt_email.get() == "" or self.txt_password.get() == "" or self.txt_pw.get() == "" or self.txt_answer.get() == "" or self.txt_qst.get()=="":
            messagebox.showerror('error', 'all fields are required', parent=self.window)
        elif self.txt_password.get() != self.txt_pw.get():
            messagebox.showerror('error', 'password doesnot match', parent=self.window)
        elif self.var_chk.get() == 0:
            messagebox.showerror('error', 'please agree our terms and condition')
        else:
            try:

                # qry = 'insert into users(f_name,l_name,contact,email,password,question,answer) values(%s,%s,%s,%s,%s,%s,%s)'
                # values= (self.txt_f_name.get(),
                #  self.txt_l_name.get(),
                #  self.txt_contact.get(),
                #  self.txt_email.get(),
                #  self.txt_password.get(),
                #  self.txt_qst.get(),
                #  self.txt_answer.get()
                #  )
                #
                # self.my_cursor.execute(qry,values)
                # self.my_connection.commit()
                loginclass.Register().register_entry(self.txt_f_name.get(),self.txt_l_name.get(),self.txt_contact.get(),self.txt_email.get(),self.txt_password.get(),self.txt_qst.get(),self.txt_answer.get())


                messagebox.showinfo('success', 'Register successfull', parent=self.window)
                self.clear()
            except Exception as e:
                messagebox.showerror('error', f'error:{str(e)}', parent=self.window)



#
# window = Tk()
# ob = User_Form(window)
# window.mainloop()
#






