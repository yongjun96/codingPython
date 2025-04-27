import random
from turtledemo.paint import switchupdown

from basic.BasicString import name1

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

print("----------------------------------------------------------")

print("261 Stock 클래스 생성")
print("주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의해보세요. "
      "클래스는 속성과 메서드를 갖고 있지 않습니다.")

class Stock:
    pass

print("----------------------------------------------------------")

print("262 생성자")
print("Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.")

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

samSung = Stock("삼성", "ss0001")
print(samSung.name, samSung.code)

print("----------------------------------------------------------")

print("263 메서드")
print("객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.")

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

stock = Stock("none", "none")
stock.set_name("LG")
print(stock.name)

print("----------------------------------------------------------")

print("264 메서드")
print("객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.")

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_code(self, code):
        self.code = code

stock = Stock("none", "none")
stock.set_code("lg0001")
print(stock.code)

print("----------------------------------------------------------")

print("265 메서드")
print("종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. "
      "해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.")

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
       return self.code

stock = Stock("LG", "lg0001")

print(stock.get_name())

print("----------------------------------------------------------")

print("266 객체의 속성값 업데이트")
print("생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 "
      "입력 받을 수 있도록 생성자를 수정하세요. "
      "PER, PBR, 배당수익률은 float 타입입니다.")


class Stock:
    def __init__(self, name, code, per, pbr, dividend_yield):
        self.name = name
        self.code =code
        self.per = per
        self.pbr = pbr
        self.dividend_yield = dividend_yield

print("----------------------------------------------------------")

print("267 객체 생성")
print("266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.")
print(
    "항목	정보",
    "종목명	삼성전자",
    "종목코드	005930"
    "PER	15.79",
    "PBR	1.33",
    "배당수익률	2.83"
)

class Stock:
    def __init__(self, name, code, per, pbr, dividend_yield):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend_yield = dividend_yield

    def list(self):
        list = {}
        list.pop("항목", "정보")
        list.pop("종목명", self.name)
        list.pop("종목코드", self.code)
        list.pop("PER", self.per)
        list.pop("PBR", self.pbr)
        list.pop("배당수익률", self.dividend_yield)
        return list

stock = Stock("삼성전자", "005930", "15.79", "1.33", "2.83")
stock.list()

print("----------------------------------------------------------")

print("268 객체의 속성 수정")
print("PER, PBR, 배당수익률은 변경될 수 있는 값입니다. "
      "이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.")

class Stock:
    def __init__(self, name, code, per, pbr, dividend_yield):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend_yield = dividend_yield

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend_yield):
        self.dividend_yield = dividend_yield

print("----------------------------------------------------------")

print("269 객체의 속성 수정")
print("267번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요.")

stock = Stock("삼성전자", "005930", "15.79", "1.33", "2.83")
stock.set_per("12.75")
print(stock.per)


print("----------------------------------------------------------")

print("270 여러 종목의 객체 생성")
print("아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요. "
      "파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.")

print(
    "종목명	종목코드	PER	PBR	배당수익률",
    "삼성전자 005930	15.79	1.33	2.83",
    "현대차	005380	8.70	0.35	4.27",
    "LG전자	066570	317.34	0.69	1.37"
)

stock_samSung = Stock("삼성전자", "005930", "15.79", "1.33", "2.83")
stock_hyundai = Stock("현대차", "005380", "8.70", "0.35", "4.27")
stock_lg = Stock("LG전자", "066570", "317.34", "0.69", "1.37")

list = []

list.append(stock_samSung)
list.append(stock_hyundai)
list.append(stock_lg)

for i in list:
    print(i.code, i.per)

print("----------------------------------------------------------")

print("271 Account 클래스")
print("은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 "
      "생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다. "
      "은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.")


class Account:

    account_count = 0


    def __init__(self, name, default_money):
        self.name = name
        self.default_money = default_money
        self.bank_name = "SC은행"
        self.deposit_count = 0
        self.deposit_history = []
        self.withdraw_history = []
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    def account_info(self):
        print(
            "예금주 명 : ", self.name, "\n"
            f"잔액 :  {self.default_money:,}", "\n"
            "은행 : ", self.bank_name, "\n"
            "계좌번호 : ", self.account_number
            )


    def deposit(self, add_money):
        if add_money >= 1:
            self.default_money += add_money
            self.deposit_count += 1
            self.deposit_history.append(add_money)
        if self.deposit_count % 5 == 0:
            print(self.default_money * 0.01)
            self.default_money += self.default_money * 0.01
            self.deposit_history.append(self.default_money * 0.01)

    def withdraw(self, del_money):
        if self.default_money >= del_money:
            self.default_money -= del_money
            self.withdraw_history.append(del_money)

    @classmethod # 클래스 내부에서 사용되는 메소드를 지정
    def get_account_num(cls):
        print(cls.account_count)

kim = Account("김용준", 10000)
kim.account_info()

print("----------------------------------------------------------")

print("272 클래스 변수")
print("클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.")

print(kim.account_count)

print("----------------------------------------------------------")

print("273 클래스 변수 출력")
print("Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.")

kim.get_account_num()

