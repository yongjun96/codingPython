import csv
from asyncore import write

print("291 파일 쓰기")
print("바탕화면에 '매수종목1.txt' 파일을 생성한 후 다음과 같이 종목코드를 파일에 써보세요.")

f = open("C:/Users/pract/OneDrive/바탕 화면/매수종목1.txt", mode="wt", encoding="utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420\n")
f.close()

print("----------------------------------------------------------")

print("292 파일 쓰기")
print("바탕화면에 '매수종목2.txt' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요.")

f = open("C:/Users/pract/OneDrive/바탕 화면/매수종목2.txt", mode="wt", encoding="utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER\n")
f.close()

print("----------------------------------------------------------")

print("293 CSV 파일 쓰기")
print("바탕화면에 '매수종목.csv' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요. 인코딩은 'cp949'를 사용해야합니다.")

f = open("C:/Users/pract/OneDrive/바탕 화면/매수종목.csv", mode="wt", encoding="'cp949", newline='')

write = csv.writer(f)
write.writerow(["종목명", "종목코드", "PER"])
write.writerow(["삼성전자", "005930", "15.79"])
write.writerow(["NAVER", "035420", "55.82"])
f.close()

print("----------------------------------------------------------")

print("294 파일 읽기")
print("바탕화면에 생성한 '매수종목1.txt' 파일을 읽은 후 종목코드를 리스트에 저장해보세요.")

f = open("C:/Users/pract/OneDrive/바탕 화면/매수종목1.txt", encoding="utf-8")

lines = f.readlines()

codes = []
for line in lines:
    code = line.strip()
    codes.append(code)

print(codes)

f.close()

print("----------------------------------------------------------")

print("295 파일 읽기")
print("바탕화면에 생성한 '매수종목2.txt' 파일을 읽은 후 종목코드와 종목명을 딕셔너리로 저장해보세요. "
      "종목명을 key로 종목명을 value로 저장합니다.")

print("strip() -> '\\n' 제거")

f = open("C:/Users/pract/OneDrive/바탕 화면/매수종목2.txt", encoding="utf-8")

lines = f.readlines()
dic = {}

for line in lines:
     code, name = line.strip().split(" ")
     print(code, name)
     dic[name] = code

print(dic.keys())
print(dic.values())

print("----------------------------------------------------------")

print("296 예외처리")
print("문자열 PER (Price to Earning Ratio) 값을 실수로 변환할 때 에러가 발생합니다. "
      "예외처리를 통해 에러가 발생하는 PER은 0으로 출력하세요.")

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

print("----------------------------------------------------------")

print("297 예외처리 및 리스트에 저장")
print("문자열로 표현된 PER 값을 실수로 변환한 후 이를 새로운 리스트에 저장해보세요.")

per = ["10.31", "", "8.00"]
float_list = []

for i in per:
    try:
        float_list.append(float(i))
    except:
        float_list.append(0)

print(float_list)

print("----------------------------------------------------------")

print("298 특정 예외만 처리하기")
print("어떤 값을 0으로 나누면 ZeroDivisionError 에러가 발생합니다. "
      "try ~ except로 모든 에러에 대해 예외처리하지 말고 ZeroDivisionError 에러만 예외처리해보세요.")

num = 10

try:
    print("성공 케이스 :", num / 0)
except ZeroDivisionError:
    print("예외케이스 :", 0)

print("----------------------------------------------------------")

print("299 예외의 메시지 출력하기")
print("다음과 같은 코드 구조를 사용하면 예외 발생 시 에러 메시지를 변수로 바인딩할 수 있습니다.")

data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
       print(e)

print("----------------------------------------------------------")

print("300 try, except, else, finally 구조 사용해보기")
print("파이썬 예외처리는 다음과 같은 구조를 가질 수 있습니다.")
print(
    "try:",
        "실행 코드",
    "except:",
        "예외가 발생했을 때 수행할 코드",
    "else:",
        "예외가 발생하지 않았을 때 수행할 코드",
    "finally:",
        "예외 발생 여부와 상관없이 항상 수행할 코드"
)

print("아래의 코드에 대해서 예외처리를 사용하고 "
      "try, except, else, finally에 적당한 코드를 작성해봅시다. "
      "else와 finally는 적당한 문구를 print하시면 됩니다.")

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("출력 완료")