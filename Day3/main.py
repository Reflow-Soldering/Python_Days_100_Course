
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