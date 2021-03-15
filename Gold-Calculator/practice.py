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
