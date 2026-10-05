celcius = float(input("Enter temperature in Celsius: ")) #The input taken from the user is a string, so it needs to be converted to a float for calculations
fahrenheit = celcius * 9 / 5 + 32 #32 is worngly written as 23, so it has been corrected to 32 to ensure accurate conversion from Celsius to Fahrenheit
print("That is", fahrenheit, "degrees Fahrenheit")