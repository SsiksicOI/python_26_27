'''
    모듈화 라이브러리

    모듈: 함수, 변수, 클래스 등을 작성해 놓은 파이썬 파일
    import 모듈이름

    패키지: 관련된 모듈을 묶어 관리하는 구조

    라이브러리: 특정 기능을 쉽게 사용할 수 있도록 미리 작성된 코드의 모음

    라이브러리
        패키지 A
            모듈 1
            모듈 2
            모듈 3

    # 직접 생성한 모듈 불러오기
    # import ex1 # 여기 안에 있는 모든걸 다 불러오기
    from ex1 import funA, funB # 선택적으로 불러오기
    print(funA(), funB())

    모듈 종류

        수학 모듈
        수학 계산 기능을 제공하는 모듈
        제곱근, 삼각함수, 원주율 등을 포함
        ex) import math
            print(math.sqrt(16)) # 16의 제곱근 계산
            print(math.pow(2,3)) # 2의 3제곱 계산

        난수 모듈
        무작위 값을 생성하는 모듈
        게임, 추천, 테스트 데이터에 사용
        ex) import random
            print(random.randint(1, 100)) # 1부터 100까지 중 랜덤한 숫자 1개 출력

        날짜/시간 모듈
        날짜와 시간을 다루는 모듈
        현재 시간 확인, 날짜 계산 사용
        ex) import datetime
            print(datetime.datetime.now()) # 현재 날짜와 시간을 출력

        시간 제어 모듈
        시간 흐름을 제어하는 모듈
        프로그램을 잠시 멈출 때 사용
        ex) import time
            time.sleep(3) # 프로그램을 3초 동안 멈춤
            print('3초 후 실행') # 3초가 지난 후 출력

        시스템 모듈
        파이썬 실행 환경을 다루는 모듈
        ex) import sys
            print(sys.version) # 현재 사용중인 파이썬 버전 출력

        운영체제 모듈
        운영체제(OS)와 관련된 기능 제공
        파일/폴더 경로 처리에 사용
        ex) import os
            print(os.getcwd()) # 현재 작업중인 폴더 경로 출력

        데이터 형식 모듈
        JSON형식으로 데이터를 변환
            - JSON : 데이터를 약속된 모양으로 적는 방식("key" : "value")
        웹, API 저장에 사용
            - API : 프로그램끼리 대화하는 방법(규칙)
        ex) import json
            data = {
                'name' : 'jin',
                'age' : 22
            }

            print(json.dumps(data))

        정규표현식 모듈
        문자열 패턴 검사 모듈
        형식 확인(아이디, 이메일)에 사용
        ex) import re
            print(bool(re.match('hi', 'hi python'))) # 문자열이 hi로 시작하는지 확인

        CSV 파일 모듈
        CSV(엑셀) 파일을 읽고 쓰는 모듈
        데이터 저장/분석 기초에 사용
        ex) import csv
            # CSV 파일에 한 줄 데이터를 저장
            with open('test2.csv', 'w', newline='') as f:
                csv.writer(f).writerow(['name', 'score'])

        자료구조 모듈
        자료구조를 편하게 쓰도록 도와줌
        카운트, 큐, 딕셔너리 확장 기능 제공
        ex) from collections import Counter
            print(Counter('apple')) # 문자열에서 각 글자의 개수를 셈
'''

'''
    유니코드:
        전 서계의 문자와 기호를 컴퓨터에서 일관되게 표현하기 위한 국제 문자 표준
'''
# Python 유니코드 / 인코딩 핵심 정리

text = '파이썬'

print(text) # 문자열 출력
print(len(text)) # 문자열 길이

# 문자 <-> 숫자 / 변환
print(ord('가')) # 문자를 유니코드 숫자로 변환
print(chr(44032)) # 유니코드를 다시 문자로 변환

# 인코딩
# Encode : 문자열을 바이트(byte)로 바꾸는 작업
# 파일 저장이나 네트워크 전송 시 사용됨
encoded = text.encode('utf-8')
print(encoded)
print(type(encoded))

# decode : 인코딩의 반대과정 / 문자열로 다시 복원
decoded = encoded.decode('utf-8')
print(decoded)
print(type(decoded))

# 인코딩이 맞지 않으면 오류 발생
try:
    wrong = encoded.decode('cp949')
    print(wrong)
except UnicodeDecodeError:
    print('인코딩 방식이 맞지 않아 오류 발생')



# 클로저(Closure) 데코레이터(Decorator)

# 클로저 : 내부 함수가 자신이 정의된 외부 함수의 변수들을 기억하고, 외부 함수의 실행이 끝난 후에도 해당 변수를 사용할 수 있는 구조

print('==== 1단계: 함수 안에 함수 만들기 ====')
def outer():
    print("outer 함수가 실행되었습니다.")

    def inner():
        print('inner 함수가 실행되었습니다.')

    return inner # 함수 자체를 반환
#   return inner() # 함수를 실행하고 그 결과를 반환

func = outer() 
func()

print('\n==== 2단계: 클로저 ====')
# 클로저는 '외부 함수의 변수를 기억하는 내부 함수'
def make_multiplier(x):
    # x는 make_multiplier 함수의 지역 변수

    def multiplier(n):
        # 내부 함수 multiplier는
        # 바깥 함수의 변수 x를 사용할 수 있다.
        return x * n

    return multiplier
    
times3 = make_multiplier(3)
print(times3(10))
print(times3(5))

print('\n==== 3단계: 데코레이터 기본 구조 ====')

# 데코레이터는 '함수를 꾸며주는 함수'
# 내부 구조는 클로저와 매우 유사

def decorator(func):
    # func는 꾸며줄 함수

    def wrapper():
        print('함수 실행 전')
        func()
        print('함수 실행 후')

    return wrapper

@decorator
def say_hello():
    print('안녕하세요')

say_hello()

print('\n==== 4단계: 매개변수가 있는 데코레이터 ====')

def decorator_width_args(func):
    def wrapper(name):
        print('실행 전')
        func(name)
        print('실행 후')
        
    return wrapper

@decorator_width_args
def say_name(name):
    print('이름 :', name)

say_name('홍길동')



print('==== 변수 어노테이션 ====')
# 기본 변수
age = 30

# 어노테이션 추가
# 변수이름: 자료형 = 값
age: int = 30

print(age)


print('\n==== 함수 어노테이션 ====')
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 5))
print(add('3', '5'))


print('\n==== 리스트, 딕셔너리 어노테이션 ====')

# 리스트 안에 int가 들어간다는 의미
nums = list[int] = [1, 2, 3]

# 딕셔너리 타입 지정
person: dict[str, int] = {
    'age': 30,
    'height': 170
}