from tkinter import *

from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import mysql.connector
import form2
import time
import datetime
from tkcalendar import Calendar, DateEntry
class oneway:

    def __init__(self,user, window):


        self.search_by=StringVar()

        self.search_txt=StringVar()
        self.list2 = [{'name':'Select','price':[]},{'name':'Economy','price':3000},{'name':'Premium Economy','price':4000},{'name':'Business Class','price':5000},{'name':'First Class','price':6000}]
        # Get the names of the all flights name

        self.names = list(map(lambda x: x.get('name'), self.list2))

        print(self.names)



        self.window = window
        self.user_id = user
        self.item_index=[]
        self.user=user
        self.window.title('User Form')
        self.window.geometry('1100x650+90+40')





        self.frame1 = Frame(self.window, bg='#37474F')
        self.frame1.place(x=0, y=0, height=650, width=1100)
        self.frame2 = Frame(self.frame1, bg='white',bd=1,relief=RIDGE)
        self.frame2.place(x=390, y=130, height=360, width=630)
        self.label_name = Label(self.frame1, text="One Way Flight", font=('Impact', 20, 'bold'), fg="white",
                                bg='#37474F')
        self.label_name.place(x=300, y=15)
        time1 = StringVar()
        time1.set(time.strftime('%H:%M:%S:%p'))
        self.ent_where = Label(self.frame1, font=('times new roman', 25),fg='white', bg='#37474F', textvariable=time1)
        self.ent_where.place(x=60, y=5)


        self.label_name = Label(self.frame1, text="Where From:", font=('Goudy old style', 12, 'bold'), fg='white',
                             bg='#37474F')
        self.label_name.place(x=50, y=90)
        self.ent_where = Entry(self.frame1, font=('times new roman', 9), bg='lightgray')
        self.ent_where.place(x=170, y=90, width=200, height=30)
        self.label_name = Label(self.frame1, text="Where To:", font=('Goudy old style', 12, 'bold'), fg='white',
                                bg='#37474F')
        self.label_name.place(x=50, y=140)
        self.ent_to = Entry(self.frame1, font=('times new roman', 9), bg='lightgray')
        self.ent_to.place(x=170, y=140, width=200, height=30)
        self.label_name = Label(self.frame1, text="Departure Date:", font=('Goudy old style', 12, 'bold'), fg='white',
                                bg='#37474F')
        self.label_name.place(x=50, y=190)
        self.ent_dpt = DateEntry(self.frame1, width=12, background='darkblue',
                                 foreground='white', borderwidth=2)
        self.ent_dpt.place(x=170, y=190, width=200)
        ttk.Button(self.frame1, text="ok")

        self.combo = Label(self.frame1, text="Age Selection:", font=('Goudy old style', 12, 'bold'), fg='white',
                                bg='#37474F').place(x=50, y=240)
        self.txt_combo = ttk.Combobox(self.frame1, font=('times new roman', 9), state='readonly', justify=CENTER)
        self.txt_combo['values'] = ('select','Adult', 'Children', 'Infant', 'Old age')

        self.txt_combo.place(x=170, y=240)
        self.txt_combo.current(0)

        self.label_name = Label(self.frame1, text="Count:", font=('Goudy old style', 12, 'bold'), fg='white',
                                bg='#37474F')
        self.label_name.place(x=50, y=290)
        self.ent_count = Entry(self.frame1, font=('times new roman', 9), bg='lightgray')
        self.ent_count.place(x=170, y=290, width=200, height=30)
        self.classcombo = Label(self.frame1, text="Class Selection:", font=('Goudy old style', 12, 'bold'), fg='white',
                           bg='#37474F').place(x=50, y=340)
        self.txt_classcombo = ttk.Combobox(self.frame1, font=('times new roman', 9), state='readonly', justify=CENTER,values=self.names)
        # self.txt_classcombo['values'] = ('Economy', 'Premium Economy', 'Business Class', 'First Class')
        self.txt_classcombo.bind('<<ComboboxSelected>>', self.fetch_data)

        self.txt_classcombo.place(x=170, y=340)
        self.txt_classcombo.current(0)
        self.label_price = Label(self.frame1, text="Price:", font=('Goudy old style', 12, 'bold'), fg='white',
                                bg='#37474F')
        self.label_price.place(x=50, y=390)
        self.ent_price = Entry(self.frame1, font=('times new roman', 9), bg='lightgray')
        self.ent_price.place(x=170, y=390, width=200, height=30)
        self.ent_price.insert(0,'')
        self.flight = Label(self.frame1, text="Flight Selection:", font=('Goudy old style', 12, 'bold'), fg='white',
                           bg='#37474F').place(x=50, y=440)
        self.txt_flight = ttk.Combobox(self.frame1, font=('times new roman', 9), state='readonly', justify=CENTER)
        self.txt_flight['values'] = ('select','Buddha Air', 'Yeti Airlines', 'Surya Airline', 'Nepal Airlines','Tara Airlines')

        self.txt_flight.place(x=170, y=440)
        self.txt_flight.current(0)

        self.item_entry = Entry(self.window,textvariable=self.search_txt)
        self.item_entry.place(x=400, y=90)
        self.txt_combo_1 = ttk.Combobox(self.frame1,textvariable=self.search_by, font=('times new roman', 9), state='readonly', justify=CENTER)
        self.txt_combo_1['values'] = ('flight_name', 'destination', 'class_selection')

        self.txt_combo_1.place(x=600, y=90)
        self.txt_combo_1.current(0)

        self.btn_add = Button(self.window, text="Search",command=self.Search_items)
        self.btn_add.place(x=800,y=90)

        self.btn_book = Button(self.frame1, text="Book Flight", relief=RAISED, bg='#001C55', font=('arial', 14, 'bold'),
                               fg='white', command=self.book_flight)
        self.btn_book.place(x=100, y=550)
        self.btn_book = Button(self.frame1, text="Cancel Flight", relief=RAISED, bg='#00072D', font=('arial', 14, 'bold'),
                               fg='white',command=self.delete_item)
        self.btn_book.place(x=540, y=550)
        self.btn_book = Button(self.frame1, text="Bill", relief=RAISED, bg='#00072D', font=('arial', 14, 'bold'),
                               fg='white',command=self.generate_bill)
        self.btn_book.place(x=700, y=550)
        self.btn_book = Button(self.frame1, text="Update", relief=RAISED, bg='#00072D', font=('arial', 14, 'bold'),
                               fg='white', command=self.update)
        self.btn_book.place(x=800, y=550)
        scroll_x = Scrollbar(self.frame2, orient=HORIZONTAL)
        self.bg1 = ImageTk.PhotoImage(file='C:\\Users\\Dell\\PycharmProjects\\untitled3\\project\\Webp.net-resizeimage (3).png')
        self.btn4 = Button(self.window, image=self.bg1, text='Logout', relief=RAISED, bg='#37474F',
                           font=('arial', 14, 'bold'),
                           fg='white', bd=0, command=exit)
        self.btn4.place(x=1000, y=7, width=90)



        self.item_tree = ttk.Treeview(self.frame2,selectmode='browse', columns=('ID','Where from', 'Where to', 'Departure Date','Age Selection','Count','Class Selection','User_id','Flight_Name','Price'),xscrollcommand=scroll_x.set)
        self.item_tree.pack(fill=BOTH,expand=1)
        #self.item_tree.place(x=390,y=120)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_x.config(command=self.item_tree.xview)




        self.item_tree['show'] = 'headings'
        self.item_tree.column('ID',width=90,anchor='center')
        self.item_tree.column('Where from', width=90,anchor='center')
        self.item_tree.column('Where to', width=90,anchor='center')
        self.item_tree.column('Departure Date', width=90,anchor='center')

        self.item_tree.column('Age Selection', width=90,anchor='center')
        self.item_tree.column('Count', width=90,anchor='center')
        self.item_tree.column('Class Selection', width=90,anchor='center')
        self.item_tree.column('User_id', width=90,anchor='center')

        self.item_tree.column('Flight_Name',width=90,anchor='center')

        self.item_tree.column('Price',width=90,anchor='center')
        self.item_tree.heading('ID', text="ID")
        self.item_tree.heading('Where from', text="Where from")
        self.item_tree.heading('Where to', text="Where to")
        self.item_tree.heading('Departure Date', text="Departure Date")

        self.item_tree.heading('Age Selection', text="Age Selection")
        self.item_tree.heading('Count', text="Count")
        self.item_tree.heading('Class Selection', text="Class Selection")
        self.item_tree.heading('User_id', text="User ID")
        self.item_tree.heading('Flight_Name', text="Flight_Name")
        self.item_tree.heading('Price', text="Price")

        # scroll_x = Scrollbar(manage_teacher_frame2_1, orient=HORIZONTAL)
        #
        # scroll_x.pack(side=BOTTOM, fill=X)
        # scroll_x.config(command=self.teacher_tree.xview)
        # scroll_y.pack(side=RIGHT, fill=Y)

        # self.item_treeScrollbar=ttk.Scrollbar(self.window,orient='horizontal',command=self.item_tree.xview)
        # self.item_tree.configure(xscroll=self.item_treeScrollbar.set)
        # self.item_treeScrollbar.pack(side=BOTTOM,fill=X)
        self.show_in_treeview()
    def clear(self):
        self.ent_where.delete(0,END)
        self.ent_to.delete(0,END)
        self.ent_dpt.delete(0, END)
        self.txt_combo.set('')
        self.ent_count.delete(0, END)
        self.txt_classcombo.set('')
    # def logout(self):
    #     messagebox.showinfo('Message','Do you want to log out')
    #     import login2
    #     self.window.withdraw()
    #     dd = Toplevel(self.window)
    #
    #     login2.Login(dd)

    def update(self):
        selected_item = self.item_tree.selection()[0]
        self.item_index = self.item_tree.item(selected_item, 'text')
        item_data = self.item_tree.item(selected_item, 'values')

        if item_data[0] == '':
            messagebox.showerror('error', 'select a row')
        else:
            if form2.Item_dlt().update_items(item_data[0],self.ent_where.get(),
                          self.ent_to.get(),
                          self.ent_dpt.get_date(),
                          self.txt_combo.get(),
                          self.ent_count.get(),
                          self.txt_classcombo.get(),

                          self.txt_flight.get(),



                          self.ent_price.get(),
                        self.user_id
                        ):
                messagebox.showinfo("Item", "Booking Updated")
                self.show_in_treeview()

            else:
                messagebox.showerror("Error", "Booking Details cannot be added")



    def book_flight(self):
        if self.ent_where.get() == "" or self.ent_to.get() == "" or self.ent_dpt.get() == ""  or self.txt_combo.get() == "" or self.ent_count.get() == "" or self.txt_classcombo.get() == "":
            messagebox.showerror('Error', 'please enter all required fields')

        else:

            try:

                form2.oneway_flight().oneway_reg(self.ent_where.get(),
                          self.ent_to.get(),
                          self.ent_dpt.get_date(),
                          self.txt_combo.get(),
                          self.ent_count.get(),
                          self.txt_classcombo.get(),
                          self.user_id,
                          self.txt_flight.get(),

                          self.ent_price.get()
                        )

                messagebox.showinfo('success', 'Register successfull', parent=self.window)
                self.show_in_treeview()

                #self.clear()
            except Exception as e:
                messagebox.showerror('error', f'error:{str(e)}', parent=self.window)

    def fetch_data(self,*args):

        va = filter(lambda x: x.get('name') == self.txt_classcombo.get(), self.list2)


        self.ent_price.delete(0,END)
        self.ent_price.insert(0,next(va).get('price'))
    def select_item(self, event):
        selected_item=self.item_tree.selection()[0]
        self.item_index=self.item_tree.item(selected_item,'text')
        item_data = self.item_tree.item(selected_item, 'values')


        self.ent_where.delete(0, END)
        self.ent_where.insert(0, item_data[1])
        self.ent_to.delete(0, END)
        self.ent_to.insert(0, item_data[2])

        #dpt_date_f=datetime.datetime.strptime(int(item_data[2]/3), '%Y-%m-%d').strftime('%m/%d/%y')

        dpt_date = datetime.datetime(int(item_data[3][0:4]), int(item_data[3][5:7]), int(item_data[3][8:10]))
        dpt_date_f = dpt_date.strftime('%m/%d/%y')




        self.ent_dpt.set_date(dpt_date_f)

        self.txt_combo.set(item_data[4])
        self.txt_combo.current()

        self.ent_count.delete(0, END)
        self.ent_count.insert(0, item_data[5])
        self.txt_classcombo.set(item_data[6])
        self.txt_classcombo.current()



        self.txt_flight.set(item_data[8])
        self.txt_flight.current()
        self.ent_price.delete(0,END)
        self.ent_price.insert(0,item_data[9])


    def show_in_treeview(self):
        #
        # qry = 'select * from oneway where user_id=%s'
        # self.my_cursor.execute(qry,(self.user_id))
        row = form2.show_flight().show_in_treeview(self.user_id)
        # spot_marker = 0
        # while spot_marker < len(row):
        #     for num in range(spot_marker, len(row)):
        #         if row[num] < row[spot_marker]:
        #             row[spot_marker], row[num] = row[num], row[spot_marker]
        #     spot_marker += 1
        #     print(row)
        if row:

            self.item_tree.delete(*self.item_tree.get_children())

            for i in row:
                #self.tree.item(idx)['text']

                self.item_tree.insert("", "end", text=i[0], value=(i[0],i[1], i[2], i[3], i[4], i[5], i[6],i[7],i[8],i[9]))
            # self.my_connection.commit()
        self.item_tree.bind('<Double-1>', self.select_item)
    def Search_items(self):
        con=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='register'

        )
        cur=con.cursor()
        values = (str(self.search_by.get()), '"{}"'.format(str(self.search_txt.get()+'%')), )
        qry=(f"SELECT ID,destination,source,dpt,combo,count_no,class_selection,user_id,flight_name,price FROM oneway WHERE user_id={self.user_id} AND {values[0]} LIKE {values[1]}  ")



        cur.execute(qry)
        rows=cur.fetchall()

        if len(rows)!=0:
            self.item_tree.delete(*self.item_tree.get_children())

            for row in rows:
                self.item_tree.insert("",END,values=row)
            con.commit()

    def valid(self):

        if self.ent_where.get() == "" or self.ent_to.get() == "" or self.ent_dpt.get() == "" or self.txt_combo.get() == "" or self.ent_count.get() == "" or self.txt_classcombo.get() == "":
            messagebox.showerror('Error', 'please enter all required fields')

            return False

        else:
            return True

    def delete_item(self):
        selected_item = self.item_tree.selection()[0]

        item_data = self.item_tree.item(selected_item, 'text')



        index = item_data
        if form2.Item_dlt().delete_items(index):
            messagebox.showinfo('Item', 'Item Deleted')
            self.show_in_treeview()

            # selected_item = self.item_tree.selection()
            # self.item_tree.delete(selected_item)

        else:
            messagebox.showerror("Error", "Item cannot be deleted",parent=self.window)




    def generate_bill(self):
        all_orders=self.item_tree.get_children()
        bill_list=[]
        total=0
        # tbl=self.order_tree.item(all_orders[0],'values')[0]
        # name=self.order_tree.item(all_orders[1],'values')[1]
        for i in all_orders:
            order=self.item_tree.item(i,'values')
            amt=float(order[5])*float(order[9])
            bill_list.append((order[2],order[3],order[4],order[5],order[6],order[8],order[9],amt))
            total+=amt
        BillView(bill_list, total, self.user)

