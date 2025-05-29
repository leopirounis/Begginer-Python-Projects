unit = input("Is the temperature in Celcius or Fahrenheit ? (C/F): ").upper()
while True:
 try:
  temperature = float(input("What is the temperature ? : "))
  if unit == "C":
    temperature = (9 * temperature)/5 + 32
    print(f"The temperature in Fahrenheit is {temperature} °F." )
    break
  elif unit == "F":
    temperature = (temperature - 32) * 5 / 9
    print(f"The temperature in Celcius is {temperature} °C. ")
    break
  else:
    print("Invalid input !")
    unit = input("Is the temperature in Celcius or Fahrenheit ? (C/F): ").upper()
 except ValueError:
   print("You didn't enter a temperature! Try again! ")
      

