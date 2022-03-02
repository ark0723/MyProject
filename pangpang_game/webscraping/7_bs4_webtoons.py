import requests
from bs4 import BeautifulSoup

# url = "https://comic.naver.com/webtoon/weekday.nhn"
# res = requests.get(url)
# res.raise_for_status()
#
# soup = BeautifulSoup(res.text, "lxml") # (불러올 text, parser)
#
# # 네이버 웹툰 전체 목록 가져오기
# # class 속성이 title인 모든 "a" element 반환
# cartoons = soup.find_all("a",attrs = {"class": "title"})
#
# for title in cartoons:
#     print(title.get_text())

# 웰컴투실버라이프
url = "https://comic.naver.com/webtoon/list.nhn?titleId=749456"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 만화제목과 링크 가져오기
titles = soup.find_all("td", attrs={"class":"title"})
for title in titles:
    print(title.a.get_text())
    print("https://comic.naver.com" + title.a["href"])

# 만화 평점 구하기
total_rate = 0
rates = soup.find_all("div", attrs = {"class":"rating_type"})
for rate in rates:
    #print(rate.strong.get_text())
    total_rate += float(rate.strong.get_text()) #string을 float으로 변환

    # print(rate.strong.get_text()) 같은 기능
    # print(rate.find("strong").get_text())

total_rate = total_rate / len(rates)
print(total_rate)