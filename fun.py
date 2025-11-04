# python program using functions.
# Simple calculator

def calculator():
    num1 = float(input("Enter the first number :"))
    operator = input("Enter Operators : (+, * , /, % , - )")
    num2 = float(input("Enter second number :"))
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print(num1/num2)
        else:
            print("Eror: division by zero")
    else: print("invalid operators")
    
calculator()



## RETURN MULTIPLE VALUES
def get_user_info(name, age):
    return name , age , "active"

user_name , user_age, user_status= get_user_info("Manasa",30)
print(f"Name : {user_name} , Age : {user_age} , Status : {user_status}")

# USING RETURN VALUE IN EXPRESSION
def square(num):
    return num * num

def cal_average(x,y):
    return (x+y)/2

square_value= square(4)
average_of_square = cal_average(square(3), square(2))
print(f"Square value :{square_value} ")
print(f"Average of square : {average_of_square}")