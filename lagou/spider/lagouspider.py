#__author__="noveling"
from selenium import webdriver
import loadstr
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://www.lagou.com/"

class Lagouspider(object):
    def __init__(self,wd="",maxpage=1):
        self.url = "https://www.lagou.com/jobs/list_"+wd+"?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput="
        self.wb = webdriver.Firefox()
        self.maxpage=maxpage
        self.res = []
        self.start=1

    def first(self):
        self.wb.get(self.url)
        self.parse()

    def parse(self):
        all_job = WebDriverWait(self.wb,3).until(EC.presence_of_element_located((By.XPATH,"//div[@id='s_position_list']/ul[1]")))
        for job in all_job.find_elements_by_xpath("//li"):
            if job.get_attribute("data-positionname"):
                position=[job.get_attribute("data-company"),job.get_attribute("data-positionname"),job.get_attribute("data-salary")]
                self.res.append(position)
        if self.start == self.maxpage:
            print("结束！")
            for i in self.res:
 #             print(i)
                content = "公司："+str(i[0])+"  职务："+str(i[1])+"  薪水："+str(i[2])+"\n"
                loadstr.loadstr("公司："+str(i[0])+"  职务："+str(i[1])+"  薪水："+str(i[2])+"\n")
                print(content)
            self.wb.close()
        self.start+=1
        self.next_page()

    def next_page(self):
        while(self.start<=self.maxpage):
            self.wb.find_element_by_xpath("//*[@id='s_position_list']/div[2]/div/span[last()]").click()
            time.sleep(2)
            self.parse()



if __name__ == "__main__":
    spider = Lagouspider(input("输入内容是"),maxpage=3)
    spider.first()
