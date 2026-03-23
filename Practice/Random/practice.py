# Simple Interest Calculator
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))  
Simple_Interest = (principal * rate * time) / 100
print("The Simple Interest is:", Simple_Interest)
# Compound Interest Calculator
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))
compound_interest = principal * (1 + rate/100) ** time - principal
print("The Compound Interest is:", compound_interest)               