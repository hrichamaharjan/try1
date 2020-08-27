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
class oneway_flight(Db_Connection):
    def __init__(self):
        super().__init__()
    def oneway_reg(self,destination,source,dpt,combo,count_no,class_selection,user_id,flight_name,price):
        qry=('insert into oneway(destination,source,dpt,combo,count_no,class_selection,user_id,flight_name,price) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)')
        values=(destination,source,dpt,combo,count_no,class_selection,user_id,flight_name,price,)
        print(values)
        self.my_cursor.execute(qry, values)

        self.my_connection.commit()
        return True
class show_flight(Db_Connection):
    def __init__(self):
        super().__init__()
    def show_in_treeview(self,user_id):

        qry = ('select * from oneway where user_id=%s')
        values=(user_id,)
        self.my_cursor.execute(qry,values)
        data = self.my_cursor.fetchall()
        return data
class Item_dlt(Db_Connection):
    def __init__(self):
        super().__init__()
    def delete_items(self,index):

        qry = 'delete from oneway where id=%s'
        values = index

        self.my_cursor.execute(qry, (values,))
        # self.my_cursor.executemany(qry, values[])

        self.my_connection.commit()
        return True
    def update_items(self,index,destination,source,dpt,combo,count_no,class_selection,flight_name,price,user_id):
        try:
            qry=f"update oneway set destination='{destination}',source='{source}',dpt='{dpt}',combo='{combo}',count_no='{count_no}',class_selection='{class_selection}',flight_name='{flight_name}',price='{price}' where id='{index}' and user_id='{user_id}'"

            self.my_cursor.execute(qry)
            self.my_connection.commit()
            return True
        except Exception as e:
            print(e)
            return False