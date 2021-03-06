#자주 사용하는 함수 위주로 실습
#사용하다보면 자연스럽게 숙달됨

#절대값
#abs()

print(abs(-3))

# all : iterable 요소 검사(참, 거짓)
print(all([1, 2, '0'])) # 모두 true일때만 true  # and
print(any([1, 2, '0'])) # 하나라도 true 있으면 true # or

#chr : 아스키 -> 문자, ord : 문자 -> 아스키

print(chr(67))
print(ord('C'))

#enumerate : 인덱스 + iterable 객체 생성

for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pas(x):
    return abs(x) > 2

print(list(filter(conv_pas, [1,-3,5,-2,6])))
print(list(filter(lambda x: abs(x) > 2, [1,-3,5,-2,6])))

# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))

# len : 요소의 길이를 반환
print(len('asdfasdf'))
print(len([1,-3,5,-2,6]))

#max, min : 최대값, 최소값

print(max([1,2,3]))
print(max('ptrhon study'))
print('----------------------')
print(min([1,2,3]))
print(min('ptrhonstudy'))

# map : 반복 가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1,-3,2,0,-5,6])))

#pow : 제곱값 반환
print(pow(2, 10))

#range : 반복가능한 객체(iterable) 반환
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))

