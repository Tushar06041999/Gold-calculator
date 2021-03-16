# creating a Number guessing game

wining_number=26
number=input("type number between 1 to 100 :")
number=int(number)
if number==wining_number:
    print("you win")
else:
    if number>wining_number:
        print("Too high")
    if number<wining_number:
        print("Too Low")

# Q/n Text Two value rectangle and shape and solve it

print("Enter length")
length=input()
print("Enter bredth")
bredth=input()

if length==bredth:
    print("yes,it's rectangel")
else:
    print("no,it's not rectangle")

# Take Two int Values from user and compare greatest one them

first_number=input("Enter your first number : ")
first_number=int(first_number)
second_number=input("Enter your Second number :")
second_number=int(second_number)
if first_number<second_number:
    print(second_number)
else:
    if first_number>second_number:
        print(first_number)
    if first_number==second_number:
        print(first_number,second_number)

print("First Quantity")
print("Total Price is :")
Quantity=int(input())
if Quantity >= 1000:
    print("After 10% Discount Price is :",((Quantity)-(.1*Quantity)))
else:
    print("cost is",Quantity)

# Suppose ,It's a alcoholic Day and the alchohole company provides a offer for Evryone
# if you buy 3 bottol of alcohole then you get 25% dicount & if you buy 10 bottol then you get 15% dicount and if you buy 50 bottol then you get 50% dicount

print("Buy Three bottol of Alchohole")
Three_price=input("Enter Each Bottol price :")
Three_price=int(Three_price)
if Three_price*.25 <Three_price:
    print("Discount Price :",((3*Three_price)-(3*Three_price*.25)))

#suppose a man get 5000 ,so he's need to give every month 5% interest then how much they provide3 after 6 month
#Gold Bondoki Hisab Calculator

print("Given Money")
How_much=input("We give him total Money : ")
How_much=int(How_much)
Monthly_count=input("Enter How many Month : ")
Monthly_count=(int(Monthly_count))
if How_much*0.05<How_much:
    print("Total Monafa :",(How_much*0.05*Monthly_count))
    print("Now Total We get",((How_much)+(How_much*0.05*Monthly_count)))
    
    
# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

Grading_system=input("Enter your Mark :")

Grading_system=int(Grading_system)
if Grading_system<25:
    print("F")
else:
    if 25<= Grading_system <45:
        print("E")
    if 45 <= Grading_system <50:
        print("D")
    if 50 <= Grading_system<60:
        print("C")
    if 60 <= Grading_system<80:
        print("B")
    if 80<=Grading_system:
        print("A")

# Take input of age of 3 people by user and determine oldest and youngest among them.

print("Age Determind :")
User_one=input("Enter your age :")
User_one=int(User_one)
# User_two=input("Enter your age :")
# user_two=int(User_two)
# user_three=input("Enter your age :")
# user_three=int(user_three)
if User_one <=20:
    print("Yougest")
elif User_one< 50:
    print("oldest")
else:
    print("Among of them")

# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

user_student=int(input("Enter your total classes :"))
Total_class=int(input("Total class held on :"))
Attend_class=int(input("Total attend class :"))
print("Attend Totalpercent of class :",((Attend_class*100)/(Total_class)))
if Total_class*0.75<=Attend_class:
     print("You Allow to sit in the exam")
else:
    print("You aren't Eligible ")

# Gold Calculator Update
gold_price=int(input("Enter the gold Price :"))
Gold_perana_price=int(gold_price/16)
wanna_buy=(int(input("How much Wanna be buy :")))
gold_per_roti_price=int(Gold_perana_price/6)
per_point_price=gold_per_roti_price/10
After_add_mozori=int((4000*wanna_buy)/16)+wanna_buy*Gold_perana_price
print("per ana price :",Gold_perana_price)
print("Per roti price :",gold_per_roti_price)
print("Total per point price :",per_point_price)
print("Total Gold Price:",wanna_buy*Gold_perana_price)
print("After Adding mozori :",After_add_mozori)
