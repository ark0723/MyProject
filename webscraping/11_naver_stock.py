import requests
import csv
from bs4 import BeautifulSoup


# HTTP GET(?key = value & key = value & ...)
# HTTP POST (password나 개인정보 등에서 쓰임)
headers = {"User-Agent": \
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# csv 파일 쓰기
f_name = "시가총액200.csv"

# newline=""은 enter 없이 바로 다음줄로 쓰이도록 해줌
# 한글이 깨질경우 encoding = "utf-8-sig"
f = open(f_name, "w", encoding = "utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# print(title)
# title 을 첫 줄로 입력하기
writer.writerow(title)
for i in range(1,5): # 페이지당 50개씩 총 200개 시가총액 상위 회사
    url = url + str(i)
    res = requests.get(url, headers= headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    # 시가총액 테이블 가져오기
    data_rows = soup.find("table", attrs = {"class": "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미없는 row는 스킵
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)