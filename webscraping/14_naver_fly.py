from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#chrome version 확인 및 chrome driver 설치한 후 실행
browser = webdriver.Chrome("C:/Users/ark07/PycharmProjects/chromedriver.exe") # chromedriver 설치경로 표시:
browser.get("https://flight.naver.com/flights/")