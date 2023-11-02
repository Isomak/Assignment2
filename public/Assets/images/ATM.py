# Michael Maniatis
# 100876436

balance = float(0)
otherBalance = float(0)

def getBalance():
    global balance   #Returns Your Total Balance
    return balance

def getOtherBalance():     #Retuns Your Total otherBalance
    global otherBalance   
    return otherBalance

def printBalances(): #Returns Your Two Balances Together
    print(f"The Total of Both Balances Are", getBalance() + getOtherBalance())

def deposit(money):
    global balance
    if money <= 0:
        print("Invalid input! Money entered should be greater than zero!")
    else:
        balance += money
        print("Money deposit successful!")


def withdraw(money):
    global balance   #Lets You Withdraw Money
    if money <= 0:
        print("Invalid input! Withdraw amount entered should be greater than zero!")
    elif money > balance:
        print("Insufficent Funds")
    else:
        balance -= money
        print("Money is withdrawn successfully!")

def transfer(money):
    global balance
    global otherBalance 
    if money <= 0:
        print("Invalid input! Money entered should be greater than zero")
    elif money > balance:
        print("Insufficent Funds")
    else:
        otherBalance += money
        balance -= money
        print("Money has been transferred from balance to other Balance") 

loopBool = True
while loopBool:
    choice = input(f"\nWhat Would You Like To Do?\n---------------------------\nSee Balance (1)\nSee Other Balance (2)\nSee Total Balance (3)\nDeposit Money (4)\nWithdraw Money (5)\nTransfer Money (6)\nExit (7)\n:")

    if choice == '1':
        print(f"Your balance is {getBalance()}")

    elif choice == '2':
        print(f"Your other balance is {getOtherBalance()}")

    elif choice == '3':
        printBalances()

    elif choice == '4':
        money = float(input("How much would you want to deposit?"))
        deposit(money)

    elif choice == '5':
        money = float(input("How much would you want to withdraw?"))
        withdraw(money)

    elif choice  == '6':
        money = float(input("How much would you want to transfer?"))
        transfer(money)

    elif choice == '7':
        loopBool = False
        
    else:
        print("invalid input")
    