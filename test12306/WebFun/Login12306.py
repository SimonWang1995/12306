from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import re,time,base64,os,sys
import subprocess


class login12306():
    def __init__(self,driver):
        self.driver = driver
        self.__initurl = "https://kyfw.12306.cn/otn/resources/login.html"
        self.initlogin()

    def initlogin(self):
        self.driver.get(self.__initurl)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"J-qrImg")))
        except Exception as e:
            print("网络有问题，请稍后再试")
            raise RuntimeError("网络有问题，请稍后再试")

    def login(self,user,passwd,vcode_num):
        self.user_ele = self.driver.find_element(By.ID,"J-userName")
        self.user_ele.clear()
        self.user_ele.send_keys(user)
        self.passwd_ele = self.driver.find_element(By.ID,"J-password")
        self.passwd_ele.clear()
        self.passwd_ele.send_keys(passwd)
        self.moveaction(vcode_num)
        self.submit()


    def verifycode(self,vcodenum):
        """自动验证Vcode"""
        pass

    def moveaction(self,result):
        self.coordinate = [[-105, -20], [-35, -20], [40, -20], [110, -20], [-105, 50], [-35, 50], [40, 50], [110, 50]]
        try:
            Action = ActionChains(self.driver)
            for i in result:
                Action.move_to_element(self.img_element).move_by_offset(self.coordinate[i][0],
                                                                        self.coordinate[i][1]).click()
            Action.perform()
        except Exception as e:
            print(e)
            raise RuntimeError ("Click Vcode failed")

    def showImage(self,img_path):
        if sys.platform.find('darwin') >= 0:
            subprocess.call(['open', img_path])
        elif sys.platform.find('linux') >= 0:
            subprocess.call(['xdg-open', img_path])
        else:
            os.startfile(img_path)
        return True

    def get_QRcode(self,filename="vcode.png"):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"""//*[@id="J-qrImg"]""")))
        except Exception as e:
            print("网络有问题，请稍后再试")
            raise RuntimeError ("网络有问题，请稍后再试")
        QRbase64=self.driver.find_element(By.XPATH, """//*[@id="J-qrImg"]""").get_attribute("src").split(',')[1]
        QRcode = base64.b64decode(QRbase64)
        with open(filename,'wb') as file:
            file.write(QRcode)

    def submit(self):
        self.driver.find_element(By.ID,"J-login").click()
        try:
            WebDriverWait(self.driver,6).until(EC.presence_of_element_located((By.CLASS_NAME,"logout")))
        except Exception as e:
            print(e)
            if self.driver.find_element_by_xpath("""//*[@id="J-login-error"]/span""").text != '':
                raise RuntimeError(self.driver.find_element(By.XPATH,"""//*[@id="J-login-error"]/span""").text)
            raise RuntimeError("登录失败，请重新登录")



    def get_Vcode(self,filename='vcode.png'):
        self.driver.find_element(By.CLASS_NAME,"login-hd-account").click()
        try:

            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.ID, "J-loginImg"))
            )

        except Exception as e:
            print(u"网络开小差,请稍后尝试")
        time.sleep(2)
        img_element = self.driver.find_element(By.ID,"J-loginImg")
        base64_str = img_element.get_attribute("src").split(",")[-1]
        imgdata = base64.b64decode(base64_str)
        with open(filename, 'wb') as file:
            file.write(imgdata)
        self.img_element = img_element

if __name__ == '__main__':
    imgpath=os.path.join(os.getcwd(),'vcode.png')
    driver = webdriver.Chrome()
    try:
        logintest = login12306(driver)
        logintest.get_Vcode(imgpath)
        logintest.showImage(imgpath)
        code_num = input("Enter Vcode number(Such as 1,2):")
        code_num=[int(x)-1 for x in code_num.split(',')]
        # logintest.verifycode(code_num)
        # logintest.moveaction(code_num)
        logintest.login("username","password",code_num)
        logintest.submit()
    finally:
        driver.close()