divisor = int(input("Enter the divisor:"))
divident = int(input("Enter the divident:"))

try:
    print(divisor/divident)
except ZeroDivisionError as e:
    print(e)

