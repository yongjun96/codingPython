import datetime
import time
from os import getcwd, rename
from time import strftime, strptime
import numpy

print("241 현재시간")
print("datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.")

date = datetime.datetime.now()

print(date)

print("----------------------------------------------------------")

print("242 현재시간의 타입")
print("datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.")

print(type(datetime.datetime.now()))

print("----------------------------------------------------------")

print("243 timedelta")
print("datetime 모듈의 timedelta를 사용해서 오늘로부터 "
      "5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.")

for day in range(1, 6):
    del_day = datetime.timedelta(day)
    print(datetime.datetime.now() - del_day)

print("----------------------------------------------------------")

print("244 strftime")
print("현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. "
      "strftime 메서드를 사용하세요.")

now = datetime.datetime.now()

print(now.strftime("%H:%M:%S"))

print("----------------------------------------------------------")

print("245 strptime")
print("datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 "
      "시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "
      "'2020-05-04'의 문자열을 시간 타입으로 변환해보세요.")

date = "2025-04-25"

ret = datetime.datetime.strptime(date, "%Y-%m-%d")

print(ret, type(ret))

print("----------------------------------------------------------")

print("246 sleep 함수")
print("time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.")

# while True:
#     now = datetime.datetime.now()
#     time.sleep(1)
#     print(now)

print("----------------------------------------------------------")

print("247 모듈 임포트")
print("모듈을 임포트하는 4가지 방식에 대해 설명해보세요.")

# import module
# import module as name
# from module import function_name
# from module import *

print("----------------------------------------------------------")

print("248 os 모듈")
print("os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.")

print(getcwd())

print("----------------------------------------------------------")

print("249 rename 함수")
print("바탕화면에 텍스트 파일을 하나 생성한 후 "
      "os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.")

# rename("C:/Users/pract/OneDrive/바탕 화면/test.txt",
#        "C:/Users/pract/OneDrive/바탕 화면/complete.txt")

print("----------------------------------------------------------")

print("250 numpy")
print("numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.")

for i in numpy.arange(0, 5, 0.1):
    print(i)




