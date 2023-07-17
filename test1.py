name = list(input('이름을 입력하세요:'))
height = float(input('키를 입력하세요:'))

if height >= 150 and height < 170:
    print('탈 수 있어요')
elif height >= 175 and height <= 180:
    print('탈 수 있어요')
else:
    print('탈 수 없어요')