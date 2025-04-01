
print("081 별 표현식")
print("기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. \n"
      "하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. \n"
      "튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 \n"
      "나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.")

print("다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, \n"
      " start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.")

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

# valid_score = scores[0:8:]
*valid_score, _, _ = scores

print(valid_score)
print("저장 시킬 변수 앞에 *를 붙이고 값을 비우는 경우 _, 를 사용해서 지움")

print("----------------------------------------------------------")

print("082 별 표현식")
print("다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, \n"
      "start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.")

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

#_, _, *valid_score = scores
a, b, *valid_score = scores

print(valid_score)
print("a 와 b 를 사용해서 값을 받아 놓고 나머지를 저장")

print("----------------------------------------------------------")

print("083 별 표현식")
print("다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, \n"
      " start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.")

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

_, *valid_score, _ = scores

print(valid_score)

print("----------------------------------------------------------")

print("084 비어있는 딕셔너리")
print("temp 이름의 비어있는 딕셔너리를 만들라.")

temp = {}

print(temp)
print("딕셔너리는 {} 사용")

print("----------------------------------------------------------")

print("085 딕셔너리")
print("다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.")

ice_cream = {"메로나": 1000, "폴라포": 1200 , "빵빠레": 1800}

print(ice_cream, type(ice_cream))
print("json과 비슷한 형식으로 값의 쌍을 이뤄주면 됨 :를 사용")

print("----------------------------------------------------------")

print("086 딕셔너리 값 추가")
print("085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.")

ice_cream["죠스바"] = 1200
ice_cream["월드콘"] = 1500

print(ice_cream)
print("앞의 값을 key값으로 이용해서 해당 값에 value를 추가하는 형식")

print("----------------------------------------------------------")

print("087 딕셔너리 출력")
print("다음 딕셔너리를 사용하여 메로나 가격을 출력하라.")

ice_cream = {
    '메로나': 1000,
    '폴로포': 1200,
    '빵빠레': 1800,
    '죠스바': 1200,
    '월드콘': 1500
}

print(ice_cream["메로나"])

print("----------------------------------------------------------")

print("088 딕셔너리 값 수정")
print("다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.")

ice_cream["메로나"] = 1300

print(ice_cream["메로나"])

print("----------------------------------------------------------")

print("089 딕셔너리 삭제")
print("다음 딕셔너리에서 메로나를 삭제하라.")

del ice_cream["메로나"]

print(ice_cream)

print("----------------------------------------------------------")

print("090 딕셔너리 에러 해결")
print("다음 코드에서 에러가 발생한 원인을 설명하라.")

icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']

print("누가바는 디셔너리에 없기 때문")
