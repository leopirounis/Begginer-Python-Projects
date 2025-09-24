import random

r_p_s_dictionary = {
    "r" : "🪨",
    "p" : "📄",
    "s" : "✂️"
}
while True:
  pc_selection = random.choice(["r","p","s"])
  player_answer = input("Rock, paper, or scissors? (r/p/s): ").lower()
  if player_answer =="r" and pc_selection == "r":
    print(f"You chose {r_p_s_dictionary.get(f"{player_answer}")}")
    print(f"Computer chose {r_p_s_dictionary.get(f"{pc_selection}")}")
    print("It's a tie.")
    keep_going = input("Continue? (y/n): ").lower()
    if keep_going =="n":
     break
  elif player_answer =="r" and pc_selection == "p":
    print(f"You chose {r_p_s_dictionary.get(f"{player_answer}")}")
    print(f"Computer chose {r_p_s_dictionary.get(f"{pc_selection}")}")
    print("You lose.")
    keep_going = input("Continue? (y/n): ").lower()
    if keep_going =="n":
      break
  elif player_answer =="r" and pc_selection == "s":
    print(f"You chose {r_p_s_dictionary.get(f"{player_answer}")}")
    print(f"Computer chose {r_p_s_dictionary.get(f"{pc_selection}")}")
    print("You win.")
    keep_going = input("Continue? (y/n): ").lower()
    if keep_going =="n":
      break
  elif player_answer =="p" and pc_selection == "p":
    print(f"You chose {r_p_s_dictionary.get(f"{player_answer}")}")
    print(f"Computer chose {r_p_s_dictionary.get(f"{pc_selection}")}")
    print("It's a tie.")
    keep_going = input("Continue? (y/n): ").lower()
    if keep_going =="n":
      break
  elif player_answer =="p" and pc_selection == "r":
    print(f"You chose {r_p_s_dictionary.get(f"{player_answer}")}")
    print(f"Computer chose {r_p_s_dictionary.get(f"{pc_selection}")}")
    print("You win.")
    keep_going = input("Continue? (y/n): ").lower()
    if keep_going =="n":
     break
  elif player_answer =="p" and pc_selection == "s":
    print(f"You chose {r_p_s_dictionary.get(f"{player_answer}")}")
    print(f"Computer chose {r_p_s_dictionary.get(f"{pc_selection}")}")
    print("You lose.")
    keep_going = input("Continue? (y/n): ").lower()
    if keep_going =="n":
      break
  elif player_answer =="s" and pc_selection == "s":
    print(f"You chose {r_p_s_dictionary.get(f"{player_answer}")}")
    print(f"Computer chose {r_p_s_dictionary.get(f"{pc_selection}")}")
    print("It's a tie.")
    keep_going = input("Continue? (y/n): ").lower()
    if keep_going =="n":
      break
  elif player_answer =="s" and pc_selection == "p":
   print(f"You chose {r_p_s_dictionary.get(f"{player_answer}")}")
   print(f"Computer chose {r_p_s_dictionary.get(f"{pc_selection}")}")
   print("You win.")
   keep_going = input("Continue? (y/n): ").lower()
   if keep_going =="n":
      break
  elif player_answer =="s" and pc_selection == "r":
   print(f"You chose {r_p_s_dictionary.get(f"{player_answer}")}")
   print(f"Computer chose {r_p_s_dictionary.get(f"{pc_selection}")}")
   print("You lose")
   keep_going = input("Continue? (y/n): ").lower()
   if keep_going =="n":
     break
  else:
    print("Invalid choice!")
   