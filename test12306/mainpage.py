from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from test12306.webfunc import *

class MainPage(object):
    def __init__(self,master):
        self.root = master
        self.root.geometry("%dx%d" % (650, 500))
        #查询用
        self.starting = StringVar()
        self.target = StringVar()
        self.Sdate = StringVar()
        self.Ttype = set()
        #抢票用
        self.passenger = StringVar()
        self.Tnum = StringVar()

        self.initpage()

    def initpage(self):
        """self.Upframe = Frame(self.root)
        self.Downframe = Frame(self.root)
        Label(self.Upframe).grid(row=0)
        Label(self.Upframe,text="出发地:").grid(row=1,column=0)
        Entry(self.Upframe,textvariable=self.starting,width=10).grid(row=1,column=1,padx=20,)
        Label(self.Upframe,text="目的地:").grid(row=1,column=2,stick=E)
        Entry(self.Upframe,textvariable=self.target,width=10).grid(padx=20,row=1,column=3,stick=W)
        Label(self.Upframe,text="出发日期:").grid(row=1,column=4,stick=E)
        Entry(self.Upframe,textvariable=self.Sdate,width=10).grid(padx=20,row=1,column=5,stick=W)
        self.Upframe.pack(side=TOP)
        self.Downframe.pack(side=BOTTOM)"""

        #查询按键
        self.query = Button(self.root,text="查询",width=10,height=2,bg='skyblue',command=self.query_button).place(relx=0.70,rely=0.12,anchor=CENTER)
        #抢票按键
        self.buy = Button(self.root,text="抢票",width=10,height=2,bg='skyblue',command=self.buy_button).place(rely=0.12,relx=0.90,anchor=CENTER)
        #显示查询结果框
        #self.text_show=Text(self.root,bd=4,relwidth=90,height=28,font=('楷体',10))
        self.text_show = Text(self.root, bd=4, width=90, height=28, font=('楷体', 10))
        self.text_show.place(relx=0.50,rely=0.60,relwidth=0.9,relheight=0.7,anchor=CENTER)
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
        self.varlist = ["G","C", "D ", "Z ", "T ", "K "]
        self.var=[]
        for i,value in enumerate(self.varlist):
            self.var.append(IntVar())
            Checkbutton(self.root,text=value,variable=self.var[i],onvalue=1,offvalue=0,command=self.select_type).place(relx=0.10+(i+1)*0.07,rely=0.15,anchor=CENTER)


        #车次（抢票用）
        Label(self.root,text="乘客(抢票用):",font=('楷体',12)).place(relx=0.10,rely=0.20,anchor=CENTER)
        Entry(self.root,textvariable=self.passenger,width=10).place(relx=0.25,rely=0.20,anchor=CENTER)
        Label(self.root,text="车次(抢票用):",font=('楷体',12)).place(relx=0.40,rely=0.20,anchor=CENTER)
        Entry(self.root,textvariable=self.Tnum,width=10).place(relx=0.55,rely=0.20,anchor=CENTER)


    def select_type(self):
        for i in range(len(self.varlist)):
#            print(self.var[i].get())
            if self.var[i].get()==1:
                self.Ttype.add(self.varlist[i])
            else:
                self.Ttype.remove(self.varlist[i])


    def query_button(self):
       # print(self.Sdate,self.starting,self.target)
        print(self.Ttype)
        status,result=Query(self.Sdate.get(),self.starting.get(),self.target.get(),self.Ttype).query()
        if status:
            self.show_query_txt(result)
        else:
            messagebox.showerror(result)

    def show_query_txt(self,res):
        print(res)
        for train in res:
            print(tuple(train))
            text = "%-5s  %-11s  %-12s  %-5s  %-2s %-2s %-2s %-2s %-2s %-2s %-2s %-2s %-2s %-2s"% tuple(train)
            print(text)
            self.text_show.insert(END,text)
            self.text_show.insert(END,"\n")


    def buy_button(self):
        pass

if __name__ == "__main__":
    root=Tk()
    root.title("BuyTrain")
    MainPage(root)
    mainloop()