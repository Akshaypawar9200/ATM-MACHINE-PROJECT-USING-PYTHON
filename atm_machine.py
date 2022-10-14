import time
print("Please Insert Your Card Into Machine ")
time.sleep(5)

password=1234

balance=5000

pin=int(input("Please Enter Your Pin "))
print("*****************************************************************************************************************************")
if pin==password:
    while True:
        print("""
        
        1.Balance
        2.Withdrawl Amount
        3.Deposite Amount
        4.exit
        """)
               
         
        try:    
             
            choice = int(input("Please enter your choice "))
        except:
            print("Please enter valid option")
        
    
        if choice==1:
            print("*****************************************************************************************************************************")
            print(f"Your current balance is {balance}")
            print("*****************************************************************************************************************************")
        if choice==2:
            withdraw=int(input("Enter Withdrawl amount "))
            if(balance>=withdraw):
                balance=balance-withdraw
                print("*****************************************************************************************************************************")
                print(f"Successfully Withdraw amount of {withdraw}")
                print("*****************************************************************************************************************************")
                print(f"Your current balance is {balance}")
                print("*****************************************************************************************************************************")

            else:
                print("*****************************************************************************************************************************")
                print("Insufficient Balance")
                print("*****************************************************************************************************************************")
        if choice==3:
            deposite=int(input("Enter the Deposite Amount "))
            balance=deposite+balance
            print("*****************************************************************************************************************************")
            print(f"Successfully deposit amount Rs.{deposite} in your account")
            print("*****************************************************************************************************************************")
            print(f"Your current balance is {balance}")
            print("*****************************************************************************************************************************")
        if choice==4:
            break
     
else:
    print("Wrong Pin ")