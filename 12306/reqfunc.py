import requests
from bs4 import BeautifulSoup

class Login(object):
    def __init__(self,user,passwd):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
        self.positions = ['36,46', '109,44', '181,47', '254,44', '33,112', '105,116', '186,116', '253,115']
        self.vcode_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.5579044251920726'
        self.verify_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
        self.login_url = 'https://kyfw.12306.cn/passport/web/login'
        self.user = user
        self.passwd = passwd
        self.headers = {}
        self.session = requests.Session()

    def login(self):
        pass


    def query(self):
        pass

    def qianpiao(self):
        pass



