from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

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
        Label(self.page,text="账户：").grid()
        Entry(self.page,textvariable = self.username).grid()
        Label().grid()
        Entry().grid()
        Button(self.page,text="登陆",command = self.login).grid()
        Button().grid()

    def login(self):
        pass








if __name__ == "__main__":
    tk = Tk()
    tk.title("12306")
    LoginPage(tk)
    tk.mainloop()
