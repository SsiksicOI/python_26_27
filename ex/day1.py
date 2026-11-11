'''
age = 20
has_ticket = True

# and : 기준이 엄격함!!!
#  -> True and True => True
#  -> True and Flase => False
# or : 조금 느슨함!!!
#  -> True or False => True
if age >= 20 or has_ticket:
        print('입장 가능합니다.')


age = 10
if age == 10 : 
        print("10입니다.")
elif age == 20 : 
        print("20입니다.")
else : 
        print("그 외입니다.")


# 문제 : 실행되는 출력문에는 `참` 그렇지 않으면 `거짓` 이라고 적어주세요.
# 조건 : `참1`, `참2`, `거짓1` 이런 순으로 적어주세요.

# 개념시작
if ( True ):
  print("참")
    
if ( False ):
  print("거짓")
# 개념끝

# 문제시작
a = 10

# `==` => 같다.
if ( a == 10 ):
  print("참1")

# `!=` => 같지 않다.
if ( a != 10 ):
  print("거짓1")

if ( a > 10 ):
  print("거짓2")

if ( a >= 10 ):
  print("참2")

b = 10

if ( a == b ):
  print("참3")

# c 에는 true or false 이 담긴다.
c = a != b

if ( c ):
  print("거짓3")

if ( c == False ):
  print("참4")

# `not` => 반전
if ( not c ):
  print("참5")

if ( not(not c) ):
  print("거짓4")

d = True

if ( c != d ):
  print("참6")

if ( 10 > 5 and -6 > -10 and 10 != 10 ):
  print("거짓5")

if ( 10 < 5 and -6 < -10 and 10 != 10 or 10 > 5 ):
  print("참7")
# 문제끝





# 문제 : 10대, 20대, 30대 중 나이에 맞는 변수를 출력해주세요.

age = 15 # 25로 바꿔서 실행해보세요. 15로도 바꿔서 실행해보세요.

if(age >= 10 and age < 20):
   print("10대")
elif(age >= 20 and age < 30):
   print("20대")
elif(age >= 30 and age < 40):
   print("30대")



# 문제 : 할인 대상인지 아닌지 출력해주세요.
# 조건 : 나이가 19세 이하이거나 60세 이상이면 할인 대상입니다.
# 조건 : `and, or`없이 풀어야 합니다.
# 조건 : 2가지 이상의 방법으로 풀어야 합니다.

age = 60

print("== 정답 v1 ==")
if(age >= 60):
   print("할인 대상입니다.")
elif(age <= 19):
   print("할인 대상입니다.")
else :
   print("할인 대상이 아닙니다.")


print("== 정답 v2 ==")
if(age < 60):
   if(age <= 19):
      print("할인 대상입니다.")
   else:
      print("할인 대상이 아닙니다.")
else:
   print("할인 대상입니다.")


# print("할인 대상입니다.")
# print("할인 대상이 아닙니다.")


# print("할인 대상입니다.")
# print("할인 대상이 아닙니다.")


#==============================반복문==============================
# 시작값, 조건식, *보폭*(없으면 무한루프 돌아서 무조건 필요)

# +되는 반복문
i = 1
while i <= 3:
   print(i)
   i += 1
print(i)

# -되는 반복문
i = 3
while i >= 3:
   print(i)
   i -= 1
print(i)



# 문제 : 1부터 300까지 출력해주세요.

i = 1
while i <= 300:
   print(i)
   i += 1


# 문제 : 100부터 -25까지 출력해주세요.

i = 100
while i >= -25:
   print(i)
   i -= 1

'''
# 문제 : 1부터 100 사이의 짝수만 출력해주세요.(개념 : while, if, %)
# i = 1
# while i <= 100:
#     if(i % 2 == 0):
#         print('숫자', i, '는 짝수입니다.')
#     i += 1

# 문제 : 1부터 1000 사이의 수 중에서 3의 배수만 출력해주세요.
# i = 1
# while i <= 1000:
#     if(i % 3 == 0):
#         print('숫자', i, '는 3의 배수입니다.')
#     i += 1

