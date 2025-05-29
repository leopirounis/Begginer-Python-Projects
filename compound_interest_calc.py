principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter principal: "))
    if principal <= 0:
     print("Principal can't be zero or negative!")

while time <= 0:
    time = int(input("Enter time: "))
    if time <= 0:
     print("Time can't be zero or negative!")


while rate <= 0:
    rate = float(input("Enter rate: "))
    if rate <= 0:
     print("Rate can't be zero or negative!")

total = principal * pow(1 + rate/100,time)

print(f"Balance after {time} years is : ${total:.2f}") #total:.2f kanei ypologismo tou total sta dio dekadika
