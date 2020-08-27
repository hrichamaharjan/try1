import mysql.connector


#from login2 import *

class Db_Connection:
    def __init__(self):
        self.my_connection = mysql.connector.connect(
            host='localhost',
            user='root',

            password='',
            database='register'

        )
        self.my_cursor = self.my_connection.cursor()
class return_flight(Db_Connection):
    def __init__(self):
        super().__init__()
    def form_reg(self,destination,source,dpt,date,combo,count_no,user_id,price,flight_name):
        qry=('insert into book_flight(destination,source,dpt,date,combo,count_no,user_id,price,flight_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)')
        values=destination,source,dpt,date,combo,count_no,user_id,price,flight_name
        self.my_cursor.execute(qry, values)

        self.my_connection.commit()
        return True
    def show_in_treeview(self,user_id):
        qry=('select * from book_flight where user_id=%s')
        values=(user_id,)
        self.my_cursor.execute(qry,values)
        data = self.my_cursor.fetchall()
        self.my_connection.close()
        return data
class Item_dlt(Db_Connection):
    def __init__(self):
        super().__init__()
    def delete_items(self,index):

        qry = 'delete from book_flight where id=%s'
        values = index

        self.my_cursor.execute(qry, (values,))
        # self.my_cursor.executemany(qry, values[])

        self.my_connection.commit()
        return True
    def update_items(self,index,destination,source,dpt,date,combo,count_no,flight_name,price,user_id):
        try:
            qry=f"update book_flight set destination='{destination}',source='{source}',dpt='{dpt}',date='{date}',combo='{combo}',count_no='{count_no}',price='{price}',flight_name='{flight_name}' where id='{index}' and user_id='{user_id}'"

            self.my_cursor.execute(qry)
            self.my_connection.commit()
            return True
        except Exception as e:
            print(e)
            return False


