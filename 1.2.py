# ws_1_2.py

string = '문자열'
integer = 10
floating_point = 3.14
a_list = [1, 2, 3, 4, 5]
dictionary = {'name': '홍길동', 'age': 20}
a_set = {1, 2, 3, 4, 5}
a_range = range(11)
a_tuple = (1, 2, 3)
boolean = True

print(type(string))
print(type(integer))
print(type(floating_point))
print(type(a_list))
print(type(dictionary))
print(type(a_set))
print(type(a_range))
print(type(a_tuple))
print(type(boolean))

#2. 해당 타입이 맞는지 그 결과를 출력
#is 비교 연산자 사용.. 가리키는 주소가 서로 같은지를 비교
# print(type(string) is str)
# print(isinstance(integer, int))