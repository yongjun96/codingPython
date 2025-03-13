# 초보자를 위한 파이썬 300제

# print 기초
print("Mary's cosmetics")
print("신씨가 소리질렀다. \"도둑이야\".")
print("C:\Windows")
print("안녕하세요.\n만나서\t\t반갑습니다.") # \n -> 줄바꿈 \t -> tab
print("오늘은", "일요일") # 여러 값을 출력 하려면 ,를 사용
print("naver", "kakao", "sk", "samsung", sep=";") # sep 인자로 공백 대신 ;를 사용
print("naver", "kakao", "sk", "samsung", sep="/")
print("first", end=""); print("second") # ; -> 한줄에 여러 print 를 사용하기 위해 사용 / end="" -> 마지막 \n 의 동작을 수정
print(5/3)

# 파이썬 변수
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

시가총액 = 2980000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액), 현재가, type(현재가), PER, type(PER)) # type() -> 해당 변수의 타입을 출력

s = "hello"
t = "python"
print(s+"!",t)

print(2+2*3)

a = "132"
print(a, type(a))

num_str = "720"
print(num_str, type(num_str))
num_str = int(num_str) # int() -> 정수형 변환
print(num_str, type(num_str))

num = 100
num = str(num) # str() -> 문자열 변환
print(num, type(num))

float_str = "15.79"
float_str = float(float_str) # float() -> 실수 변환
print(float_str, type(float_str))











