from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import os
from random import *
from bs4 import BeautifulSoup
import requests
import platform
from selenium.common.exceptions import NoSuchElementException  # 이거 추가해야되나
# # Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
# driver = webdriver.Chrome('../chromedriver/chromedriver')
# # PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
# # driver = webdriver.PhantomJS(
# #     '../chromedriver/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
# driver.implicitly_wait(3)
# # url에 접근한다.
# driver.get('https://google.com')


# def get_html(url):  # 날씨 코드를 받아오기
#     _html = ""
#     resp = requests.get(url)
#     if resp.status_code == 200:
#         _html = resp.text
#     return _html


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# for webdriver chromedriver 2.35 linux64
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument('headless')
# chrome_options.add_argument('window-size=1100x400')
chrome_options.add_argument('disable-gpu')
if platform.system() == "Windows":
    try:
        driver = webdriver.Chrome(os.path.join(
            BASE_DIR, '../chromedriver/chromedriver.exe'), chrome_options=chrome_options)
    except ConnectionResetError:
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        driver = webdriver.Chrome(os.path.join(
            BASE_DIR, '../chromedriver/chromedriver.exe'), chrome_options=chrome_options)
else:
    try:
        driver = webdriver.Chrome(os.path.join(
            BASE_DIR, 'chromedriver'), chrome_options=chrome_options)
    except ConnectionResetError:
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        driver = webdriver.Chrome(os.path.join(
            BASE_DIR, 'chromedriver'), chrome_options=chrome_options)
driver.implicitly_wait(3)
# url에 접근한다.


class Tisory:
    def __init__(self):
        # self.id = id
        # self.password = password
        # self.advertising()
        self.output = ""

    def advertising(self):
        print("Start")
        #JavascriptExecutor js = (JavascriptExecutor) driver
        driver.get('https://mgh3326.tistory.com/m')
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        num = randrange(1, 11)
        # print(randrange(1,3))  # 주사위처럼 1에서 6까지의 정수 중 하나를 무작위
        # print(randrange(1,6))  # 주사위처럼 1에서 6까지의 정수 중 하나를 무작위
        driver.find_element_by_xpath(
            """//*[@id = "mArticle"]/div[3]/ul/li[%d]/a/span[1]/span""" % num).click()  # 로그인 버튼 누르기
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        elem = driver.find_element_by_xpath("//*")
        source_code = elem.get_attribute("outerHTML")
        soup_data = BeautifulSoup(
            source_code, 'html.parser')  # beautiful함수로 실행
        # print(soup_data)
        # print(source_code)
        # f = open('frame.html', 'wb')
        kakao = soup_data.findAll("iframe")[2].get('id')
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        driver.switch_to_frame(kakao)

        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(5, 10))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(10, 20))))  # Time in seconds.
        try:

            driver.find_element_by_xpath(
                """//*[@id="banner"]/span[2]""").click()  # 로그인 버튼 누르기
        except:
            temp = randrange(1, 3)
            if temp == 1:
                temp_num = randrange(1, 4)
                driver.find_element_by_xpath(
                    """//*[@id="mArticle"]/div/div[6]/div[2]/ul/li[%d]/a/span[1]/span""" % temp_num).click()  # 로그인 버튼 누르기
            else:
                temp_num = randrange(1, 7)
                driver.find_element_by_xpath(
                    """//*[@id="mArticle"]/div/div[8]/ul/li[%d]/a""" % temp_num).click()  # 로그인 버튼 누르기
            print("예외 처리 시작!")
            self.rerere()

            # return
            # for index in soup_data.findAll("iframe"):
            #     f.write(index.encode('utf-8'))
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        driver.switch_to_window(driver.window_handles[1])
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.

        # driver.save_screenshot('out.png')
        sleep(float("{0:.2f}".format(uniform(10, 20))))  # Time in seconds.
        #td class tl_tit_l 이거 다 모아보자

        #         a=[];
        # a = driver.find_elements_by_class_name("content");

        # f.close()
        # driver.save_screenshot('out.png')
        print("Finish")

    def rerere(self):
        elem = driver.find_element_by_xpath("//*")
        source_code = elem.get_attribute("outerHTML")
        soup_data = BeautifulSoup(
            source_code, 'html.parser')  # beautiful함수로 실행
        # print(soup_data)
        # print(source_code)
        # f = open('frame.html', 'wb')
        kakao = soup_data.findAll("iframe")[2].get('id')
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        driver.switch_to_frame(kakao)

        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(5, 10))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(10, 20))))  # Time in seconds.
        try:

            driver.find_element_by_xpath(
                """//*[@id="banner"]/span[2]""").click()  # 로그인 버튼 누르기
        except:
            temp = randrange(1, 3)
            if temp == 1:
                temp_num = randrange(1, 4)
                driver.find_element_by_xpath(
                    """//*[@id="mArticle"]/div/div[6]/div[2]/ul/li[%d]/a/span[1]/span""" % temp_num).click()  # 로그인 버튼 누르기
            else:
                temp_num = randrange(1, 7)
                driver.find_element_by_xpath(
                    """//*[@id="mArticle"]/div/div[8]/ul/li[%d]/a""" % temp_num).click()  # 로그인 버튼 누르기
            # print("클릭 못했어 예외 처리 해야되")
            # return
            # for index in soup_data.findAll("iframe"):
            #     f.write(index.encode('utf-8'))
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.


if __name__ == "__main__":

    Tisory = Tisory()

    Tisory.advertising()
    # Tisory.homework(6, 1)
    # print(Tisory.output)
    driver.quit()
    # driver.close()
