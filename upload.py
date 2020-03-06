from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
from time import strftime, localtime
from threading import Timer


#识别title是否出现投稿字样，如果出现投稿字样，则跳入case 2
#识别阻塞，输出时间，刷新页面
#如果不为阻塞则将,新的状态存起来，作为下一次
#def HandleLoginPage:


 #switch = {"valueA":functionA,"valueB":functionB,"valueC":functionC}
 #try:
#　　switch["value"]() #执行相应的方法。
# except KeyError as e:
#       pass 或 functionX #执行default部分

driver = webdriver.Chrome()
url = 'https://member.bilibili.com/video/upload.html'
driver.get(url)
time.sleep(5)
print(driver.title)
i = 0
while(i < 1000):  
    i = i + 1
    try:  
        print(driver.title)       
        listing = driver.find_elements_by_class_name("video-jam-state")
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()),end="\t")
        for k in range(len(listing)):
            print(listing[k].text)
        driver.refresh()
    except Exception:
        print ('str(Exception):\t\t', str(Exception))   
    time.sleep(20)
   # driver.find_element_by_name("你的手机号").send_keys("18923296180")
   # driver.find_element_by_name("密码").send_keys("mia984299")
   # driver.find_element_by_class_name("btn-login").click()
   

#movies = get_movies()
#print(movies)