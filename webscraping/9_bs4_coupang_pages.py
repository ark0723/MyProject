import requests
import re
from bs4 import BeautifulSoup

# HTTP GET(?key = value & key = value & ...)
# HTTP POST (password나 개인정보 등에서 쓰임)
headers = {"User-Agent": \
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

# 최근 5개 페이지 내 상품 리스트 검색
for i in range(1, 6):
    print(" 페이지 no: ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    res = requests.get(url, headers= headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    # class가 "search-product"로 시작하는 모든 "li" elements 가져오기
    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

    for item in items:

        # 광고 제품은 제외
        ad_badge = item.find("span", attrs = {"class": "ad-badge-text"})
        if ad_badge:
            print(" <광고 상품 제외> ")
            continue


        # 제품명
        name = item.find("div", attrs= {"class": "name"}).get_text()

        # 애플 제품 제외
        if "Apple" in name:
            print(" <애플 제품 제외> ")
            continue

        # 가격
        price = item.find("strong", attrs = {"class": "price-value"}).get_text()
        # 평점
        rate = item.find("em", attrs = {"class": "rating"})
        # 평점 수
        count = item.find("span", attrs={"class": "rating-total-count"})
        if rate:
            rate = rate.get_text()
            count = count.get_text()
            count = re.sub(r"[^a-zA-Z0-9]", "", count) # () 없애기

        else:
            print(" <평점 없는 상품 제외> ")
            continue

        # 리뷰 100개 이상, 평점 4.5 이상인 제품만 조회
        if float(rate) >= 4.5 and int(count) >= 100:
            link = "https://www.coupang.com" + item.a["href"]
            print("상품명 : ", name)
            print("가격 : ", price)
            print("평점(평점 수) : ", rate, "(",count,"개)" )
            print("링크 :", link)
            print("=" * 100)
