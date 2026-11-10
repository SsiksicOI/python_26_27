# 문제 : 입력받은 정수가 소수인지 아닌지 알려주는 함수를 구현해주세요.
# is로 시작하면 관례상 True 나 False로 리턴
# def is_prime_number(num):
#   if num <= 1:
#     return False
#   i = 2
#   while i < num:
#     if num % i == 0:
#       return False
#     i += 1
  
#   return True

# some_num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# for i in some_num:
#     is_prime_number(i)


# print("3은 소수입니다 : {}".format(is_prime_number(3)))
# print("4는 소수입니다 : {}".format(is_prime_number(4)))
# print("5는 소수입니다 : {}".format(is_prime_number(5)))
# print("6는 소수입니다 : {}".format(is_prime_number(6)))
# print("7는 소수입니다 : {}".format(is_prime_number(7)))
# print("1000은 소수입니다 : {}".format(is_prime_number(1000)))



# def get_divisors_sum(num):
#   s = 0
#   i = 1
#   while i <= num:
#     if num % i == 0:
#       s += i
#     i += 1
#   return s

# def is_prime_number_v2(num):
#   return get_divisors_sum(num) == num + 1

# print(get_divisors_sum(2))


'''
    객체란? => 폴더
    관련된 데이터끼리 묶는게 좋다.



'''

'''
# 문제 : 리스트에 순서대로 2, 1, 5, 6, 7를 한 번에 담아주세요.
some_list = [2, 1, 5, 6, 7]

# 문제 : 비어있는 리스트를 만들고, 순서대로 2, 1, 5, 6, 7를 하나씩 담아주세요.

some_list = []
some_list.append(2)
some_list.append(1)
some_list.append(5)
some_list.append(6)
some_list.append(7)


# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 그리고 '+=' 연산자를 이용해서 '토', '일' 을 한번에 추가해주세요.

some_list = []

some_list.append('월', '화', '수', '목', '금')
some_list += ['토', '일']


# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 그리고 가장 마지막 요소를 출력해주세요.
some_list = []

some_list.append('월', '화', '수', '목', '금')

print(some_list[4])


# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 그리고 while문을 이용해서 요소 전부 출력해주세요.
some_list.append('월', '화', '수', '목', '금')

i = 0
while i < len(some_list):
    print(some_list[i])


# 문제 : 리스트에 순서대로 2, 1, '오', 6, 7를 한번에 담아주세요. 그리고 리스트 안에 있는 '오'를 정수 5로 변경해주세요.

some_list.append(2, 1, '오', 6, 7)

some_list[some_list.index('오')] = 5

print(some_list)

'''

'''
    리스트 장점
        - 데이터를 넣을 때 편하다
        a.append(10) #0
        a[0] = 20

    딕셔너리 장점
        - 데이터를 가져올 때 편하다
        a["철수"] = 10
        a["철수"] = 20
'''


'''
# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담기
month_end_days = {
    "1월" : 31,
    "2월" : 28,
    "3월" : 31
}

print(month_end_days)

# 문제 : 딕셔너리에 각 달의 마지막 날들을 반복문을 통해 담기

for i in month_end_days:
    if i == "1월":
        month_end_days[i] = 31
    elif i == "2월":
        month_end_days[i] = 28
    else :
        month_end_days[i] = 31
        
print(month_end_days)

month_end_days = {}

for i in range(1, 13):
    month = str(i) + "월"

    end_day = 31

    if i == 2:
        end_day = 28
    elif i in [4, 6, 9, 11]:
        end_day = 30

    month_end_days[month] = end_day
print (month_end_days)


month_end_days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i, end_day in enumerate(month_end_days_list):
    month = str(i+1) + "월"
    month_end_days[month] = end_day
    
print(month_end_days)
'''


'''
    문자열
    인덱싱 : 특정 위치의 문자 하나를 가져오는 것
    슬라이싱 : 지정한 범위의 문자열을 가져오는 것

'''

'''
print("=== 예제 1번 ===")
s = '안녕하세요.'
#   [0 1 2 3 4 5]

print('s의 길이 출력')
print(len(s))

# 문자열[시작:종료-1:간격]
print('s를 이루는 문장 중에서 앞에 거 2개 출력')
print(s[0:2])

print('s를 이루는 문장 중에서 문자 하나 건너 뛰고 1개 출력')
print(s[1:2])

print('s를 이루는 문장 중에서 문자 4개 출력, 첫 인덱스 생략')
print(s[:4])

print('s를 이루는 문장 중에서 앞에 문자 3개 건너뛰고, 나머지 전부 출력')
print(s[3:len(s)])

print('s를 이루는 문장 중에서 앞에 문자 3개 건너뛰고, 뒤 인덱스 생략')
print(s[3:])


print('=== 예제2 ===')
s = '안녕하세요.'

print('s를 이루는 문자를 하나씩 출력, while')

i = 0
while i < len(s):
    print(s[i])
    i += 1


print('s를 이루는 문자를 역순으로 하나씩 출력, while')

i = len(s) - 1
while i >= 0:
    print(s[i])
    i -= 1


print('s를 이루는 문자를 하나씩 출력, for')
for c in s:
    print(c)



print('=== 예제3 ===')

s = 'a안b녕c하d세e요f'

print('s를 이루는 문장 중에서 한글만 출력, for, if, or, continue')
for c in s:
    if c == 'a' or c == 'b' or c == 'c' or c == 'd' or c == 'e' or c == 'f':
        continue    
    print(c)

print('s를 이루는 문장 중에서 한글만 출력, for, if, and, continue')
for c in s:
    if c != 'a' and c != 'b' and c != 'c' and c != 'd' and c != 'e' and c != 'f':
        print(c)


print('s를 이루는 문장 중에서 한글만 출력, not in')
for c in s:
    if c not in ['a','b','c','d','e','f']:
        print(c)


print('숫자를 입력해주세요 : ', end="")
x = input()
print("변환 시도!")
try:
    y = int(x)
    print(f"입력하신 숫자는 {y}입니다.")
except ValueError:
    print("숫자를 입력해주세요.")
else:
    print("변환 성공!")
print("변환 종료!")
'''


