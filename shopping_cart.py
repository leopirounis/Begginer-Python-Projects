foods = []
prices = []
total = 0

while True:
 food = input("Enter a food to buy (q to quit): ")
 if food.lower() == "q":
  break
 else:
  foods.append(food)
  price = float(input("Enter the price: $"))
  prices.append(price)

print("---YOUR CART---")
for food in foods:
 print(food,end = " ") #to end= " " gia na einai dipla dipla me keno kai oxi to ena katw apo to allo

for price in prices:
 total += price

print()
print(f"Price total: ${total}")