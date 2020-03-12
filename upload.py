from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
from time import strftime, localtime
import threading


#识别title是否出现投稿字样，如果出现投稿字样，则跳入case 2
#识别阻塞，输出时间，刷新页面
#如果不为阻塞则将,新的状态存起来，作为下一次
#def HandleLoginPage:
#switch = {"valueA":functionA,"valueB":functionB,"valueC":functionC}
#try:
#　　switch["value"]() #执行相应的方法。
# except KeyError as e:
#       pass 或 functionX #执行default部分
class GetUploadStatus() :
    driver = 0
    def __init__(self):
        # 下面为Person对象增加2个实例变量
        self.driver =  webdriver.Chrome()
        url = 'https://member.bilibili.com/video/upload.html'
        self.driver.get(url)

    def WriteFile(self,msg):
        try:
            f = open('upload.txt','a') #实时写入text中，以防关机或者程序中断 
            f.write(msg)
            f.close()
        except Exception as e:
            print(e)
            f.close()

    def GetUploadStatusFromBiliBili(self):
        try:
            print(self.driver.title) #从HTML的title里面可以获知当前页面的信息   
            listing = self.driver.find_elements_by_class_name("video-jam-state")
            dateTime = strftime("%Y-%m-%d %H:%M:%S", localtime()) + '\t'        
            print(strftime("%Y-%m-%d %H:%M:%S", localtime()),end="\t")
            self.WriteFile(dateTime + listing)
            for k in range(len(listing)):
                print(listing[k].text)
            self.driver.refresh()#刷新页面
        except Exception as e:
            print (e)   

up = GetUploadStatus()
time.sleep(5)
timer = threading.Timer(5, up.GetUploadStatusFromBiliBili)
timer.start()
while(1):
    

   


   