balance = 1000

print("-------ATM-------")
print("Balance")
print("Deposit")
print("Withdraw")
print("Exit")

while True:
    choice = int(input("Please choose which service you want to dot: "))

    if choice == 1:
        print("Your balance is:", balance)
    elif choice == 2:
        deposit = int(input("How much would you like to deposit: "))
        balance += deposit
        print("Done! New balance:", balance)
            print("Thank you!")
    else:
        print("Deposit must be greater than 0: ")

              
