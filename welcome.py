from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import datetime
import Oneway
import form


import mysql.connector


class welcome:

    def __init__(self,user, window):
        self.window = window
        self.user_id =user
        self.user = user
        self.window.title('User Form')
        self.item_index=[]


        self.my_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='register'

        )
        self.my_cursor = self.my_connection.cursor()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.list2 = [{'name': 'Economy', 'price': 3000}, {'name': 'Premium Economy', 'price': 4000},
                      {'name': 'Business Class', 'price': 5000}, {'name': 'First Class', 'price': 6000}]
        # Get the names of the all flights name

        self.names = list(map(lambda x: x.get('name'), self.list2))

        self.window.geometry('1100x700+90+40')
        self.window.resizable(0, 0)
        self.bg = ImageTk.PhotoImage(file='C:\\Users\\Dell\\PycharmProjects\\untitled3\\project\\Webp.net-resizeimage (4).jpg')
        self.bg_Image = Label(self.window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.frame1 = Frame(self.window, bg='white')
        self.frame1.place(x=100, y=30, height=700, width=900)
        self.frame2 = Frame(self.frame1, bg='lightgrey')
        self.frame2.place(x=0, y=60, height=55, width=900)
        self.label_name = Label(self.frame1, text="Book Flights",font=('Impact', 20, 'bold'), fg="#d77337", bg='white')
        self.label_name.place(x=300, y=15)
        self.btn_return = Button(self.frame1, text="Return",relief=RAISED, bg='lightgrey', font=('arial', 14, 'bold'),
                           fg='black',bd=0)
        self.btn_return.place(x=90,y=70)
        self.btn_oneway = Button(self.frame1, text="One way",relief=RAISED, bg='lightgrey', font=('arial', 14, 'bold'),
                           fg='black',bd=0,command=self.open)
        self.btn_oneway.place(x=300,y=70)
        self.btn_exit = Button(self.frame1, text="Exit", relief=RAISED, bg='lightgrey', font=('arial', 14, 'bold'),
                              fg='red',bd=0,command=exit)
        self.btn_exit.place(x=510, y=70,width=100)
        self.label_where = Label(self.frame1, text="Where From:", font=('Goudy old style', 12, 'bold'), fg='grey',
                             bg='white')
        self.label_where.place(x=60, y=130)
        self.ent_where = Entry(self.frame1, font=('times new roman', 9), bg='lightgray')
        self.ent_where.place(x=170, y=130, width=200, height=30)
        self.label_to = Label(self.frame1, text="Where To:", font=('Goudy old style', 12, 'bold'), fg='grey',
                                bg='white')
        self.label_to.place(x=390, y=130)
        self.ent_to = Entry(self.frame1, font=('times new roman', 9), bg='lightgray')
        self.ent_to.place(x=490, y=130, width=200, height=30)
        self.label_dpt = Label(self.frame1, text="Departure Date:", font=('Goudy old style', 12, 'bold'), fg='grey',
                                bg='white')
        self.label_dpt.place(x=50, y=180)

        self.ent_dpt=DateEntry(self.frame1, width=12, background='darkblue',
                        foreground='white',state='readonly', borderwidth=2)
        self.ent_dpt.place(x=170, y=180,width=200)
        ttk.Button(self.frame1, text="ok")

        # self.ent_dpt = Entry(self.frame1, font=('times new roman', 9), bg='lightgray')
        # self.ent_dpt.place(x=170, y=200, width=200, height=30)
        self.label_date = Label(self.frame1, text="Return date:", font=('Goudy old style', 12, 'bold'), fg='grey',
                                bg='white')
        self.label_date.place(x=390, y=180)
        self.ent_date = DateEntry(self.frame1, width=12, background='darkblue',
                                 foreground='white',state='readonly', borderwidth=2)
        self.ent_date.place(x=490, y=180,width=200)
        ttk.Button(self.frame1, text="ok")

        self.combo = Label(self.frame1, text='Age Selection', font=('Goudy old style', 12, 'bold'), bg='white',
                        fg='gray').place(x=50, y=230)
        self.txt_combo = ttk.Combobox(self.frame1, font=('times new roman', 9), state='readonly', justify=CENTER)
        self.txt_combo['values'] = ('Adult', 'Children', 'Infant', 'Old age')
        self.txt_combo.place(x=170, y=230, width=200)
        self.txt_combo.current(0)
        self.label_count = Label(self.frame1, text="Count:", font=('Goudy old style', 12, 'bold'), fg='grey',
                                bg='white')
        self.label_count.place(x=390, y=230)
        self.ent_count = Entry(self.frame1, font=('times new roman', 9), bg='lightgray')
        self.ent_count.place(x=490, y=230, width=200, height=30)
        self.classcombo = Label(self.frame1, text="Class Selection:", font=('Goudy old style', 12, 'bold'), fg='grey',
                              bg='white').place(x=50, y=280)
        self.txt_classcombo = ttk.Combobox(self.frame1, font=('times new roman', 9), state='readonly', justify=CENTER,
                                          values=self.names)
        self.txt_classcombo['values'] = ('Economy', 'Premium Economy', 'Business Class', 'First Class')
        self.txt_classcombo.bind('<<ComboboxSelected>>', self.fetch_data)

        self.txt_classcombo.place(x=170, y=280)
        self.txt_classcombo.current(0)
        self.label_price = Label(self.frame1, text="Price:", font=('Goudy old style', 12, 'bold'), fg='grey',
                                 bg='white')
        self.label_price.place(x=390, y=280)
        self.flight = Label(self.frame1, text="Flight Selection:", font=('Goudy old style', 12, 'bold'), fg='grey',
                            bg='white').place(x=50, y=320)
        self.txt_flight = ttk.Combobox(self.frame1, textvariable=self.search_by,font=('times new roman', 9), state='readonly', justify=CENTER)
        self.txt_flight['values'] = ('Buddha Air', 'Yeti Airlines', 'Surya Airline', 'Nepal Airlines', 'Tara Airlines')

        self.txt_flight.place(x=170, y=320)
        self.txt_flight.current(0)
        self.ent_price = Entry(self.frame1,textvariable=self.search_txt, font=('times new roman', 9), bg='lightgray')
        self.ent_price.place(x=490, y=280, width=200, height=30)
        self.ent_price.insert(0, '3000')
        self.txt_search=Entry(self.frame1,font=('times new roman',9))
        self.txt_search.place(x=400,y=320)
        self.combo_search=ttk.Combobox(self.frame1,font=('times new roman', 9), state='readonly', justify=CENTER)
        self.combo_search['values'] = ('flight_name', 'destination', 'source')
        self.combo_search.place(x=550,y=320)

        self.combo_search.current(0)
        self.btn_add = Button(self.frame1, text="Search", command=self.Search_Items)
        self.btn_add.place(x=710, y=320)

        self.btn_book = Button(self.frame1, text="Book Flight", relief=RAISED, bg='green', font=('arial', 14, 'bold'),
                                 fg='white',command=self.book_flight)
        self.btn_book.place(x=50, y=590)
        self.btn_book = Button(self.frame1, text="Cancel Flight", relief=RAISED, bg='red', font=('arial', 14, 'bold'),
                               fg='white',command=self.delete_item)
        self.btn_book.place(x=220, y=590)
        self.book_tree = ttk.Treeview(self.frame1, columns=('ID','Where from', 'Where to', 'Departure Time','Return Date','Age Selection','Count','User_id','Price','Flight_Name'))
        self.book_tree.place(x=50,y=360)
        self.btn_book = Button(self.frame1, text="Bill", relief=RAISED, bg='red', font=('arial', 14, 'bold'),
                               fg='white', command=self.generate_bill)
        self.btn_book.place(x=400, y=590)
        self.btn_update = Button(self.frame1, text="Update", relief=RAISED, bg='red', font=('arial', 14, 'bold'),
                               fg='white', command=self.update)
        self.btn_update.place(x=600, y=590)
        # self.book_entry = Entry(self.frame1)
        # self.book_entry.grid(row=60, column=300)


        self.book_tree['show'] = 'headings'
        self.book_tree.column('ID', width=80)

        self.book_tree.column('Where from', width=80)
        self.book_tree.column('Where to', width=80)
        self.book_tree.column('Departure Time', width=80)
        self.book_tree.column('Return Date', width=80)
        self.book_tree.column('Age Selection', width=80)
        self.book_tree.column('Count', width=80)
        self.book_tree.column('User_id', width=80)
        self.book_tree.column('Price', width=80)
        self.book_tree.column('Flight_Name', width=80)
        self.book_tree.heading('ID', text="ID")
        self.book_tree.heading('Where from', text="Where from")
        self.book_tree.heading('Where to', text="Where to")
        self.book_tree.heading('Departure Time', text="Departure Time")
        self.book_tree.heading('Return Date', text="Return Date")
        self.book_tree.heading('Age Selection', text="Age Selection")
        self.book_tree.heading('Count', text="Count")
        self.book_tree.heading('User_id', text="User Id")
        self.book_tree.heading('Price', text="Price")
        self.book_tree.heading('Flight_Name', text="Flight_Name")
        self.show_in_treeview()
    def clear(self):
        self.ent_where.delete(0,END)
        self.ent_to.delete(0,END)
        self.ent_dpt.delete(0, END)
        self.ent_date.delete(0, END)
        self.txt_combo.set('')
        self.ent_count.delete(0, END)

    def update(self):
        selected_item = self.book_tree.selection()[0]
        self.item_index = self.book_tree.item(selected_item, 'text')
        item_data = self.book_tree.item(selected_item, 'values')

        if item_data[0] == '':
            messagebox.showerror('error', 'select a row')
        else:
            if form.Item_dlt().update_items(item_data[0],self.ent_where.get(),
                          self.ent_to.get(),
                                            self.ent_dpt.get_date(),
                                            self.ent_date.get_date(),
                                            self.txt_combo.get(),
                                            self.ent_count.get(),

                                            self.txt_flight.get(),

                                            self.ent_price.get(),
                                            self.user_id
                                             ):
                messagebox.showinfo("Item", "Item Updated")
                self.show_in_treeview()

            else:
                messagebox.showerror("Error", "Item cannot be added")

    def book_flight(self):

        if self.ent_where.get()== "" or self.ent_to.get()== "" or self.ent_dpt.get()== "" or self.ent_date.get()== "" or self.txt_combo.get()== "" or self.ent_count.get()== "":
            messagebox.showerror('Error','please enter all required fields')

        else:

            try:

                form.return_flight().form_reg(self.ent_where.get(),
                          self.ent_to.get(),
                          self.ent_dpt.get_date(),
                          self.ent_date.get_date(),
                          self.txt_combo.get(),
                          self.ent_count.get(),
                          self.user_id,
                          self.ent_price.get(),
                          self.txt_flight.get())

                messagebox.showinfo('success', 'Register successfull', parent=self.window)
                self.show_in_treeview()
                self.clear()
            except Exception as e:
                messagebox.showerror('error', f'error:{str(e)}', parent=self.window)

    def show_in_treeview(self):
        try:


            row= form.return_flight().show_in_treeview(self.user_id)
            if len(row):


                self.book_tree.delete(*self.book_tree.get_children())

                for i in row:
                    self.book_tree.insert("", "end", text=i[0], value=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
                # self.my_connection.commit()
            self.book_tree.bind('<Double-1>', self.select_item)
        except Exception as e:
            messagebox.showerror('error', f'error:{str(e)}', parent=self.window)

    def select_item(self, event):
        selected_item=self.book_tree.selection()[0]
        self.item_index=self.book_tree.item(selected_item,'text')
        item_data = self.book_tree.item(selected_item, 'values')
        dpt_date = datetime.datetime(int(item_data[3][0:4]), int(item_data[3][5:7]), int(item_data[3][8:10]))
        dpt_date_f = dpt_date.strftime('%m/%d/%y')

        return_date = datetime.datetime(int(item_data[4][0:4]), int(item_data[4][5:7]), int(item_data[4][8:10]))
        return_date_f = return_date.strftime('%m/%d/%y')

        self.ent_where.delete(0, END)
        self.ent_where.insert(0, item_data[1])
        self.ent_to.delete(0, END)
        self.ent_to.insert(0, item_data[2])

        self.ent_dpt.set_date(dpt_date_f)
        #self.ent_dpt.current()
        self.ent_date.set_date(return_date_f)
        #self.ent_date.current()
        self.txt_combo.set(item_data[5])
        self.txt_combo.current()
        self.ent_count.delete(0, END)
        self.ent_count.insert(0, item_data[6])
        self.txt_classcombo.set(item_data[7])
        self.txt_classcombo.current()

        self.ent_price.delete(0, END)
        self.ent_price.insert(0, item_data[8])

        self.txt_flight.set(item_data[9])
        self.txt_flight.current()

    def fetch_data(self,*args):

        va = filter(lambda x: x.get('name') == self.txt_classcombo.get(), self.list2)


        self.ent_price.delete(0,END)
        self.ent_price.insert(0,next(va).get('price'))
    def open(self):

        self.window.withdraw()
        dd = Toplevel(self.window)
        Oneway.oneway(self.user_id, dd)
    def Search_Items(self):
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='register'

        )
        cur = con.cursor()
        values = (str(self.search_by.get()), '"{}"'.format(str(self.search_txt.get() + '%')),)
        qry = (f"SELECT id,destination,source,dpt,date,combo,count_no,user_id,price,flight_name FROM book_flight WHERE user_id={self.user_id} AND {values[0]} LIKE {values[1]}")
        cur.execute(qry)
        rows = cur.fetchall()

        if len(rows) != 0:
            self.book_tree.delete(*self.book_tree.get_children())

            for row in rows:
                self.book_tree.insert("", END, values=row)
            con.commit()
    def delete_item(self):
        selected_item = self.book_tree.selection()[0]

        item_data = self.book_tree.item(selected_item, 'text')

        index = item_data
        if form.Item_dlt().delete_items(index):
            messagebox.showinfo('Item', 'Item Deleted')
            self.show_in_treeview()

            # selected_item = self.item_tree.selection()
            # self.item_tree.delete(selected_item)

        else:
            messagebox.showerror("Error", "Item cannot be deleted",parent=self.window)


    def generate_bill(self):
        all_orders = self.book_tree.get_children()
        bill_list = []
        total = 0
        # tbl=self.order_tree.item(all_orders[0],'values')[0]
        # name=self.order_tree.item(all_orders[1],'values')[1]
        for i in all_orders:
            order = self.book_tree.item(i, 'values')
            amt = float(order[5]) * float(order[7])
            bill_list.append((order[1], order[2], order[3], order[4], order[5], order[6], order[7], amt))
            total += amt
        BillView(bill_list, total, self.user)

class BillView:
    def __init__(self, bill_list, total, user):
        self.window = Tk()

        self.window.title('Bill')
        self.window.geometry('800x700')

        self.book_tree = ttk.Treeview(self.window, column=('Destination', 'Departure Date', 'Return Date', 'Age Selection', 'Count', 'User_id', 'Price', 'Amount'))
        self.book_tree.grid(row=3, column=0, columnspan=2)
        self.book_tree['show'] = 'headings'

        self.book_tree.column('Destination', width=100)
        self.book_tree.column('Departure Date', width=100)
        self.book_tree.column('Return Date', width=100)

        self.book_tree.column('Age Selection', width=100)
        self.book_tree.column('Count', width=100)

        self.book_tree.column('User_id', width=100)
        self.book_tree.column('Price', width=100)

        self.book_tree.column('Amount', width=100)

        self.book_tree.heading('Destination', text="Destination")
        self.book_tree.heading('Departure Date', text="Departure Date")
        self.book_tree.heading('Return Date', text="Return Date")

        self.book_tree.heading('Age Selection', text="Age Selection")
        self.book_tree.heading('Count', text="Count")

        self.book_tree.heading('User_id', text="User ID")
        self.book_tree.heading('Price', text="Price")
        self.book_tree.heading('Amount', text="Amount")
        for i in bill_list:
            self.book_tree.insert('', 'end', text='', value=i)
        self.book_tree.insert('', 'end', text='', value=('Total', '', '', '', '','','',total))
        self.window.mainloop()


window = Tk()
ob = welcome(8,window)
window.mainloop()
