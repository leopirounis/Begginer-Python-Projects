#Currency converter my solution ✅


#Is it positive float function
def is_positive_float(string):
    try:
        if float(string) > 0:
            return True
        else:
            return False
    except ValueError:
        return False

#Is it acceptable currency function
def is_it_currency(string):
    try:
        if (string == "USD") or (string == "EUR") or (string == "CAD"):
            return True
        else:
            return False
    except ValueError :
        return False 
    
#Convertion function
def convert(amount,source_currency,target_currency):
    if (source_currency == "USD" and target_currency == "CAD"):
        return float(amount) * 1.36
    elif (source_currency == "CAD" and target_currency == "USD"):
        return float(amount) * 0.73
    elif (source_currency == "USD" and target_currency == "EUR"):
        return float(amount) * 0.87
    elif (source_currency == "EUR" and target_currency == "USD"):
        return float(amount) * 1.15
    elif (source_currency == "CAD" and target_currency == "EUR"):
        return float(amount) * 0.64
    elif (source_currency == "EUR" and target_currency == "CAD"):
        return float(amount) * 1.57
    else: 
        return float(amount)
        
  
#Currency Converter Programm
boolian1 = True
boolian2 = True
boolian3 = True
while boolian1 == True:
    amount = input("Enter amount: ") 
    if is_positive_float(amount) == False :
        print("Invalid amount")  
    else:
        boolian1 = False 
    while is_positive_float(amount) == True and (boolian2 == True):
        source_currency = input("Enter source currency (USD/EUR/CAD): ").upper() 
        if is_it_currency(source_currency) == False:
            print("Invalid source currency")
        else:
            boolian2 = False
        while is_it_currency(source_currency) == True and (boolian3 == True):
            target_currency = input("Enter target currency (USD/EUR/CAD): ").upper()
            if is_it_currency(target_currency) == False:
                print("Invalid target currency")
            else:
                print(f'{amount} {source_currency} is equal to {convert(amount,source_currency,target_currency):.2f} {target_currency}')   
                boolian3 = False
            
        
    
            
            
     
        
    