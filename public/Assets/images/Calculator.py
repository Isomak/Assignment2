#Michael Maniatis
#100876436

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2
                                # All of these calculate your inputs
def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def exponent(num1, num2):
    return num1 ** num2
    
def custom_input(x):
    current_input = input(x)
    if current_input.lower() == "exit" or current_input.lower() == "stop":
        exit()
    return current_input

calculated_number = 0 
while True:
    print("Please Select A Mathematical Operator:\n\nFor Addition, Please Select: add (or) +\nFor Subtration, Please Select: subtract (or) -\nFor Multiplication, Please Select: multiply (or) *\nFor Division, Please Select: divide (or) /\nFor Exponents, Please Select: exponent (or) **")
    choice = custom_input('''Enter Your Choice: ''')

    if choice == 'add' or choice == '+': # --------------------------------------------------------
        operation = 0 

    elif choice == 'subtract' or choice == '-':
        operation = 1 
                                                                      # This takes your choice and does the math
    elif choice == 'multiply' or choice == '*':
        operation = 2
    
    elif choice == 'divide' or choice == '/':
        operation = 3

    elif choice == 'exponent' or choice == '**':
        operation = 4

    else:
        print("Invalid input")
        continue

    num1 = custom_input("Enter First Number: ") # First Number (it goes down the entire list)

    if num1.isdigit():
        num1 = float(num1)
    else:
        break
    
    num2 = custom_input("Enter Second number or leave blank to use previous calculation: ")
    if not num2.isdigit():
        num2 = calculated_number
    else:
        num2 = float(num2)


    if operation == 0: 
        calculated_number = add(num1,num2)

    elif operation == 1:
        calculated_number = subtract(num1,num2)

    elif operation == 2:
        calculated_number = multiply(num1,num2)
    
    elif operation == 3:
        calculated_number = divide(num1,num2)

    elif operation == 4:
        calculated_number = exponent(num1,num2) # to be quite frank I have no idea how you want us to do it with loops, I figured out how to do it with loops, put it in a different code, but I had an INSANE amount of trouble inplementing it into my code. 



    print(calculated_number)
    next_calculation = custom_input("Do You Want To Do Another Calculation? [yes/no]\n(Note, You May Also Use The Words [stop] or [exit]:\n")

    if next_calculation.lower().startswith('y'):
        continue

    elif next_calculation.lower().startswith('n') or next_calculation == 'stop' or next_calculation == 'exit':
        break

    else:
        print("Invalid Input, Returning To Choice Selection")