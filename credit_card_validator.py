sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1: 
# Remove "-" or " ".

card_number = input("Enter your credit card number: ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1] # antistrefei tous arithmous


# Step 2:
#  Add odd digits from right to left.

for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3
# : Double every second digit from right to left
# (If result is a two digit number,add the two digit number
# together to get a single digit.) and then  sum them.

for y in card_number[1::2]:
    y = int(y)*2
    if y >= 10 : # doulevei mono gia dipsifia <= 18 afou to megalytero dipsio mporei na einai 2*9=18
        sum_even_digits += 1 + (1 + (y % 10))  
    else:
        sum_even_digits += y

# Step 4:
#total sum

total = sum_odd_digits + sum_even_digits

# Step 5 :
# an to total diairite me to 10 einai valid

if total % 10 == 0: 
    print("Valid")
else :
    print("Invalid")