class BillView:
    def __init__(self,bill_list,total,user):
        self.window=Tk()

        self.window.title('Bill')
        self.window.geometry('800x700')
       

        self.item_tree = ttk.Treeview(self.window, column=('Destination', 'Departure Date','Age Selection','Count','Class Selection','User_id','Price','Amout'))
        self.item_tree.grid(row=3, column=0, columnspan=2)
        self.item_tree['show'] = 'headings'


        self.item_tree.column('Destination', width=100)
        self.item_tree.column('Departure Date', width=100)

        self.item_tree.column('Age Selection', width=100)
        self.item_tree.column('Count', width=100)
        self.item_tree.column('Class Selection', width=100)
        self.item_tree.column('User_id', width=100)
        self.item_tree.column('Price', width=100)

        self.item_tree.column('Amout', width=100)


        self.item_tree.heading('Destination', text="Destination")
        self.item_tree.heading('Departure Date', text="Departure Date")

        self.item_tree.heading('Age Selection', text="Age Selection")
        self.item_tree.heading('Count', text="Count")
        self.item_tree.heading('Class Selection', text="Class Selection")
        self.item_tree.heading('User_id', text="User ID")
        self.item_tree.heading('Price', text="Price")
        self.item_tree.heading('Amout', text="Amout")
        for i in bill_list:
            self.item_tree.insert('','end',text='',value=i)
        self.item_tree.insert('','end',text='',value=('Total','','','','','','',total))
        self.window.mainloop()




window = Tk()
ob = oneway(8,window)
window.mainloop()