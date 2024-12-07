class Atm:
    def __init__(self):
        
        self.pin=""
        self.balance=0
        
        self.menu()
    def menu(self):
        User_input=input("""
              Hello ,how would you like to proceed
              1.enter 1 to create pin
              2.enter 2 to deposit
              3.enter 3 to withdraw
              4.enter 4 to check balance
              5.enter 5 to exit
""")
        if User_input =="1":
            self.create_pin()
        elif User_input =="2":
            self.deposit()
        elif User_input =="3":
            self.withdraw()
        elif User_input =="4":
            self.check_balance()
        else:
            print("bye")
            

     def create_pin(self):
         self.pin=input("Enter your pin")
         print("pin set successfully")
     def deposit (self):
         temp=input("Enter your pin") 
         if temp==self.pin:
             amount=int(input("Enter the amount"))
             self.balance=self.balance + amount
             print("Deposit succesfully")
         else:
             print("invilid pin")
     def withdraw(self):
         temp=input("Enter your pin")
         if temp==self.pin:
             amount=int("Enter the amount")
             if amount < self.balance:
                 self.balance=self.balance-amount
                 print("operation successful")
             else:
                  print ("insufficient fund")
         else:
             print("invalid pin")
     def check_balance(self):
         temp=input("Enter your pin")
         if temp==self.pin:
             print(self.balance)
         else:
             print("invalid pin") 
         

          
         
     
             
        
        
    
    
