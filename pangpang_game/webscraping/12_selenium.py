from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#chrome version 확인 및 chrome driver 설치한 후 실행
browser = webdriver.Chrome("C:/Users/ark07/PycharmProjects/chromedriver.exe") # chromedriver 설치경로 표시:
browser.get("http://naver.com")
# login 페이지로 이동 by class name
elem = browser.find_element_by_class_name("link_login")

elem.click()

# 이전 페이지로 이동
browser.back()

# 앞 페이지로 이동
browser.forward()

# 브라우저 새로고침
browser.refresh()

# 네이버 홈으로 돌아오기
browser.back()

# 검색창 찾기 by id
elem = browser.find_element_by_id("query")
elem.send_keys("고아라") # 검색창에 텍스트 입력
elem.send_keys(Keys.ENTER) # 검색창에 엔터 치기

# tag_name으로 찾기 - 'a' tag 모두 가져오기
elem = browser.find_elements_by_tag_name("a")

'''
for e in elem:
    print(e.get_attribute("href"))
'''
# 다음 홈페이지로 이동
browser.get("http://daum.net")
elem = browser.find_element_by_name("q")
elem.send_keys("고아라")
# 엔터키 눌러서 이동
# elem.send_keys(Keys.ENTER)

# xpath 이용해서 돋보기 아이콘으로 이동
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
elem.click()

# 현재 페이지 종료
# browser.close()

# 모든 브라우저 종료
browser.quit()


