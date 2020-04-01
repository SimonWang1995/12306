from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from test12306.WebFun.Login12306 import login12306
from test12306.mainpage import MainPage
from PIL import Image,ImageTk
import time

class LoginPage():
    def __init__(self,master,login):
        self.root = master
        self.root.geometry('%dx%d' % (300, 300))
        self.root.resizable(False,False)
        self.logininit = login
        self.username = StringVar()
        self.passwd = StringVar()
        self.initpage()

    """init login page"""
    def initpage(self):
        self.page = Frame(self.root)
        Label(self.page,text="账户：").place(x=30,y=10,width=50,height=20)
        Entry(self.page,textvariable=self.username).place(x=80,y=10,width=200,height=20)
        Label(self.page,text="密码：").place(x=30,y=40,width=50,height=20)
        Entry(self.page, textvariable=self.passwd,show="*").place(x=80, y=40, width=200, height=20)
        # Canvas_root = Canvas(self.page,width=300,height=200)
        # photo=self.get_image()
        # Canvas_root.create_image(150,100,image=photo)
        # Canvas_root.place(x=1,y=70,width=300,height=200)
        Button(self.page,text="登录",command=self.login).place(x=20,y=270,width=50,height=25)
        Button(self.page,text="退出",command=self.page.quit).place(x=230,y=270,width=50,height=25)
        self.page.place(x=0,y=0,width=300,height=300)
        self.initvcode()

    def initvcode(self):
        global photo
        self.logininit.get_vcode() #获取验证码
        Canvas_root = Canvas(self.page,width=300,height=200)
        photo=self.get_image()
        # Canvas_root.create_image(150,100,image=photo)
        Canvas_root.create_image(150,100, image=photo)
        Canvas_root.place(x=1,y=70,width=300,height=200)
        self.select_list=[]
        for i in range(8):
            self.select_list.append(IntVar())
            x = 36+(i%4)*73
            y = 115+(i//4)*71
            Checkbutton(self.page,variable=self.select_list[i],onvalue=1,offvalue=0).place(x=x,y=y)

    def select_vcode(self):
        selected_num= []
        for i,num in enumerate(self.select_list):
            if num.get() == 1:
                selected_num.append(i)
        print(selected_num)
        return selected_num



    def get_image(self):
        time.sleep(0.1)
        img = Image.open("vcode.jpg")
        #img.show()
        return ImageTk.PhotoImage(img)


    def login(self):
        """
            login check

        """
        code_num = self.select_vcode()
        if not self.username.get():
            showwarning(message="用户名不能为空")
        elif not self.passwd.get():
            showwarning(message="密码不能为空")
        elif len(code_num) == 0:
            showwarning(message="请选择验证码")
        if self.username.get() and self.passwd and len(code_num) != 0:
            try:
                status,session = self.logininit.login(self.username.get(),self.passwd.get(),code_num)
                self.page.destroy()
                MainPage(self.root,session)
            except RuntimeError as e:
                self.initvcode()
                showerror(message=e)



            # try:
            #     self.logininit.login()
            # except:
        #         pass
        #











if __name__ == "__main__":
    tk = Tk()
    tk.title("12306Buy")
    login12306 = login12306()
    LoginPage(tk,login12306)
    tk.mainloop()
