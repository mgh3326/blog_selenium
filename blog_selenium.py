from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import os
from random import *
from bs4 import BeautifulSoup
import requests
import platform
from selenium.common.exceptions import NoSuchElementException
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


class Blog:
    def __init__(self):
        # self.id = id
        # self.password = password
        # self.advertising()
        self.output = ""

    def advertising(self):
        print("Start")
        #JavascriptExecutor js = (JavascriptExecutor) driver
        driver.get('https://mgh3326.github.io')
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.

        # print(randrange(1,3))  # 주사위처럼 1에서 6까지의 정수 중 하나를 무작위
        # print(randrange(1,6))  # 주사위처럼 1에서 6까지의 정수 중 하나를 무작위
        num1, num2 = randrange(1, 6), randrange(1, 3)
        print("num1 : %d, num2 %d" % (num1, num2))
        driver.find_element_by_xpath(
            """//*[@id="main"]/div[2]/section/div[2]/div[%d]/article[%d]/div/a/span[1]""" % (num1, num2)).click()  # 로그인 버튼 누르기
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.

        elem = driver.find_element_by_xpath("//*")
        source_code = elem.get_attribute("outerHTML")
        soup_data = BeautifulSoup(
            source_code, 'html.parser')  # beautiful함수로 실행
        # print(soup_data)
        # print(source_code)
        # f = open('frame.html', 'wb')
        kakao = soup_data.findAll("iframe")[1].get('id')
        # for index in soup_data.findAll("iframe"):
        #     print(index.get('id'))
        #     # f.write(index.encode('utf-8'))

        # f.close()
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        # driver.save_screenshot('test.png')

        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        driver.switch_to_frame(kakao)
        # print(kakao)
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(5, 10))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(10, 20))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(10, 20))))  # Time in seconds.

        try:

            driver.find_element_by_xpath(
                """//*[@id="landingLink"]/span/img""").click()  # 로그인 버튼 누르기
        except:
            print("예외 처리 시작!")
            sleep(float("{0:.2f}".format(uniform(10, 20))))  # Time in seconds.
            sleep(float("{0:.2f}".format(uniform(10, 20))))  # Time in seconds.
            # Time in seconds.
            sleep(float("{0:.2f}".format(uniform(100, 200))))
            print("일단 그냥 꺼지게 하자")
            return  # 일단 그냥 꺼지게 하자
            temp = randrange(1, 3)
            if temp == 1:
                temp_num = randrange(1, 3)
                if temp_num == 1:

                    driver.find_element_by_xpath(
                        """//*[@id="article-nav-newer"]/p""").click()  # 로그인 버튼 누르기
                else:
                    driver.find_element_by_xpath(
                        """//*[@id="article-nav-older"]/p""").click()
            else:
                temp_num = randrange(1, 6)
                driver.find_element_by_xpath(
                    """//*[@id="recent-post"]/li[%d]/div[2]/p[2]/a""" % temp_num).click()  # 로그인 버튼 누르기
            print("예외 처리 시작!")
            self.rerere()
        #https://stackoverflow.com/questions/19200497/python-selenium-webscraping-nosuchelementexception-not-recognized
        #위에 링크처럼 해줘야겠다. 예외처리해서 다른 페이지 가서 실행하게 하면 되겠다.
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        driver.switch_to_window(driver.window_handles[1])
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.

        # driver.save_screenshot('out.png')
        sleep(float("{0:.2f}".format(uniform(10, 20))))  # Time in seconds.
        #td class tl_tit_l 이거 다 모아보자
        sleep(float("{0:.2f}".format(uniform(10, 20))))  # Time in seconds.

        #         a=[];
        # a = driver.find_elements_by_class_name("content");
        print("Finish")

    def rerere(self):
        elem = driver.find_element_by_xpath("//*")
        source_code = elem.get_attribute("outerHTML")
        soup_data = BeautifulSoup(
            source_code, 'html.parser')  # beautiful함수로 실행
        # print(soup_data)
        # print(source_code)
        # f = open('frame.html', 'wb')
        kakao = soup_data.findAll("iframe")[1].get('id')
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
                """//*[@id="landingLink"]/span/img""").click()  # 로그인 버튼 누르기
        except:
            sleep(float("{0:.2f}".format(uniform(10, 20))))  # Time in seconds.

            temp = randrange(1, 3)
            if temp == 1:
                temp_num = randrange(1, 3)
                if temp_num == 1:

                    driver.find_element_by_xpath(
                        """//*[@id="article-nav-newer"]/p""").click()  # 로그인 버튼 누르기
                else:
                    driver.find_element_by_xpath(
                        """//*[@id="article-nav-older"]/p""").click()
            else:
                temp_num = randrange(1, 6)
                driver.find_element_by_xpath(
                    """//*[@id="recent-post"]/li[%d]/div[2]/p[2]/a""" % temp_num).click()  # 로그인 버튼 누르기
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.


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
        print("num : "+str(num))
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
                """//*[@id="landingLink"]/span/img""").click()  # 로그인 버튼 누르기
        except:

            sleep(float("{0:.2f}".format(uniform(10, 20))))  # Time in seconds.

            temp = randrange(1, 3)
            if temp == 1:
                temp_num = randrange(1, 4)
                driver.find_element_by_xpath(
                    """//*[@id="mArticle"]/div/div[6]/div[2]/ul/li[%d]/a/span[1]/span""" % temp_num).click()  # 로그인 버튼 누르기
            else:
                # Time in seconds.
                sleep(float("{0:.2f}".format(uniform(10, 20))))

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
                """//*[@id="landingLink"]/span/img""").click()  # 로그인 버튼 누르기
        except:
            sleep(float("{0:.2f}".format(uniform(10, 20))))  # Time in seconds.

            temp = randrange(1, 3)
            if temp == 1:
                temp_num = randrange(1, 4)
                driver.find_element_by_xpath(
                    """//*[@id="mArticle"]/div/div[6]/div[2]/ul/li[%d]/a/span[1]/span""" % temp_num).click()  # 로그인 버튼 누르기
            else:
                # Time in seconds.
                sleep(float("{0:.2f}".format(uniform(10, 20))))

                temp_num = randrange(1, 7)
                driver.find_element_by_xpath(
                    """//*[@id="mArticle"]/div/div[8]/ul/li[%d]/a""" % temp_num).click()  # 로그인 버튼 누르기
            # print("클릭 못했어 예외 처리 해야되")
            # return
            # for index in soup_data.findAll("iframe"):
            #     f.write(index.encode('utf-8'))
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.


if __name__ == "__main__":
    ohoh = randrange(1, 3)
    if(ohoh == 1):
        print("github")
        Blog = Blog()

        Blog.advertising()
    else:
        print("tistory")
        Tisory = Tisory()

        Tisory.advertising()
    # Blog.homework(6, 1)
    # print(Blog.output)
    driver.quit()
    # driver.close()
