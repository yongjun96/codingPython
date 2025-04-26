print("251 클래스, 객체, 인스턴스")
print("클래스와 객체에 대해 설명해봅시다.")

print("클래스는 일종의 설계도로, 하나의 타입을 정의하는 방법입니다. "
      "클래스에는 관련있는 데이터와 함수를 한 데 모아 정의할 수 있습니다. "
      "클래스로 만들어진 결과물을 객체라고합니다.")

print("----------------------------------------------------------")

print("252 클래스 정의")
print("비어있는 사람 (Human) 클래스를 '정의' 해보세요.")

class Human:
    pass

print("----------------------------------------------------------")

print("253 인스턴스 생성")
print("사람 (Human) 클래스의 인스턴스를 '생성' 하고 이를 areum 변수로 바인딩해보세요.")

areum = Human()

print("----------------------------------------------------------")

print("254 클래스 생성자-1")
print("사람 (Human) 클래스에 '응애응애'를 출력하는 생성자를 추가하세요.")

class Human:
    def __init__(self):
        print("응애응애")

areum = Human()

print("def __init__(self): -> 무슨의미인지 알아봐야 함")

print("----------------------------------------------------------")

print("255 클래스 생성자-2")
print("사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.")

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


man = Human("김용준", 30, "남")

print("----------------------------------------------------------")

print("256 인스턴스 속성에 접근")
print("255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. "
      "인스턴스 변수에 접근하여 값을 출력하면 됩니다.")

print(man.name, man.age, man.gender)

print("----------------------------------------------------------")

print("257 클래스 메소드 - 1")
print("사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.")

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def whe(self):
        print(self.name, self.age, self.gender)

man = Human("김용준", 30, "남")

man.whe()

print("----------------------------------------------------------")

print("258 클래스 메소드 - 2")
print("사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.")

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def whe(self):
        print(self.name, self.age, self.gender)

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

man = Human("김용준", 30, "남")

man.setInfo("불명", 100, "불명")
man.whe()

print("----------------------------------------------------------")

print("259 클래스 소멸자")
print("사람 (human) 클래스에 '나의 죽음을 알리지 말라'를 출력하는 소멸자를 추가하세요.")

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print("나의 죽음을 적에게 알리지 마라")


    def whe(self):
        print(self.name, self.age, self.gender)

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

man = Human("김용준", 30, "남")
del man

print("----------------------------------------------------------")

print("260 에러의 원인")
print("아래와 같은 에러가 발생한 원인에 대해 설명하세요.")

# class OMG :
#     def print():
#         print("Oh my god")

print("함수명에 print()를 사용하고 함수 내용으로 print를 다시 호출하고 있음")











