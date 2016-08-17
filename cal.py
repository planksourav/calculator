# first program to make a simple calculator

#define function

#this function to add two numbers
def add(x, y):
    return x + y

#this function to subtracts two numbers
def subract(x, y):
    return x - y

#this function to multiply two numbers
def multiply(x, y):
    return x * y

#this function to devided two numbers
def devide(x, y):
    return x / y


#now take the input from user

print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Devide")

choice = input("Enter Choice(1/2/3/4):")

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1, num2))

elif choice == '2':
    print(num1,"-",num2, "=", subract(num1, num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", devide(num1, num2))

else:
    print("Invalid Input")