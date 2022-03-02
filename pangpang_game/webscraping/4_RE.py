# 정규식: regular expression(re)
import re

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는 것이 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태: 정규식
# ca?e
# . : 하나의 문자를 의미
# ^ : 문자열의 시작을 의미
# "^de" : desk, destination (0)
# $ : 문자열의 끝을 의미
# "se$" : case, base, vase(0)

def print_match(m):
    if m:  # 매치가 되었으면
        print("m.group() :", m.group()) # 일치하는 문자열을 반환
        print("m.string() :", m.string) # 입력받는 문자열을 그대로 반환
        print("m.start() :", m.start())  # 일치하는 문자열의 시작 인덱스
        print("m.end() :", m.end())  # 일치하는 문자열의 끝 인덱스
        print("m.span() :", m.span())  #일치하는 문자열의 시작과 끝 인덱스

    else:
        print("매칭되지 않았습니다.")

p = re.compile("ca.e") # cave, cafe, ....

m = p.match("careless") # match: 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)

m = p.search("good care") # search: 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

lst = p.findall("good care cafe") # findall: 일치하는 모든것을 리스트 형태로 반환
print(lst)

