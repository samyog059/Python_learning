# Simple Interest Calculator
def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    Parameters:
    principal (float): The initial amount of money.
    rate (float): The annual interest rate (in percentage).
    time (float): The time the money is invested for (in years).

    Returns:
    float: The simple interest earned.
    """
    interest = (principal * rate * time) / 100
    return interest