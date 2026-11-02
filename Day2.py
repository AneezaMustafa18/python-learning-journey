#Arithmetic Operators 
a = 10
b = 5
print("Addition : " , a + b)
print("Subtraction :" , a - b)
print("Mutiplication :" , a * b)
print("Division :" , a / b)
print("Floor Division :" , a // b)
print("Modulus :" , a % b)
print("Power :" , a ** b )

#Comparison Operators
a = 10
b = 5
print( a > b)
print( a < b)
print( a == b)
print( a != b)
print( a >= b)
print( a <= b)

#If-else Statement
age = int (input ("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print('You are Under Age!!')


#-----Simple Calculator--------
num1 = float(input("\n Enter your first number :"))
num2 = float(input("Enter your second number :"))

print("\n Choose an operation :")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1-4) : ")

if choice == "1":
    print("Result : ", num1 + num2)
elif choice == "2":
    print ("Result : ", num1 - num2)
elif choice == "3":
    print ("Result : ", num1 * num2)
elif choice == "4":
 if num2 != 0 :
    print("Result : ", num1 / num2)
 else:
    print("Cannot Divide by zero")

else: 
   print("Invalid choice")
