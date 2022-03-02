from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])

#chrome version 확인 및 chrome driver 설치한 후 실행
browser = webdriver.Chrome("C:/Users/ark07/PycharmProjects/chromedriver.exe",options=options) # chromedriver 설치경로 표시:

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("mobbom")
browser.find_element_by_id("pw").send_keys("Ark07231527!")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# time.sleep(3) #3초 기다리기

# 5. id 새로 입력
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("mobbom")
# browser.find_element_by_id("pw").send_keys("Ark07231527!")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재브라우저 종료
# browser.quit() # 전체 브라우저 종료
