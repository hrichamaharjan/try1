

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
class Login(Db_Connection):
    def __init__(self):
        super(Login,self).__init__()

    def login_user(self, email, password):
        try:
            qry = ('select * from users where email=%s and password=%s')
            values = (email,password)
            self.my_cursor.execute(qry, values)
            data = self.my_cursor.fetchone()
            self.my_connection.close()
            return data
        except Exception as e:
            print(e)
            return False
class Recover_pw(Db_Connection):
    def __init__(self):
        super().__init__()
    def forget_pw(self,email):
        try:
            qry=('select * from users where email=%s')
            values=(email,)
            self.my_cursor.execute(qry,values)
            data=self.my_cursor.fetchone()

            self.my_connection.close()

            return data
        except Exception as e:
            print(e)
            return False
class Answer_match(Db_Connection):
    def __init__(self):
        super().__init__()
    def check_ans(self,email,question,answer):
        try:
            qry=('select * from users where email=%s and question=%s and answer=%s')
            values=(email,question,answer)
            self.my_cursor.execute(qry,values)
            data=self.my_cursor.fetchall()

            self.my_connection.close()
            return data

        except Exception as e:
            print(e)
            return False
    def update_pw(self,password,email):
        try:

            qry=('update users set password=%s where email=%s ')
            values=(password,email)
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()

            self.my_connection.close()
            return True
        except Exception as e:
            print(e)
            return False
class Register(Db_Connection):
    def __init__(self):
        super().__init__()
    def register_entry(self,fname,lname,contact,email,password,question,answer):
        try:
            qry=('insert into users(f_name,l_name,contact,email,password,question,answer) values(%s,%s,%s,%s,%s,%s,%s)')
            values=(fname,lname,contact,email,password,question,answer,)
            self.my_cursor.execute(qry, values)
            print(contact)

            self.my_connection.commit()

            self.my_connection.close()
            return True
        except Exception as e:
            print(e)
            return False









#
    # def login_user(self,email,password):
    #     qry = ('select * from users where email=%s and password=%s')
    #     values = (email,password)
    #     self.my_cursor.execute(qry, values)
    #     data = self.my_cursor.fetchone()
    #     return data
    # def verify_item(self,email):
    #     qry = ('select * from users where email=%s')
    #     values = (email)
    #     self.my_cursor.execute(qry, values)
    #     data = self.my_cursor.fetchall()
    #     return data
    #

