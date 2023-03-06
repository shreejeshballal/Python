divisor = int(input("Enter the divisor:"))
dividend = int(input("Enter the divident:"))

try:
    print(dividend/divisor)
except ZeroDivisionError as e:
    print(e)