# 문제 : 1부터 5까지의 합을 출력해주세요.(개념 : while)
# i = 1
# sum = 0
# while i <= 5:
#     sum += i
#     i += 1
# print(sum)


# 문제 : 1부터 100까지의 수 중에서 짝수의 합을 출력해주세요.(개념 : while, if, %)
# i = 1
# sum = 0
# while i <= 100:
#     if(i % 2 == 0):
#         sum += i
#     i += 1
# print(sum)

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 3:
#         print(j)
#         j += 1
#     i += 1


# while : 조건식이 참인 동안 반복(조건에 따른 반복)
# for : 정해진 범위나 데이터의 요소를 순서대로 반복(범위에 따른 반복)

'''
for 변수 in 반복가능한객체 :
    실행문

range(stop) : 0부터 종료값 직전까지
range(start, stop) : 시작값부터 종료값 '직전'까지 ex) range(1,5)이면 5는 미포함 사실상 i<5 까지
range(start, stop, step) : 시작값부터 종료값 '직전'까지 지정한 간격으로

 
for i in range(1,5,2):
    print(i)

i = 1
while i < 5:
    print(i)
    i += 2
'''

# 문제 : for문으로 1부터 100까지 출력
# for i in range(1, 101):
#     print(i)

# 문제 : for문으로 100부터 1까지 출력
# for i in range(100, 0, -1):
#     print(i)


# 문제 : for문으로 구구단 1단 ~ 9단 출력

# i = 1
# while i <= 9:
#     j = 1
#     print("===== {}단 =====".format(i))
#     while j <=9:
#         print("{} X {} = {}".format(i,j,i*j))
#         j+=1
#     i+=1

# for i in range(1, 10):
#     print("======= {}단 =======".format(i))
#     for j in range(1, 10):
#         print("{} X {} = {}".format(i,j,i*j))


#============================== 함수 ==============================
'''
# 함수를 왜? 써야하는가?
# 코드 재사용: 동일한 코드를 여러 번 작성할 필요가 없음
# 중복 코드 감소: 반복되는 코드를 하나의 함수로 관리
# 유지보수: 기능을 수정할 때 함수 내부만 수정하면 된다.
# 가독성: 코드의 역할과 목적을 쉽게 파악할 수 있다.

# def 함수이름():
#       실행문
'''


# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.

# def gugudan():
#         dan = 8

#         print("== 구구단 8단 출력 ==")
#         i = 1
#         while i <= 9:
#                 print("{} * {} = {}".format(dan, i, dan * i))
#                 i += 1


'''
        매개변수/Parameter
        - 인자/인수/Argument
        전역변수
        지역변수
'''

# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.

# def gugudan(dan):
#         print("== {}단 ==".format(dan))
#         i = 1
#         while i <= 9:
#                 print("{} * {} = {}".format(dan, i, dan * i))
#                 i += 1

# 함수가 값을 가지게 하려면 딱 하나 [리턴: 반환값]
# 리턴 : 함수에서 처리한 결과를 함수 외부로 전달하고 함수의 실행을 종료시키는 키워드이다.
# def add(a, b):
#     return a + b

# x = add(10, 20)
# print(f'x : {x}')

# y = 10 + 20
# print(f'y : {y}')



# 문제 : 입력받은 정수가 소수인지 아닌지 알려주는 함수를 구현해주세요.
'''
def is_prime_number(num):
    cnt = 0
    i = 1
    for i in range(i, num+1):
        if(num % i == 0):
            cnt += 1
    if(cnt >= 3):
        print(f'{num}은 소수가 아닙니다.')
        return False
    else:
        print(f'{num}은 소수 입니다.')
        return True

some_num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for i in some_num:
    is_prime_number(i)
'''


'''
    파이썬
    -출력문
        - print(), print(f""),print("".format())
    - 변수
        - x = 10, y = 5
    - 조건문
        - if, elif, else
    - 반복문
        - while, for
    - 함수
        - 내장함수 : print(), int(), float(), format()
        - 사용자 정의 함수
            - 매개변수/인자
            - 리턴(반환값)
            - 전역변수/지역변수
'''