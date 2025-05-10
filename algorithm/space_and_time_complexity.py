# 시간 복잡도 & 공간 복잡도

# 점근 표기법 (asymptotic notation)
# - 어떤 함수의 가 양상을 다른 함수와의 비교로 표 (수론 & 해석학)
# ex). N정도의 시간과 공간이 걸리겠구나 했던게 점근 표기법의 일종
# 빅오 표기법, 빅 오메가 표기법
# - 빅오 : 최악의 성능이 나올 때 어느 정도의 연산량이 나오는지
# - 빅오메가 : 최선의 성능이 나올 때 어느 정도의 연산량이 나오는지

print("문제 풀어보기")

print("Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때, "
      "왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 '✕' 혹은 '+' 연산자를 넣어 "
      "결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오.단, "
      "'+' 보다 '✕' 를 먼저 계산하는 일반적인 방식과는 달리, "
      "모든 연산은 왼쪽에서 순서대로 이루어진다.")

def find_max_plus_or_multiply(array):
    sum = 0                         # 대입 연산
    for num in array:               # N의 길이 만큼 반복 O(N) )
        if sum <= 1 or num <= 1:    # 비교
            sum += num              # 대입
        else:                       # 비교
            sum *= num              # 대입
    return sum

# 해당 함수의 빅오 표기법 -> O(N)

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))
print("정답 = 3 현재 풀이 값 =", result([0,0,0,1,2]))

print("----------------------------------------------------------------")

print("Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, "
      "이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.")

# 빅오 표기법 : O(N^2)
# 비효율적
# - 이런 경우 공간 복잡도를 사용해서 시간복잡도를 줄여야 함
# def find_not_repeating_first_character(string):
#     for str in string:
#         match = 0
#         for str2 in string:
#             if str == str2:
#                 match += 1
#         if match == 1:
#             return str
#     return "_"

# 빅오 표기법 : O(N)
# 효율적
# - 공간 복잡도를 이용해서 시간 복잡도의 제곱을 사용하지 않고 해결
def find_not_repeating_first_character(string):
    english_list = [0] * 26
    for str in string:
        index = ord(str) - int(ord('a'))
        english_list[index] += 1

    for str in string:
        english_index = ord(str) - ord('a')
        if english_list[english_index] == 1:
            return str
    return "_"

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))

print("----------------------------------------------------------------")

print("Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오."
      "소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.")

input = 20

def find_prime_list_under_number(number):
    number_list = []
    for num in range(2, number+1):
        if num <= 3:
            number_list.append(num)
        elif num % 3 != 0 and num % 2 != 0:
            number_list.append(num)
    return number_list

result = find_prime_list_under_number(input)
print("정답 : [2, 3, 5, 7, 11, 13, 17, 19] / 답 :", result)

print("소수는 2와 3을 포함하고 2와 3으로 나누었을 때 나머지가 남는 수의 집합")

print("----------------------------------------------------------------")

print("Q. 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다. "
      "할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다."
      "예를 들어 S=0001100 일 때, 전체를 뒤집으면 1110011이 된다."
      "4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다."
      "하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다."
      "주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.")

input = "011110"
input = "01101010110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):

    return 1


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)