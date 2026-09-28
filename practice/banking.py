def show_balance():
    print(f"Your balance is ${balance}")

def withdrawl(balance):
    amount=int(input("Enter the amount to withdrawl"))
    return amount
def deposit(balance):
    amount=int(input("Enter the amount to deposit"))
    return amount

balance=0
is_running=True
while is_running:
    print("Welcome to banking program")
    print("1.Show balance")
    print("2.Withdrawl")
    print("3.Deposit")
    print("4.Exit")

    choice=int(input("Enter the choice(1-4)"))
    if choice==1:
        show_balance()
    elif choice==2:
       balance-= withdrawl(balance)
    elif choice==3:
       balance+= deposit(balance)
    elif choice==4:
        is_running=False
    else:
        print("Enter the valid one to proceed")
