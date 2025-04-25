import time
from pickle import PROTO

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

print("----------------------------------------------------------")

print("221 함수")
print("입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.")

def print_reverse(str):
    print(str[::-1])

print_reverse("python")

print("----------------------------------------------------------")

print("222 함수")
print("성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.")

# def print_score(list):
#     sum = 0
#     for num in list:
#         sum += num
#     print(sum / len(list))

def print_score(score_list) :
    print(sum(score_list)/len(score_list))

print_score ([1, 2, 3])

print("----------------------------------------------------------")

print("223 함수")
print("하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.")

def print_even(list):
    for num in list:
        if num % 2 == 0:
            print(num)

print_even ([1, 3, 2, 10, 12, 11, 15])

print("----------------------------------------------------------")

print("224 함수")
print("하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.")

def print_keys(dic):
    for key in dic.keys():
        print(key)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

print("----------------------------------------------------------")

print("225 함수")
print("my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.")

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

print("my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.")

# def print_value_by_key(dic, date):
#     for key in dic.keys():
#         if key == date:
#             for val in dic[key]:
#                 print(val)

def print_value_by_key(dic, date):
    print(dic[date])

print_value_by_key(my_dict, "10/26")

print("----------------------------------------------------------")

print("226 함수")
print("입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.")

start = time.time()

# 실행 시간: 0.273265초 (100000개 기준)
# def print_5xn(str):
#     str_save = ""
#     for i in range(int(len(str))):
#         str_save += str[i]
#         if (i+1) % 5 == 0:
#             print(str_save)
#             str_save = ""


# 실행 시간: 0.216017초 (100000개 기준)
# def print_5xn(str):
#     split_num = int(len(str)) / 5
#     for i in range(int(split_num)):
#         print(str[i * 5 : i * 5 + 5])

# 실행 시간: 0.206974초 (100000개 기준)
def print_5xn(s):
    for i in range(0, len(s), 5):
        print(s[i:i+5])

print_5xn("아이엠어보이유알어걸" * 100000)

end = time.time()

print(f"실행 시간: {end - start:.6f}초")

print("----------------------------------------------------------")

print("227 함수")
print("문자열과 한줄에 출력될 글자 수를 입력을 받아 "
      "한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.")

def printmxn(str, count):
    for i in range(0, len(str), count):
        print(str[i:i+count])

printmxn("아이엠어보이유알어걸", 3)

print("----------------------------------------------------------")

print("228 함수")
print("연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) "
      "함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.")

def calc_monthly_salary(annual_salary):
    num = int(annual_salary / 12)
    return num

print(calc_monthly_salary(12000000))

print("----------------------------------------------------------")

print("229 함수 바인딩")
print("아래 코드의 실행 결과를 예측하라.")

def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

print("예측 : 왼쪽: 100 오른쪽: 200")

print("----------------------------------------------------------")

print("230 함수 바인딩")
print("아래 코드의 실행 결과를 예측하라.")

def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

print("예측 : 왼쪽: 200 오른쪽: 100")

print("----------------------------------------------------------")

print("231 함수")
print("아래 코드를 실행한 결과를 예상하라.")

# def n_plus_1 (n) :
#     result = n + 1
#
# n_plus_1(3)
# print (result)

print("예측 : 변수가 함수 안에 선언되어 에러 발생")

print("----------------------------------------------------------")

print("232 함수")
print("문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.")

def make_url(str):
    return "www."+str+".com"

print(make_url("naver"))

print("----------------------------------------------------------")

print("233 함수")
print("문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.")

def make_list(str):
    list = []
    for i in range(len(str)):
        list.append(str[i])
    return list

print(make_list("abcd"))

print("----------------------------------------------------------")

print("234 함수")
print("숫자로 구성된 하나의 리스트를 입력받아, "
      "짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.")

def pickup_even(list):
    my_list = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            my_list.append(list[i])
    return my_list

print(pickup_even([3, 4, 5, 6, 7, 8]))

print("----------------------------------------------------------")

print("235 함수")
print("콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.")

def convert_int(str):
    replace_str = str.replace(",", "")
    return int(replace_str)


print(convert_int("1,234,567"))

print("----------------------------------------------------------")

print("236 함수")
print("아래 코드의 실행 결과를 예측하라.")

def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

print("예측 : 22")

print("----------------------------------------------------------")

print("237 함수")
print("아래 코드의 실행 결과를 예측하라.")

def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

print("예측 : 22")

print("----------------------------------------------------------")

print("238 함수")
print("아래 코드의 실행 결과를 예측하라.")

def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

print("예측 : 140")

print("----------------------------------------------------------")

print("239 함수")
print("아래 코드의 실행 결과를 예측하라.")

def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

print("예측 : 16")

print("----------------------------------------------------------")

print("240 함수")
print("아래 코드의 실행 결과를 예측하라.")

def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

print("예측 : 28")