'''
    storage : 현재 저수지에 저장된 물의 양을 나타내는 정수
    usage : 지난 달 물 사용량을 나타내는 정수
    change : 월별 물 사용량이 전 달 대비 어떻게 변하는지 저장된 정수 리스트

def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = total_usage * change[i]/100
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1


# solution(1000, 1000, [1,2,3,4,5])
'''

# 문제 : 리스트에 순서대로 2, 1, '오', 6, 7를 한번에 담아주세요. 그리고 리스트 안에 있는 '오'를 정수 5로 변경해주세요.

# l = [2, 1, '오', 6, 7]

# l[l.index('오')] = 5

# print(l)


# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. '화'가 리스트 안에 들어있는지 알려주세요.

# l = ['월', '화', '수', '목', '금']

# for i in l :
#     if i in '화':
#         print("'화' 가 리스트 안에 있습니다.")
#         break

# # 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. '화'가 리스트 안에서 몇 번째 데이터 인지 알려주세요.
# l = ['월', '화', '수', '목', '금']

# for i in range (0, len(l)):
#     if l[i] in '화':
#         print(f'{i+1} 번째 데이터 입니다.')


# # 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 리스트에 있는 '금'을 삭제하는 3가지 방법을 보여주세요.
# l = ['월', '화', '수', '목', '금']

# print("=== 첫번째 ===")
# del l[4]

# print("=== 두번째 ===")
# del l[-1]

# print("=== 세번째 ===")
# del l[l.index('금')]

# print("=== 네번째 ===")
# l.remove('금')

# print(l)



'''
    클래스 -> 객체를 표한하기 위한 문법의 일종
    전사, 마법사, 궁수, 자동차, 비행기, 사람, 강아지, 고양이 등 현실, 가상, 개념

    속성 - Attribute
    능력(기능) - Method

    전사 클래스 - 체력, 공격력 -> 속성(변수)
               - 공격하다, 방어하다 -> 메소드(함수)

    
'''

'''
class Person:
    def hello(self):
        print('hi')

jin = Person() # jin은 Person의 인스턴스(특정 클래스로부터 생성된 객체)
jin.hello()


class Person:
    pass

class Person():
    def hello(self):
        print('hello')
    def hi(self):
        self.hello()

jin = Person()
jin.hi()

class Person():
    def __init__(self, name, age, hobby): # 클래스 내부에서 접근
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.hobby = hobby

    def  introduce(self):
        print(f'{self.hello} 저의 이름은 {self.name}이고 나이는 {self.age}이고 제 취미는 {self.hobby}입니다.')

jin = Person('진', 22, '운동') # 이 때 __init__ 메서드가 실행됐다.
jin.introduce()

print(f'이름 : {jin.name}') # 클래스 외부에서 접근
print(f'나이 : {jin.age}')
print(f'취미 : {jin.hobby}')


class Person:
    pass

jin = Person() # 인스턴스 생성
jin.name = '진' # 인스턴스를 생성한 뒤 속성을 추가 / 해당 인스턴스에서만 사용이 가능함

print(jin.name)

# kim = Person()
# print(kim.name)


# 클래스 외부에서는 접근 불가, 클래서 내부에서만 사용 가능한 private attribute

class Person():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight # 비공개 속성 / 사용법: 앞에 __(언더바 2개)

    def diet(self, loss_weight):
        self.__weight -= loss_weight
        print(jin.__weight)

jin = Person('진', 22, 80)
jin.diet(10)

'''

'''
class Person():
    def __init__(self, name, age, hobby):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.hobby = hobby

jin = Person('진', 22, '운동')
'''

# 클래스 속성
class Person:
    __weight = 80
    folder = [] # 클래스 속성 (공용 / 창고같은 느낌)

    def add_files(self, file):
        self.folder.append(file)

    def print_weight(self):
        print(Person.__weight)

jin = Person()
jin.add_files('txt')

jin.print_weight()

kim = Person()
kim.add_files('img')

print(jin.folder)
print(kim.folder)


print('hi')