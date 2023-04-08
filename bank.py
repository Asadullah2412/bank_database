# bank project

import sys
import sqlite3
import random as r

class customer:
    bank_name = "Welcome to SBI BANK"
    conn = None

    def __init__(self):
        
        self.conn = sqlite3.connect('customer.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("Create table if not exists customer(accno int primary key , name varchar(20),balance int)")
    
    def get_account(self):
        
        accno = r.randint(100001,999999)
        name = input("Enter your Name ")
        balance = int(input("Enter your Balance "))
        
        self.cursor.execute("insert into customer values(?,?,?)",(accno,name,balance))
        self.conn.commit()
        
        print("Hello",name,"your Account got created")
        self.cursor.execute("Select accno from customer where name = '{}'".format(name))

        account_number = self.cursor.fetchone()
        
        for i in account_number:
            print("plz notedown your account number",i)
        sys.exit()

    def deposit(self):
        acno= int(input("Enter your account number "))
        dpst = int(input("enter your amount to deposit "))

        self.cursor.execute("Update customer set balance = balance + {} where accno{}".format(dpst,acno))
        self.conn.commit()

        self.cursor.execute("select balance from customer where accno = {}".format(acno))
        bal = self.cursor.fetchone()
        for i in bal:
            print("Hi after deposit your balance amount is:",i)
    
    def withdraw(self):
        
        acno = int(input("Enter your Account number"))
        wdant = int(input("Enter your amount to withdraw"))
        self.cursor.execute("select balance from customer where accno= {}".format(acno))
        bal = self.cursor.fetchone()
        t = 0
        for i in bal:
            t = int(i)
        if wdant > t:
            print("Sorry insuffucient funds in your account ")
            sys.exit()
        else:
            self.cursor.execute("Update customer set balance = balance-{} where accno ={}".format(wdant,acno))
            self.conn.commit()
        
        self.cursor.execute("select balance from customer where accno ={}".format(acno))
        bal = self.cursor.fetchone()
        for i in bal:
            print("Hi after withdraw your balance amount is :",i)


print("Welcome to ",customer.bank_name)

c1 = customer()

print("Are you existing customer or new customer ")
print("E-Existing \nN-new customer")

option = input("Choose your option >> ")

if option.lower() == 'n':
    c1.get_account()
    

elif option.lower() =='e':
    while True:
        print("D-deposit\nw-withdraw\nE-exit")
        option = input("choose your option")

        if option.lower() == 'd':
            c1.deposit()

        elif option.lower() =='w':
            c1.withdraw()
            print("thank you for banking with us")
            sys.exit()

        else:
            print("Invalid option choose valid option please ")
