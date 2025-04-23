print("201 함수")

print("'비트코인' 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.")

coin = "비트코인"

def print_coin():
    print(coin)

print("----------------------------------------------------------")

print("202 함수")
print("201번에서 정의한 함수를 호출하라.")

print_coin()

print("----------------------------------------------------------")

print("203 함수")
print("201번에서 정의한 print_coin 함수를 100번호출하라.")
count = 1
for i in range(100):
    print_coin()
    print(count)
    count += 1

print("----------------------------------------------------------")

print("204 함수")
print("'비트코인' 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.")

def print_coins():
    for i in range(100):
        print(coin)

print("----------------------------------------------------------")

print("205 함수")
print("아래의 에러가 발생하는 이유에 대해 설명하라.")

# hello()
# def hello():
#     print("Hi")

print("함수를 만들기 전에 함수를 호출했음")

print("----------------------------------------------------------")

print("206 함수")
print("아래 코드의 실행 결과를 예측하라.")

def message() :
    print("A")
    print("B")

message()
print("C")
message()

print("예상 : A B C A B")

print("----------------------------------------------------------")

print("207 함수")
print("아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)")

print("A")

def message() :
    print("B")

print("C")
message()

print("예상 : A C B")

print("----------------------------------------------------------")

print("208 함수")
print("아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)")

print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()

print("예상 : A C B E D")

print("----------------------------------------------------------")

print("209 함수")
print("아래 코드의 실행 결과를 예측하라.")

def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

print("예상 : B A")

print("----------------------------------------------------------")

print("210 함수")
print("아래 코드의 실행 결과를 예측하라.")

def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

print("예상 : B C B C B C A")

print("----------------------------------------------------------")

print("211 함수")
print("함수의 호출 결과를 예측하라.")


def function1(string) :
    print(string)

function1("안녕")
function1("Hi")

print("예측 : 안녕 Hi")

print("----------------------------------------------------------")

print("212 함수")
print("함수의 호출 결과를 예측하라.")

def function2(a, b) :
    print(a + b)

function2(3, 4)
function2(7, 8)

print("예측 : 7 15")

print("----------------------------------------------------------")

print("213 함수")
print("아래와 같은 에러가 발생하는 원인을 설명하라.")

# def function3(string) :
#     print(string)
#
# function3()

print("예측 : 파라메터가 있는데 넣어서 호출하지 않고 있음")

print("----------------------------------------------------------")

print("214 함수")
print("아래와 같은 에러가 발생하는 원인을 설명하라.")

# def function4(a, b) :
#     print(a + b)
#
# function4("안녕", 3)

print("예상 : 정수를 받아서 더하기 연산을 하고 있는데 호출할 때 문자열을 파라메터로 넣음")

print("----------------------------------------------------------")

print("215 함수")
print("하나의 문자를 입력받아 문자열 끝에 ':D' 스마일 문자열을 이어 붙여 "
      "출력하는 print_with_smile 함수를 정의하라.")

def print_with_smile(string):
    print(string + ":D")

print("----------------------------------------------------------")

print("216 함수")
print("215에서 정의한 함수를 호출하라. 파라미터는 '안녕하세요'로 입력하라.")

print_with_smile("안녕하세요")

print("----------------------------------------------------------")

print("217 함수")
print("현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.")

def print_upper_price(price):
    print(price * 1.3)

print_upper_price(50)

print("----------------------------------------------------------")

print("218 함수")
print("두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.")

def print_sum(a, b):
    print(a + b)

print_sum(5, 10)

print("----------------------------------------------------------")

print("219 함수")
print("두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.")

def print_arithmetic_operation(a, b):
    print("합 : ",a + b)
    print("차 : ",a - b)
    print("곱 : ",a * b)
    print("나누기 : ",a / b)

print_arithmetic_operation(10, 7)

print("----------------------------------------------------------")

print("220 함수")
print("세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.")

def print_max(a, b, c):
    max_val = 0
    if a > max_val:
        max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    print(max_val)

print_max(10, 8, 74)




