import requests
from threading import Thread
from test12306.Utils.Station_Parse import  parse_station
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 忽视该警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Query():
    def __init__(self,session):
        self.url_template = (
            'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.'
            'train_date={0}&'
            'leftTicketDTO.from_station={1}&'
            'leftTicketDTO.to_station={2}&'
            'purpose_codes=ADULT'
        )
        self.session = session


    def get_url(self):
        url = self.url_template.format(self.Train_date,self.from_sta,self.to_sta)
        #print(url)
        return url

    def query(self,Sdate,from_sta,to_sta,train_type=None):
        self.Train_date = Sdate
        self.from_sta = parse_station().parse(from_sta)
        self.to_sta = parse_station().parse(to_sta)
        self.train_type = train_type
        # self.train_type = "GCDT"
        self.init_url = "https://www.12306.cn/index/"
        self.query_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
        self.session.get(url=self.init_url,headers=self.headers)
        self.session.get(url=self.query_url,headers=self.headers)
        self.rep = self.session.get(url=self.get_url(),headers=self.headers,verify=False)
        print(self.rep.text)
        try:
            self.trains = self.rep.json()["data"]["result"]
            self.select_trains()
            # print(self.format_trains)
            return True,self.format_trains
        except:
            print("query failed")
            # raise ("query failed")
            return False,"出了点小问题，请重新点击按钮"

    def select_trains(self):
        self.format_trains = []
        self.list = '车次： 车站： 时间： 历时： 商务/特等座： 一等座： 二等座： 高级软卧： 软卧： 动卧： 硬卧： 软座： 硬座： 无座：'.split()
        for train in self.trains:
            # format_train=[]
            train_list = train.split('|')
            #print(train_list)
            thread_list=[]
            if self.train_type:
                if str(train_list[3][0]) in self.train_type:
                    print(train_list[3][0], self.train_type)
                    # self.train_format(train_list)
                    t = Thread(target=self.train_format,args=(train_list,))
                    # t.setDaemon(True)
                    thread_list.append(t)
                    t.start()
            else:
                # self.train_format(train_list)
                t = Thread(target=self.train_format, args=(train_list,))
                # t.setDaemon(True)
                thread_list.append(t)
                t.start()
            for t in thread_list:
                t.join()


    def train_format(self,train_list):
        print(train_list)
        format_train=[]
        format_train.append(train_list[3])
        format_train.append(parse_station().disparse(train_list[6])+"->"+parse_station().disparse(train_list[7]))
        format_train.append(train_list[8]+"->"+train_list[9])
        format_train.append(train_list[10])
        format_train.append(train_list[32] or "--")
        format_train.append(train_list[31] or "--")
        format_train.append(train_list[30] or "--")
        format_train.append(train_list[21] or "--")
        format_train.append(train_list[23] or "--")
        format_train.append(train_list[33] or "--")
        format_train.append(train_list[28] or "--")
        format_train.append(train_list[24] or "--")
        format_train.append(train_list[29] or "--")
        format_train.append(train_list[26] or "--")
        print(format_train)
        self.format_trains.append(format_train)




