import requests

res = requests.get("http://google.com")

res.raise_for_status()
print("웹 스크래핑을 진행합니다.")

# print("응답코드 :", res.status_code) #200: 정상 403: 가져올수 없음(권한)

# if res.status_code == requests.codes.ok: #즉 200이면
#     print("정상입니다.")
#
# else:
#     print("문제가 있습니다.[에러코드: ", res.status_code, "]")

print(len(res.text))

with open("mygoogle.html", "w", encoding= "utf-8") as f:
    f.write(res.text)
