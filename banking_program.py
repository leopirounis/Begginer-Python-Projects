def show_balance(balance): #vazw to balance san eisodo giati xrisimopoiite mesa sti sinartisi
    print(f"Your balance is : ${balance:.2f}")
    

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
      print("That's not a valid amount!")
      return 0 # gia na mi prosthesei tipota sto balance (stin main function) 
    else:      #otan kanei katethesi kai exw valei arnitiko
      return amount                     
    

def withdraw(balance): #vazw to balance san eisodo giati xrisimopoiite mesa sti sinartisi
    amount = float(input("Enter an amount to be withdrawn: "))
    if amount > balance:
        print("You don't have enough funds!")
        return 0
    elif amount < 0 :
        print("Amount must be greater than zero!")
    else:
        return amount

def main(): 
    
  balance = 0
  is_running = True

  while is_running:
    print("***************")
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("***************")
    
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        show_balance(balance)
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw(balance)
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice")
  print("***************************")
  print("Thank you! Have a nice day!")
  print("***************************")

if __name__ == "__main__": # afto to if panta isxyei kai trexei prin treksei to ipolipo programma 
  main()                 #opote panta tha trexei prwta h main() function