#python script which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature. (Note: Tf = Tc * 9/5 + 32)
try:
    celsiusT = float(input("Enter Celsius temperature:"))
    fahrenheitT = celsiusT * 9/5 +32
    print("The fahrenheit temperature is ",fahrenheitT)
except Exception as e:
    print(e)