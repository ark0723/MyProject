import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # (불러올 text, parser)
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체이서 처음 발견되는 a를 반환
# print(soup.a.attrs) # a element의 attributes를 dictionary형태도 반환
# print(soup.a["href"]) # a의 특정 attribute에 접근
# print(soup.a["onclick"])

# soup 객체 내의 모든 a를 찾고, 그 중에서 attrs 내 클래스 정보고 Nbtn_upload 인 것을 찾으시오
# print(soup.find("a", attrs = {"class": "Nbtn_upload"}))
# print(soup.find(attrs = {"class": "Nbtn_upload"}))

# print(soup.find("li", attrs = {"class": "rank01"}
rank1 = soup.find("li", attrs = {"class": "rank01"})
# print(rank1.a)
# print(rank1.a.get_text())

# sibling 찾기
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a.get_text())
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
#
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# 부모찾기
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
#
# rank1 = rank2.find_previous_sibling("li")
# print(rank1.a.get_text())

ranks = rank1.find_next_siblings("li")

for i in ranks:
    print(i.a.get_text())

webtoon = soup.find("a", text = "독립일기")
print(webtoon)