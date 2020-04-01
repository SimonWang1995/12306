from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from test12306.WebFun.queryTrains import *
import requests

class MainPage(object):
    def __init__(self,master,session=requests.session()):
        self.root = master
        self.root.geometry("%dx%d" % (800, 600))
        self.session = session
        #查询用
        self.headers = "车次 车站 时间 历时 商务/特等座 一等座 二等座 高级软卧 软卧 动卧 硬卧 软座 硬座 无座".split()
        self.starting = StringVar()
        self.target = StringVar()
        self.Sdate = StringVar()
        self.Ttype = set()
        #抢票用
        self.passenger = StringVar()
        self.Tnum = StringVar()
        self.initpage()


    def initpage(self):
        #查询按键
        self.query = Button(self.root,text="查询",width=10,height=2,bg='skyblue',command=self.query_button).place(relx=0.70,rely=0.12,anchor=CENTER)
        #抢票按键
        self.buy = Button(self.root,text="抢票",width=10,height=2,bg='skyblue',command=self.buy_button).place(rely=0.12,relx=0.90,anchor=CENTER)
        #显示查询结果框
        # self.text_show = Text(self.root, bd=4, width=90, height=28, font=('楷体', 10))
        # self.text_show.place(relx=0.50,rely=0.60,relwidth=0.9,relheight=0.7,anchor=CENTER)
        self.page = Frame(self.root)
        self.scrollbar = Scrollbar(self.page)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.text_show = ttk.Treeview(self.page,show="headings",columns=self.headers,yscrollcommand=self.scrollbar.set)
        self.init_show()
        self.scrollbar.config(command=self.text_show.yview)
        self.text_show.pack(expand=YES,fill=BOTH)
        self.page.place(relx=0.50, rely=0.60, relwidth=0.9, relheight=0.7, anchor=CENTER)
        #输入乘客信息
        Label(self.root,text="出发地:",font=('楷体',12)).place(relx=0.10,rely=0.05,anchor=CENTER)
        Entry(self.root,textvariable=self.starting,width=10).place(relx=0.10,rely=0.10,anchor=CENTER)
        Label(self.root,text="目的地:",font=('楷体',12)).place(relx=0.25,rely=0.05,anchor=CENTER)
        Entry(self.root,textvariable=self.target,width=10).place(relx=0.25,rely=0.10,anchor=CENTER)
        Label(self.root,text="日期 :",font=('楷体',12)).place(relx=0.40,rely=0.05,anchor=CENTER)
        Entry(self.root,textvariable=self.Sdate,width=10).place(relx=0.40,rely=0.10,anchor=CENTER)
        #车票类型（查询用）
        Label(self.root,text="车票类型:",font=('楷体',12)).place(relx=0.10,rely=0.15,anchor=CENTER)
        #self.varlist=["GC-高铁/城际","D-动车","Z-直达","T-特快","K-快速","其他"]
        self.varlist = ["G","C", "D", "Z", "T", "K"]
        self.var=[]
        for i,value in enumerate(self.varlist):
            self.var.append(IntVar())
            Checkbutton(self.root,text=value,variable=self.var[i],onvalue=1,offvalue=0).place(relx=0.10+(i+1)*0.07,rely=0.15,anchor=CENTER)


        #车次（抢票用）
        Label(self.root,text="乘客(抢票用):",font=('楷体',12)).place(relx=0.10,rely=0.20,anchor=CENTER)
        Entry(self.root,textvariable=self.passenger,width=10).place(relx=0.25,rely=0.20,anchor=CENTER)
        Label(self.root,text="车次(抢票用):",font=('楷体',12)).place(relx=0.40,rely=0.20,anchor=CENTER)
        Entry(self.root,textvariable=self.Tnum,width=10).place(relx=0.55,rely=0.20,anchor=CENTER)


    def select_type(self):
        self.Ttype.clear()
        for i in range(len(self.varlist)):
#            print(self.var[i].get())
            if self.var[i].get()==1:
                self.Ttype.add(self.varlist[i])

    def init_show(self):
        wd_list = [50,100,100,50,30,30,30,30,30,30,30,30,30,30]
        for name,v in zip(self.headers,wd_list):
            self.text_show.column(name,width=v,anchor='center')
            self.text_show.heading(name,text=name)

    def clear_txt(self):
        items = self.text_show.get_children()
        for i in items:
            self.text_show.delete(i)

    def query_button(self):
       # print(self.Sdate,self.starting,self.target)
        self.clear_txt()
        self.select_type()
        print(self.Ttype)
        status,result=Query(self.session).query(self.Sdate.get(),self.starting.get(),self.target.get(),self.Ttype)
        if status:
            self.show_query_txt(result)
        else:
            messagebox.showerror(message=result)

    def show_query_txt(self,res):
        print(res)
        for i,train in enumerate(res):
            print(tuple(train))
            text = tuple(train)
            print(text)
            self.text_show.insert('',i,value=text)



    def buy_button(self):
        pass

if __name__ == "__main__":
    root=Tk()
    root.title("BuyTrain")
    MainPage(root)
    mainloop()