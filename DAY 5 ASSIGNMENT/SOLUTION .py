#Object Oriented Programming Challenge......
#For this challenge, create a bank account class that has two attributes:

#owner
#balance

#and two methods:

#deposit
#withdraw

#As an added requirement, withdrawals may not exceed the available balance.
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

#SOLUTION:
#SOURCE CODE:

class Account:
    owner  = ""                   #CREATE CLASS ACCOUNT IN WHICH TWO ATTRIBUTES NAMED AS OWNER AND BALANCE....
    balance  = 0
     
    def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance
    
    def __str__(self):
            return f"Account owner: Pavan \nAccount balance: 100"
    
    def deposit(self, dep_amt):                   #FOR AMOUNT DEPOSITION USING METHOD
            self.balance += dep_amt
            print("Deposit Accepted")
    
    def withdraw(self, wd_amt):                   #FOR AMOUNT WITHDRAW USING METHOD
        try:
            if self.balance >= wd_amt:
                self.balance -= wd_amt
                print("Withdrwal accepted")
            else:
                print("Funds unavailable")
        except ValueError:
               print("valueerror for fund")
			   
			   
#OUTPUTS:
# 1. Instantiate the class 
     # acct1 = Account('Pavan',100)


# 2. Print the object
     #print(acct1)
	 #Account owner: Pavan 
     #Account balance: 100

# 3. Show the account owner attribute
     #acct1.owner
	 #'Pavan'

# 4. Show the account balance attribute
     #acct1.balnce
	 #100

# 5. Make a series of deposits and withdrawals
     #acct1.deposit(60)
	 #'Deposit Accepted'
	 
	 #acct1.balance
	 #135
	 
	 #acct1.withdraw(85)
	 #'Withdrawal Accepted'
	 
	 #acct1.balance
	 #50

# 6. Make a withdrawal that exceeds the available balance
     #acct1.withdraw(600)
     #'Funds unavailable'