import random

# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"


dice_art = {
    1:  ("┌─────────┐",        #vazw komma kai mesa stin parenthesi otan allazw grammi giati eimai mesa se tuple
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"),
    2:  ("┌─────────┐",
         "│ ●       │",
         "│         │",
         "│       ● │",
         "└─────────┘"),
    3:  ("┌─────────┐",
         "│ ●       │",
         "│    ●    │",
         "│       ● │",
         "└─────────┘"),
    4  :("┌─────────┐",
         "│  ●    ● │",
         "│         │",
         "│  ●    ● │",
         "└─────────┘"),
    5  :("┌─────────┐",
         "│ ●     ● │",
         "│    ●    │",
         "│ ●     ● │",
         "└─────────┘"),
    6  :("┌─────────┐",
         "│ ●    ●  │",
         "│ ●    ●  │",
         "│ ●    ●  │",
         "└─────────┘"),}

dice = []
total = 0
number_of_dice = int(input("How many dice? : "))

for die in range(number_of_dice):
     dice.append(random.randint(1,6))
print(dice)

for die in range(number_of_dice):  # to die einai o diktis stin list dice stin epomeni grammi
     for line in dice_art.get(dice[die]):
      print(line)

for die in dice:
     total += die
print(f"The total is {total}.")