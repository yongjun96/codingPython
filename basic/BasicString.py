print("021 문자열 인덱싱")
print("letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.")

string021 = "letters"

print(string021[0], string021[2])

print("----------------------------------------------------------")

print("022 문자열 슬라이싱")
print("자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.")

license_plate = "24가 2210"

# 문자열에서 여러 글자를 가져오는 것을 슬라이싱이라고 부릅니다.
# 음수 값은 문자열의 뒤에서부터 인덱싱 또는 슬라이싱함을 의미합니다.
# 슬라이싱에서 시작 인덱스를 생략하면 0으로 간주하고 끝 인덱스를 생략하면 문자열의 끝을 의미합니다.
print(license_plate[-4:])


print("----------------------------------------------------------")

print("023 문자열 인덱싱")
print("아래의 문자열에서 '홀' 만 출력하세요.")
string = "홀짝홀짝홀짝"

# 슬라이싱할 때 `시작인덱스:끝인덱스:오프셋`을 지정할 수 있습니다.
# String[start:end:step]
print(string[::2])

print("----------------------------------------------------------")

print("024 문자열 슬라이싱")
print("문자열을 거꾸로 뒤집어 출력하세요.")

string = "PYTHON"

# 기본 값으로 step 은 1이고 1은 문자열 처음부터 시작 / -1은 문자열 끝부터 시작
print(string[::-1])

print("----------------------------------------------------------")

print("025 문자열 치환")
print("아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.")

phone_number = "010-1111-2222"

phone_number_replace = phone_number.replace("-", " ")

print(phone_number_replace)

print("----------------------------------------------------------")

print("026 문자열 다루기")
print("25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.")

phone_number_replace = phone_number.replace("-", "")

print(phone_number_replace)

print("----------------------------------------------------------")

print("027 문자열 다루기")
print("url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.")

url = "http://sharebook.kr"

url_split = url.split('.')
print(url_split[-1])

print("----------------------------------------------------------")

print("028 문자열은 immutable")
print("아래 코드의 실행 결과를 예상해보세요.")

lang = 'python'
# lang[0] = 'P'
# print(lang)

print("문자열은 수정할 수 없습니다. 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.")

print("----------------------------------------------------------")

print("029 replace 메서드")
print("아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.")

string = 'abcdfe2a354a32a'
string_replace = string.replace("a", "A")

print(string_replace)

print("----------------------------------------------------------")

print("030 replace 메서드")
print("아래 코드의 실행 결과를 예상해보세요.")

string = 'abcd'
string.replace('b', 'B')
print(string)
print("문자열은 변경할 수 없다. 다른 변수에 저장을 시키는 것 뿐 변환은 되지 않는다.")