print("----------------------------------------------------------")

print("274 입금 메서드")
print("Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.")

kim.deposit(10000)
kim.account_info()

print("----------------------------------------------------------")

print("275 출금 메서드")
print("Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.")

kim.withdraw(10000)
kim.account_info()

print("----------------------------------------------------------")

print("276 정보 출력 메서드")
print("Account 인스턴스에 저장된 정보를 출력하는 account_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.")

kim.deposit(10000)
kim.account_info()

print("----------------------------------------------------------")

print("277 이자 지급하기")
print("입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.")

kim.deposit(10000)
kim.deposit(10000)
kim.deposit(10000)
kim.deposit(10000)
kim.deposit(10000)
kim.account_info()

print("----------------------------------------------------------")

print("278 여러 객체 생성")
print("Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.")

account_list = []

kim = Account("김용준", 1000000)
min = Account("민동수", 20000)
park = Account("박민수", 30000)

account_list.append(kim)
account_list.append(min)
account_list.append(park)

print(account_list)

print("----------------------------------------------------------")

print("279 객체 순회")
print("반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.")

for account in account_list:
    if account.default_money >= 1000000:
       account.account_info()

print("----------------------------------------------------------")

print("280 입출금 내역")
print("입금과 출금 내역이 기록되도록 코드를 업데이트 하세요."
      " 입금 내역과 출금 내역을 출력하는 "
      "deposit_history와 withdraw_history 메서드를 추가하세요.")

kim.deposit(1000000)
kim.deposit(2154987)
kim.deposit(23123542)

kim.withdraw(321254)
kim.withdraw(122354)
kim.withdraw(1223)
kim.withdraw(132455)

print("입금 내역 : ", kim.deposit_history)
print("출금 내역 : ", kim.withdraw_history)

print("----------------------------------------------------------")

print("281 클래스 정의")
print("다음 코드가 동작하도록 차 클래스를 정의하세요.")
print(
    ">> car = 차(2, 1000)",
    ">> car.바퀴",
    "2",
    ">> car.가격",
    "1000"
)

class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

    def get_wheel(self):
        print(self.wheel)

    def get_price(self):
        print(self.price)


car = Car(4, 100000)
car.get_wheel()
car.get_price()

print("----------------------------------------------------------")

print("282 클래스 상속")
print("차 클래스를 상속받은 자전차 클래스를 정의하세요.")

class Bicycle(Car):
    def __init__(self, wheel, price, drivetrain):
        super().__init__(wheel, price)
        self.drivetrain = drivetrain

    def get_drivetrain(self):
        print(self.drivetrain)

    def get_info(self):
        print(self.wheel, self.price, self.drivetrain)

print("----------------------------------------------------------")

print("283 클래스 상속")
print("다음 코드가 동작하도록 자전차 클래스를 정의하세요. "
      "단 자전차 클래스는 차 클래스를 상속받습니다.")

# bicycle = Bicycle(2, 1000)
# bicycle.get_wheel()
# bicycle.get_price()

print("----------------------------------------------------------")

print("284 클래스 상속")
print("다음 코드가 동작하도록 자전차 클래스를 정의하세요. "
      "단 자전차 클래스는 차 클래스를 상속받습니다.")
print(
    ">> bicycle = 자전차(2, 100, \"시마노\")",
    ">> bicycle.구동계",
    "시마노"
)

bicycle = Bicycle(2, 100, "시마노")
bicycle.get_drivetrain()

print("----------------------------------------------------------")

print("285 클래스 상속")
print("다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.")

print(
    ">> car = 자동차(4, 1000)",
    " >> car.정보()",
    "바퀴수 4",
    "가격 1000"
)

class Automobile(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

    def info(self):
        print(self.wheel, self.price)

car = Automobile(2, 1000)
car.info()

print("----------------------------------------------------------")

print("286 부모 클래스 생성자 호출")
print("다음 코드가 동작하도록 차 클래스를 수정하세요.")

bicycle = Bicycle(2, 100, "시마노")
bicycle.get_price()
bicycle.get_wheel()


print("----------------------------------------------------------")

print("287 부모 클래스 메서드 호출")
print("자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.")

bicycle.get_info()

print("----------------------------------------------------------")

print("288 메서드 오버라이딩")
print("다음 코드의 실행 결과를 예상해보세요.")

class parents:
    def get(self):
        print("부모호출")

class child(parents):
    def get(self):
        print("자식호출")

me = child()
me.get()

print("예상 : 자식호출")

print("----------------------------------------------------------")

print("289 생성자")
print("다음 코드의 실행 결과를 예상해보세요.")

class parents:
    def __init__(self):
        print("부모생성")

class child(parents):
    def __init__(self):
        print("자식생성")

me = child()

print("예상 : 자식생성")

print("----------------------------------------------------------")

print("290 부모클래스 생성자 호출")
print("다음 코드의 실행 결과를 예상해보세요.")

class parents:
    def __init__(self):
        print("부모생성")

class child(parents):
    def __init__(self):
        print("자식생성")
        super().__init__()

me = child()

print("예상 : 자식생성 부모생성")

