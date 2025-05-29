import random

def spin_row():
    symbols = ["🍒","🍉", "🍋", "🔔", "⭐"]
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print("************")
    print(" ".join(row)) # emfanizei ta stoixeia ths row me keno anamesa kai xwris brackets 
    print("************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4 
        elif row[0] == "🍋":
           return  bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20 
    else:
        return 0

def main():
    balance = 100
    print("****************************")
    print("Welcome to Python Slots")
    print(" Symbols: 🍒 🍉 🍋 🔔 ⭐  ")
    print("****************************")

    while balance > 0 :
        print(f"Current balance: ${balance}")
        bet = input("Enter your bet amount: ")
        if not bet.isdigit(): # an den valei arithmo gia bet
            print("Please enter a valid number: ")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient funds!")
            continue
        if bet < 0:
            print("Bet must be greater than zero!")
            continue
        balance -= bet
        row = spin_row() 
        print("Spinning...")
        print_row(row)
        payout = get_payout(row,bet)
        if payout > 0:
            print(f"You won : ${payout}")
        else:
            print("Sorry you lost this round!")
        balance += payout
        play_again = input("Do you want to spin again? (Y/N): ").upper()
        if play_again != "Y":
            break
    print("**********************************************")
    print(f"Game over! Your final balance is : ${balance}")
    print("**********************************************")

if __name__ == "__main__":
    main()