# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Example usage
principal_amount = 1000  # Principal amount in dollars
annual_rate = 5  # Annual interest rate in percentage
time_period = 3  # Time period in years

interest = calculate_simple_interest(principal_amount, annual_rate, time_period)
print(f"The simple interest is: ${interest}")