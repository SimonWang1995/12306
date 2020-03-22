from test12306.Utils.misc import *
import requests
import time,os

class login12306():
    def __init__(self,session=requests.Session(),**kwargs):
        self.__name  = 'login12306'
        self.cur_path = os.getcwd()
        self.session = session

    '''登录函数'''
    def get_vcode(self):
        self.__initializePC()
        self.__downloadVcode()

    def login(self,username,password,vcode_num,crackvcFunc=None):
        res = self.__verifyVcode(vcode_num,crackvcFunc)
        if not res:
            raise RuntimeError('verification code error...')
        data = {
            'username': username,
            'password': password,
            'appid': 'otn'
        }
        res = self.session.post(self.login_url, headers=self.headers, data=data)
        if res.status_code == 200:
            print('[INFO]: Account -> %s, login successfully...' % username)
            infos_return = {'username': username}
            return infos_return, self.session
        else:
            raise RuntimeError('Account -> %s, fail to login, username or password error...' % username)


    '''下载验证码'''
    def __downloadVcode(self):
        res = self.session.get(self.vcode_url, headers=self.headers)
        saveImage(res.content, os.path.join(self.cur_path, 'vcode.jpg'))
        return True

    '''验证码验证'''
    def __verifyVcode(self,vcode_num,crackvcFunc):
        img_path = os.path.join(self.cur_path, 'vcode.jpg')
        if crackvcFunc is None:
            #showImage(img_path)
            verify_list = []
            for each in vcode_num:
                try:
                    verify_list.append(self.positions[each])
                except:
                    raise RuntimeError('verification code error...')
        else:
            verify_list = crackvcFunc(img_path)
        data = {
            'answer': ','.join(verify_list),
            'login_site': 'E',
            'rand': 'sjrand'
        }
        res = self.session.post(url=self.verify_url, headers=self.headers, data=data)
        removeImage(img_path)
        if res.json()['result_code'] == '4':
            return True
        else:
            return False

    '''初始化PC端'''
    def __initializePC(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
        self.positions = ['36,46', '109,44', '181,47', '254,44', '33,112', '105,116', '186,116', '253,115']
        self.vcode_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.5579044251920726'
        self.verify_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
        self.login_url = 'https://kyfw.12306.cn/passport/web/login'

    '''初始化移动端'''

    def __initializeMobile(self):
        pass


if __name__ == "___main__":
    login12306()