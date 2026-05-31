name = input("Enter account holder name: ")
acc_no = input("Enter account number: ")

balance = 0

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("Deposited Successfully")

    elif choice == "2":
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdraw Successful")
        else:
            print("Not enough balance")

    elif choice == "3":
        print("Name:", name)
        print("Account No:", acc_no)
        print("Balance:", balance)

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")