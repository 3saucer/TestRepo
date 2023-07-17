# 시분초를 변수로 입력하고 나서 1001초 후의 시간을 출력해주세요!
# 24시간이 넘는 경우에는 0으로 초기화 합니다

hour, min = map(int,input().split()) # 시,분
cook_min = int(input())

min += hour * 60
min += cook_min

min_mod = min % 60
hour = min // 60
hour_mod = hour % 24

print(hour_mod, min_mod) 