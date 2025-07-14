
"""
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if  height > 120 :
    print("You can ride the rollercoaster")
else :
    print("Sorry you have to grow taller before you can ride.")
"""

"""
value_input = input("값을 입력해 주세요 : ")

value_calc = int(value_input)%2

if value_calc == 0 :
    print("짝수입니다.")
else :
    print("홀수입니다.")
"""
#브라켓 씌워도 가능
"""
value1 = int(input("값은?"))
if value1 == 3 :
    {
        print("test")
    }
else :
    {
        print("out")
    }
    """

#코드 실습 테스트 1
"""
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5 :
    print("underweight")
else :
    if (bmi >= 18.5 and bmi < 25) :
        print("normal weight")
    else :
        print("overweight")
"""

#코드 실습 테스트 2
"""
import sys
bill = 0
print("Welcome to Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M or L : ")

if  size == "S" or size == "s" :
    bill += 15
elif size == "M" or size == "m" :
    bill += 20
elif size == "L" or size == "l":
    bill += 25
else : 
    print("Wrong Type")
    sys.exit()
print(str(bill))

pepperoni = input("Dow you want pepperoni on your pizza? Y or N : ")

if pepperoni == "Y" or pepperoni == "y" :
    if size == "S" or size == "s" :
        bill += 2
    else :
        bill += 3
else : 
    if pepperoni == "N" or "n" :
        bill = bill
    else :
        print("Wrong Type")
        sys.exit()

extra_cheese = input("Do you want extra cheese? Y or N : ")

if extra_cheese == "Y" or extra_cheese == "y" :
    bill += 1
else : 
    if extra_cheese == "N" or extra_cheese == "n" :
        bill = bill
    else :
        print("Wrong Type")
        sys.exit()


print("Total " + str(bill) + " Dollars")
"""


#보물섬 프로젝트 게임
project_value = "문장";

print('''
              ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.uuu.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
      
      ''')
print("Welcome 'A Tresure Hunter!!\n");
project_value = str(input('문이 앞에 두 개 있다. "오른쪽? 왼쪽?"\n'))

if project_value == "왼쪽" :
    print("\'자네'는 바닥에 떨어져 죽었구만?\n")
    exit()
else :
    print("운이 좋구만 자네는 살았어\n")

project_value = str(input("문을 열고 나가보니 물이 차있구만 그런데 문이 아래에 있어 물은 조금씩 빠지고 있는데? 어떻게 하겠나? 수영 혹은 대기\n"))

if project_value == "수영" :
    print("수영도 잘하네?\n")
else :
    print("물이 너무 천천히 빠져서 산소부족으로 사망했네.. 잘가게\n")
    exit()

project_value = str(input("물에 젖은 생쥐구만.. 마침 눈 앞에 불을 피우는 도구가 있네 불을 피울건가? 예 혹은 아니오\n"))

if(project_value == "예") :
    print("괴물들이 불빛을 보고 찾아왔네... 자네는 공격받아 죽었네\n")
    exit()
else :
    print("아니 추워도 견디는게 이상하네? 다행히 괴물들이 귀가 어두워서 자네를 찾이 못한듯 하구만\n")

project_value = str(input("주변을 보니 스위치가 세 개 있구만.. 모두 다른데 하나만 눌러보자. 세모, 네모, 동그라미\n"))
if(project_value == "세모") :
    print("쿠우우우우우웅 소리와 함께 문이 열렸다!!\n")
elif(project_value == "네모") :
    print("덜컹!! 바닥에 빠졌어!!\n")
else :
    print("찌릿! 물에 젖어서 전기가 통하니 감전되었다!\n")
    exit()

if(project_value == "세모" or project_value == "네모") :
    project_value = str(input("온 몸이 쑤시네... 이제 거의 다 온거 같은데? 문 색깔이 다르구만 어느 문을 열 텐가? 빨강, 파랑\n"))
    if(project_value == "빨강") :
        print("화염구가 당신을 덮쳤다! 당신은 죽었다\n")
        exit()
    else :
        print("드디어 보물이다!! 찾았다!!\n")
        print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
              ''')


