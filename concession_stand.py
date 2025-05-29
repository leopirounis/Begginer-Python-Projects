menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart= []
total = 0

print("--------- MENU ---------")
for food, value in menu.items():
    print(f"{food:10} : ${value:.2f}")
print("------------------------")

while True:
  food_input = input("Select an item (q to quit): ").lower()
  if food_input == "q":
     break
  elif menu.get(food_input) is not None:
     cart.append(food_input)

print("--------- YOUR ORDER---------")
for buy in cart:
   print(buy, end=" " )
   total += menu.get(buy)
print()
print(f"Your total is ${total}.")
print("-----------------------------")