class Account:
    def __init__(self):
        self.account_number = input("acc num ")
        self.customer_name = input("name ")
        self.initial_amount = int(input("initial amount"))
        self.balance = self.initial_amount

    def deposit(self, amount):
        try:
            if int(amount) <= 0:
                raise Exception
            else:
                self.balance = int(self.balance) + int(amount)
                print("after deposit available balance =", self.balance)
                # print(self.customer_details[self.account_number])

        except Exception as e:
            print(e)
            print("Invalid Amount Exception")

    def withdraw(self, amount):
        try:
            if self.balance <= 0 or amount > self.balance:
                raise Exception
            else:
                self.balance = self.balance - amount
                print("remaining balance in", self.account_number, " =", self.balance)
        except Exception:
            print("Invalid Amount Exception")

    def balance_enquiry(self):
        print("available balance in", self.account_number, " =", self.balance)


class BankServices(Account):
    def __init__(self):
        # super().__init__()
        pass
        # self.account_number=self.account_number

    def createAccount(self):
        try:
            super().__init__()
            # self.account_number = self.account_number
            # self.customer_name = input("name ")
            # self.initial_amount = int(input("initial amount"))
            if self.initial_amount < 500:
                del self.account_number, self.customer_name, self.initial_amount
                raise Exception


            else:
                self.balance = self.initial_amount
                print("account created")
                return True
        except Exception as e:
            print(e)
            print("Account Creation Failed")
            return False

    def transfer_funds(self, tra_amt):
        try:
            if tra_amt > self.balance:
                raise Exception
            else:
                self.balance = self.balance - tra_amt
                print("remaining balance =", self.balance)
        except Exception as e:
            print(e)
            print("Transfer Failed")


lis = [BankServices() for i in range(0, 5)]
ac_num = []
for j in lis:

    a=j.createAccount()

    try:
        if a:
            if j.account_number in ac_num:
                print("account already exists")
                del j
            else:

                ac_num.append(j.account_number)
        else:
            raise Exception
    except Exception as e:
        print(e)
        print("Creation Failed")

print(ac_num)
print(len(ac_num))

# print(lis[1].account_number)
i = 1
flag=0

while i == 1:
    try:
        choice = int(input(
            "Enter the action you wannna proceed  \n 1. withdraw \n 2.deposit \n 3.balance enquiry\n 4. transfer amount \n"))

        if choice == 1:
            ac = input("Enter the account number")
            temp = 0
            for i in lis:
                if ac in i.account_number:
                    dep = int(input("Enter the amount to be withdrawed"))
                    i.withdraw(dep)
                    temp = 1
                    break
            if temp == 0:
                print("Invalid Account")

        if choice == 2:
            acc = input("Enter the account number")
            for i in lis:
                if acc in i.account_number:
                    amount = input("enter the amount")
                    i.deposit(amount)
                    flag=1
                    break

            if flag!=1:
                print("Account not found")

                # else:
                #     print(acc," ",i.account_number)
                #     print("errrrrr")

        elif choice == 3:

            acc = input("enter the account number")
            for i in lis:
                if acc in i.account_number:
                    i.balance_enquiry()
                    flag=1
            if flag!=1:
                print("account not found")
                # else:
                #     print("sorry")

        elif choice == 4:
            acc1 = input("enter the 1st account number")
            acc2 = input("enter the 2nd account number")
            for i in lis:
                if acc1 in i.account_number:
                    for j in lis:
                        if acc2 in j.account_number:
                            tran = int(input("enter the transfer amount"))
                            if tran >= j.balance:
                                print("no money")
                            else:
                                i.transfer_funds(tran)
                                j.deposit(tran)

        else:
            raise Exception

    except Exception as e:
        print(e)
        print("Invalid Choice")

    i = int(input("Press 1 to continue"))

print("End")
