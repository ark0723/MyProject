balls = [1,2,3,4]
weapons = [11, 22, 3, 44]

'''
for ball_idx, ball_val in enumerate(balls):
    print("ball ", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons :", weapon_val)
        if ball_val == weapon_val: #충돌체크
            print("공과 무기가 충돌")
            break
'''

for ball_idx, ball_val in enumerate(balls):
    print("ball ", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons :", weapon_val)
        if ball_val == weapon_val: #충돌체크
            print("공과 무기가 충돌")
            break
    # 이중 for loop 빠져나오는 팁
    else:
        continue
    print("바깥 for 문 break")
    break #안쪽 for문에 break가 있어야만 쓸 수 없음
