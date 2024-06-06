#Making a simple calulator 
#Should be able to take in user input 
#Should be able to do basic arithmetic (+,-,*,/)

#first lets set up the user input for num 1 and num 2 
print("Welcome to the Simple Calculator !")

num_1 = input("Enter your first number: ")
num_2 = input("Enter your second number: ")

#that works, I tested it with two print statements.
#now we want to have the user pick an operations +,-,*,/

# user input for the operation 
operation = input("Please choose whether you want to +, -, * , or / :")

#operation for string input 
multiple = "*"
add = "+"
subtract = "-"
divide = "/"

#setting up the conidtions, this will be changed in the future so it can be more dynamic 
if operation == "+":
    num_add = float(num_1)+float(num_2)
    exit(f"Answer: {num_add}")
if operation == "-":
    num_sub = float(num_1)-float(num_2)
    exit(f"Answer: {num_sub}")
if operation == "*":
    num_mul = float(num_1) * float(num_2)
    exit(f"Answer: {num_mul}")
if operation == "/":
    num_div = float(num_1) - float(num_2)
    exit(f"Answer:{num_div}")
else: 
    exit("Please enter a valid operation")