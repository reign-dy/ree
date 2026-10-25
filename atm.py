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
    elif choice == 3:
        Withraw = int(input("Enter amount to Withdraw :"))
        if amount > balance:
            print("Insufficient balance :")
        elif amount > 0:
            balance -= amount
            print("Please Take your cash")
        else:
            print("Invalid amount :")

elif choice == 4:
  print("Thank you for banking with us. Have a nice day.")
else: 
print("Inavlid pin. Please try again
