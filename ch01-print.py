# 참조 : https://www.python-course.eu/python3_formatted_output.php

print('Hello python')

#print 사용법, 기본출력
print('Hello python')
print("asdfasdf")
print() # 띄어 쓰기
print('''python Start!''')
print("""python Start!""")

#separator
print('p', 'y', 't', 'h', 'o', 'n', sep='|')
print('010', '1234', '7777', sep='-')
print('python', 'google.com', sep='@')
print()

#end 옵션 -> 다음 print의 문자에 붙여준다
print('Welcom to', end=' ')
print('IT News', end=' ')
print('web site')
print()

#file 옵션
from fcntl import DN_DELETE
import sys
print
print('Learn Python', file = sys.stdout)

#format 사용(d: 3, s: 'python', f: 3.14)

print('%s %s' % ('one', 'two'))
print('{} {}' .format('one', '2'))
print('{1} {0}' .format('one', 'two'))


# %s
print()
print('%10s' % ('nice'))
print('{:>10}'.format('nice')) 

print('%-10s' % ('nice'))
print('{:10}'.format('nice')) 

print('------------------')
print('{:_>10}'.format('nice'))
 
print('{:^10}'.format('nice')) #중앙정렬

print('%.5s' % ('nice')) #5자리 이후에는 절삭
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))#공간은 10개인데 5개 이후로 절삭

# %d
print('%d %d' %(1,2))
print('{} {}' .format(1,2))

print('%4d' % (42))
print('{:4d}' .format(42))

# %f
print('%1.8f' % (3.21654654654654))
print('%f' % (3.21654654654654))
print('{:f}' .format(3.21654654654654))

print('%06.2f' % (3.126565465412))
print('{:06.2f}' .format(3.126565465412))

######
########