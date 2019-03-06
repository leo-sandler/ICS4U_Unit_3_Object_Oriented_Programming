class Customer:
    def __init__(self):
        file = open("3.3_Customers.txt", "r")
        file_read = [j.split(",") for j in file.read().split()]
        self.name = str(input("Your Name: ")).title()
        if self.name.isdigit():
            print("Invalid Name")
            Customer()
        for x in range(len(file_read)):
            if self.name == file_read[x][0]:
                self.balance = file_read[x][1]
                self.password = file_read[x][2]
                self.password_checker()
            elif x == len(file_read):
                self.password = str(input("Password: "))
                self.password_checker()

    def balance_maker(self):
        try:
            self.balance = int(input("Bank Balance: "))
            if self.balance <= 0:
                print("Invalid balance amount")
                Customer()
            return int(self.balance)
        except ValueError:
            print("Invalid balance amount")
            Customer()

    def password_checker(self):
        text_file = open("3.3_Customers.txt", "r")
        file_read = [j.split(",") for j in text_file.read().split()]
        for x in range(len(file_read)):
            if self.name == file_read[x][0]:
                if str(input("What is your password: ")) == file_read[x][2]:
                    self.main()
                else:
                    print("Incorrect password")
                    Customer()
        self.writer()

    def writer(self):
        file = open("3.3_Customers.txt", "a")
        self.balance = self.balance_maker()
        file.write(str(self.name) + "," + str(self.balance) + "," + str(self.password))
        file.close()
        self.password_checker()

    def main(self):
        self.balance = int(self.balance)
        while True:
            user_input = input("1) Deposit\n2) Withdraw\n3) Print Balance\n4) Continue\n5) End Code\nInput: ")
            if user_input == "1":
                self.deposit()
            if user_input == "2":
                self.withdrawal()
            if user_input == "3":
                self.balance_printing()
            if user_input == "4":
                Customer()
            if user_input == "5":
                exit("Code Ended")
            else:
                continue

    def deposit(self):
        try:
            deposit_amount = int(input("How much money do you want to deposit: "))
            if deposit_amount >= 1:
                self.balance += deposit_amount
            else:
                print("Invalid deposit amount.")
        except ValueError:
            print("Invalid deposit amount")

    def withdrawal(self):
        try:
            withdrawal_amount = int(input("How much money do you want to withdraw: "))
            if withdrawal_amount >= 1:
                if withdrawal_amount < int(self.balance):
                    self.balance -= withdrawal_amount
                else:
                    print("Invalid withdrawal amount.")
            else:
                print("Invalid withdrawal amount.")
        except ValueError:
            print("Invalid withdrawal amount")

    def update(self, reason):
        if reason == "Withdrawal":
            print("Search through text file, then update")
        elif reason == "Deposit":
            print("Same as above.")

    def balance_printing(self):
        print("You have " + str(self.balance) + " in the bank.")


Customer()


# Need to be able to sense if a user exists, if it doesn't create a user. Access through the TXT file.
