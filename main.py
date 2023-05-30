import sqlite3
from typing import List
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import date

today = date.today()

db = "user_info.db"


def get_database_connection():
    con = sqlite3.connect(db)
    return con


class Withdraw(Screen):
    def withdraw(self):
        ACCOUNT_NUMBER = self.ids.account_number.text
        AMOUNT = self.ids.amount.text
        CVV = self.ids.cvv.text

        d3 = today.strftime("%m/%d/%y")
        type = "withdraw"
        aaa = ACCOUNT_NUMBER, type, AMOUNT, CVV, d3
        add_data_stmt = ''' INSERT INTO balance(phone, type, amount, cvv, date) VALUES(?,?,?,?,?); '''
        con = get_database_connection()
        con.execute(add_data_stmt, aaa)
        con.commit()
        con.close()


class UserLookup(Screen):
    def press(self):
        name = self.ids.card.text
        cvv = self.ids.cvv.text
        sss = name, cvv
        type_d = "deposit"
        type_w = "withdraw"
        if name == "e":
            return AddUser()
        else:
            sql_query_name = ''' SELECT name FROM info WHERE phone=? AND cvv=?; '''
            sql_query_phone = ''' SELECT phone FROM info WHERE phone=? AND cvv=?; '''
            sql_query_cvv = ''' SELECT cvv FROM info WHERE phone=? AND cvv=?; '''
            con = get_database_connection()
            cur = con.cursor()

            # name
            cur.execute(sql_query_name, sss)
            results_name = cur.fetchall()
            # phone
            cur.execute(sql_query_phone, sss)
            results_phone = cur.fetchall()
            # cvv
            cur.execute(sql_query_cvv, sss)
            results_cvv = cur.fetchall()
            # print(results)
            cur.close()
            con.close()

            ssss = cvv, type_d
            # sql_query_amount = ''' SELECT amount FROM balance '''
            sql_query_bal_deposit = ''' SELECT amount FROM balance WHERE cvv=? AND type=?; '''
            con = get_database_connection()
            cur = con.cursor()

            cur.execute(sql_query_bal_deposit, ssss)
            bal_results = cur.fetchall()
            print(bal_results)

            # --------------------------------- withdraw------------------------------------

            sssw = cvv, type_w
            # sql_query_amount = ''' SELECT amount FROM balance '''
            sql_query_bal_deposit = ''' SELECT amount FROM balance WHERE cvv=? AND type=?; '''
            con = get_database_connection()
            cur = con.cursor()

            cur.execute(sql_query_bal_deposit, sssw)
            with_bal_results = cur.fetchall()
            print(with_bal_results)

            deposit_list = []
            withdrew_list = []

            for i in bal_results:
                deposit_list.append(i)

            for x in with_bal_results:
                withdrew_list.append(x)

            de_re = sum(list(map(sum, list(deposit_list))))
            with_re = sum(list(map(sum, list(withdrew_list))))

            print(f"this is the deposit results {de_re}")
            print(f"this is the withdrawal results {with_re}")

            self.ids.results.text = str((f"""
            Name: {results_name}
            Card Number: {results_phone}
            Balance: $ {de_re - with_re}
            """))



class AddBalance(Screen):
    def add_balance(self):
        ACCOUNT_NUMBER = self.ids.account_number.text
        AMOUNT = self.ids.amount.text
        CVV = self.ids.cvv.text

        d3 = today.strftime("%m/%d/%y")
        type = "deposit"
        aaa = ACCOUNT_NUMBER, type, AMOUNT, CVV, d3
        add_data_stmt = ''' INSERT INTO balance(phone, type, amount, cvv, date) VALUES(?,?,?,?,?); '''
        con = get_database_connection()
        con.execute(add_data_stmt, aaa)
        con.commit()
        con.close()

class AddUser(Screen):
    def new_account(self):
        fname = self.ids.fname.text
        lname = self.ids.lname.text
        card = self.ids.card_n.text
        cvv = self.ids.cvv_n.text

        name = fname, lname

        sss = fname, card, cvv
        add_data_stmt = ''' INSERT INTO info(name, phone, cvv) VALUES(?,?,?); '''
        con = get_database_connection()
        con.execute(add_data_stmt, sss)
        con.commit()
        con.close()


class MainWidget(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        print("starting version 1.0.1.0")
        return kv


if __name__ == "__main__":
    MainApp().run()
