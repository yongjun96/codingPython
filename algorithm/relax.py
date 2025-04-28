# 가장 큰 수를 반환

num_array = [3,5,6,1,2,4]
num_array2 = [6,6,6]
num_array3 = [6,9,2,7,1888]

# 방법 1
def find_max_num(array):
    max_num = 0
    for num in array:
        if max_num <= num:
            max_num = num
    return max_num

# 방법 2
def max_num(array):
    return max(array)

print("정답 = 6 / 현재 풀이 값 =", find_max_num(num_array))
print("정답 = 6 / 현재 풀이 값 =", find_max_num(num_array2))
print("정답 = 1888 / 현재 풀이 값 =", max_num(num_array3))


# Q. 다음과 같은 문자열을 입력받았을 때,
# 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오.
# (단 최빈값을 가진 알파벳이 여러개일 경우 알파벳 순서가 가장 앞에 위치한 알파벳을 출력하시오)

# 1. 문자인지 확인하는 법 -> isalpha()
# 2. 아스키 코드로 문자를 저장 -> ord('a') == 97
# - 알파벳은 97 == a / 98 == b 와 같이 순서대로 저장 됨
# - 즉, 97 - 97 = a(0) / 98 - 97 = b(1)
# 3. 아스키 코드를 문자로 변환 -> chr(97) == a

def find_max_occurred_alphabet(string):

    alpha_list = [0] * 26
    for alph in string:
        if alph.isalpha() is True:
            alpha_list[ord(alph) - ord('a')] += 1

    max_alph = 0
    save_alph = 0
    count = 0
    for i in alpha_list:
        if max_alph < i:
            max_alph = i
            save_alph = ord('a') + count
            print(save_alph)
        count += 1

    print(alpha_list)
    return chr(save_alph)


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))