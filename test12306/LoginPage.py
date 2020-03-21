from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
from test12306.mainpage import MainPage
#from .reqfunc import *

class LoginPage():
    def __init__(self,master):
        self.root = master
        self.root.geometry('%dx%d' % (300, 180))
        self.username = StringVar()
        self.passwd = StringVar()
        self.initpage()

    def initpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page).grid(row=0,stick=W)
        Label(self.page,text="账户：").grid(row=1,column=0,stick=W,pady=10)
        Entry(self.page,textvariable = self.username).grid(row=1,column=1,stick=E)
        Label(self.page,text="密码：").grid(row=2,column=0,pady=10,stick=W)
        Entry(self.page,textvariable=self.passwd,show="*").grid(row=2,column=1,stick=E)
        Label(self.page).grid(row=3,stick=W)
        Button(self.page,text="登陆",command = self.login).grid(row=4,pady=10,stick=W)
        Button(self.page,text="退出",command = self.page.quit).grid(row=4,column=1,stick=E)

    def login(self):
        """
            login check

        """
        #session,flag = Login.login()
        self.page.destroy()
        MainPage(self.root)









if __name__ == "__main__":
    tk = Tk()
    tk.title("12306Buy")
    LoginPage(tk)
    tk.mainloop()
