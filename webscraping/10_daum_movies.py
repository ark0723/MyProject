import requests
import re
from bs4 import BeautifulSoup

# HTTP GET(?key = value & key = value & ...)
# HTTP POST (password나 개인정보 등에서 쓰임)
headers = {"User-Agent": \
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}


for year in range(2015, 2021):
    url = "https://search.daum.net/search?w=tot&q={0}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url, headers= headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    # class가 "thumb-img" 인 img tag 가져오기
    images = soup.find_all("img", attrs = {"class": "thumb_img"})

    for idx, img in enumerate(images):
        img_url = img["src"]
        if img_url.startswith("//"):
            img_url = "https:" + img_url

        print(img_url)
        image_res = requests.get(img_url, headers = headers)
        image_res.raise_for_status()
        # image 파일 쓰기 - wb(binary)
        with open("movie_{0}_{1}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        if idx >=4 : # 상위 5개 영화만 가져오기
            break