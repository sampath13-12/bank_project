#create account
#login account
# banking options--># CASH WITHDRAWL
                    # CASH DEPOSIT
                    # BALANCE ENQUIRY
                    # MINI STATEMENT


from time import sleep

class Account:
    def __init__(self,username,password,avail_balance = 50000):
        self.username = username
        self.password = password    
        self.avail_balance = avail_balance 

    def cash_withdrawl(self):
        withdrawl = int(input("Enter Amount to withdrawl : "))
        after_withdrawl = self.avail_balance - withdrawl
        last_transcations.append(f"Withdrawl amount : {withdrawl}")
        if withdrawl > self.avail_balance:
            print("Insufficient Balance")
        else:
            self.avail_balance = after_withdrawl
            print(f"Cash withdrawl : {withdrawl} \nAvailable Balance : {self.avail_balance}")

    def cash_deposit(self):
        deposit = int(input("Enter Deposit Amount : "))
        after_deposit = self.avail_balance + deposit
        last_transcations.append(f"Deposited amount : {deposit}")
        self.avail_balance = after_deposit
        print(f"Deposited Amount : {deposit} \nTotal Balance : {self.avail_balance}")
  
    def balance_enquiry(self):
        print(f"YOUR ACCOUNT BALANCE : {self.avail_balance}") 
    
    def mini_statement(self):
        try:
            updated_balance = (self.avail_balance + self.deposit) - self.withdrawl
            print("Last Transaction:")
            print(last_transcations)
            print(f"CURRENT AVAILABLE BALANCE : {updated_balance}")
        except Exception as e:
            if len(last_transcations) > 0 :
                print("Last Transaction:")
                print(last_transcations)
            else:
                print('No transactions')    
            
            print(f"CURRENT AVAILABLE BALANCE : {self.avail_balance}")
    
avail_balance = 50000
created_acc = [Account("ram","123",avail_balance)]
Bank_account = None
last_transcations = []

while True:
    print("1.Create Account\n""2.Login")
    select_opt = int(input("Select an option : "))
    print()

    if select_opt==1:
        username = input("Create a username : ")
        password = input("Create a password : ")
        created_acc.append(Account(username,password))
        if username == "" and password == "":
            print("Enter details to create account")
        else:    
            print(f"{username} your account is created successfully")

    elif select_opt==2:
        username = input("Enter a username : ")
        password = input("Enter a password : ")
        if username == "" and password == "":
            print("Enter details to login account")
        else:    
            for acc in created_acc:
                if acc.username == username and acc.password == password:
                    Bank_account = acc
                    print(f"{username} you are logged in")
                    break
            else:
                print("Details not registered with Bank") 
    else:
        print("Invalid option")


    while Bank_account is not None:
            print("-------------------WELCOME TO TRUST BANK-------------------")
            print()
            print("1)<--CASH WITHDRAWL-->")
            print("2)<--CASH DEPOSIT-->")
            print("3)<--BALANCE ENQUIRY-->")
            print("4)<--MINI STATEMENT-->")
            print()
            select_opt = int(input("SELECT OPTION : "))                    
                    
            if select_opt == 1 :
                Bank_account.cash_withdrawl()
                back_menu = int(input("Type 1 for Menu or 2 to Exit : "))
                if back_menu == 2:
                    break
                else:
                    sleep(1)
                    print("Coming to main menu")
            elif select_opt == 2 :
                Bank_account.cash_deposit()
                back_menu = int(input("Type 1 for Menu or 2 to Exit : "))
                if back_menu == 2:
                    break
                else:
                    sleep(1)
                    print("Coming to main menu")
                        
            elif select_opt == 3 :
                Bank_account.balance_enquiry()
                back_menu = int(input("Type 1 for Menu or 2 to Exit : "))
                if back_menu == 2:
                    break
                else:
                    sleep(1)
                    print("Coming to main menu")
                        
            elif select_opt == 4 :
                Bank_account.mini_statement()
                back_menu = int(input("Type 1 for Menu or 2 to Exit : "))
                if back_menu == 2:
                    break
                else:
                    sleep(1)
                    print("Coming to main menu")

            else:
                print("Enter valid options")






