#for loop example

"""
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits)
"""

#for 문인데 좀 헷갈림
"""
student_scores = [158, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 200, 100, 120, 150, 175, 180]

total_exam_score = sum(student_scores)

print("Total exam score: " + str(total_exam_score))

sum = 0
for score in student_scores:
    sum += score

print("Total exam score: " + str(sum))

max_score = max(student_scores)

print("Max exam score: " + str(max_score))

max_score = 0
for score in student_scores:
    if score > max_score :
        max_score = score

print("Max exam score: " + str(max_score))

min_score = 0
for score in student_scores:
    if score != 0 and min_score == 0 :
        min_score = score
    elif score < min_score :
        min_score = score
print("Min exam score: " + str(min_score))
"""

#for loop with range
# C language for(inti)
"""
Total_Sum = 0
reverse_number = 100
for number in range(1, 101, 1):
        if(reverse_number !=0) :
            print(number)
            print(reverse_number)
            Total_Sum += (number + reverse_number)
            reverse_number -= 1
print(int((Total_Sum/2)))
"""
#뭔가 이상한데
"""
Total_Sum = 0
for number in range(1, 101, 1):
      Total_Sum += number
print(Total_Sum)
"""

#코드 실습 1
#1. 1부터 100까지의 숫자를 출력해야 하며, 100 포함임
#2. 3으로 나누어 떨어지면 "Fizz"를 출력해야 함
#3. 5로 나누어 떨어지면 "Buzz"를 출력해야 함
"""
for number in range(1,101):
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%3 == 0 and number%5 != 0:
        print("Fizz")
    elif number%3 != 0 and number%5 == 0:
        print("Buzz")
    else:
        print(number)
"""


#Test
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
"""
Password = ""
for nr_letters in range(1, nr_letters +1) :
    Password += random.choice(letters)
for nr_symbols in range(1, nr_symbols +1) :
    Password += random.choice(symbols)
for nr_numbers in range(1, nr_numbers +1) :
    Password += random.choice(numbers)

print("Password : " + Password)
   """
    

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
Total_Length = nr_letters+nr_symbols+nr_numbers
Password = ""

for nr_letters in range(0, nr_letters) :
    Password += random.choice(letters)
for nr_symbols in range(0, nr_symbols) :
    Password += random.choice(symbols)
for nr_numbers in range(0, nr_numbers) :
    Password += random.choice(numbers)
random.shuffle(list(Password))
Password_list = list(Password)
random.shuffle(Password_list)

RAND = ''.join(Password_list)
print("Password : " + RAND)

# 원하는 결과는 맞지만 코드가 다른(구글링함)
