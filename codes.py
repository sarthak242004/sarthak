def calculate_simple_interest(principal, time, customer_type):
    if customer_type == 'female' and customer_type == 'senior citizen':
        rate = 0.08
    elif customer_type == 'female' and customer_type == 'non senior citizen':
        rate = 0.06
    elif customer_type == 'male' and customer_type == 'senior citizen':
        rate = 0.07
    elif customer_type == 'male' and customer_type == 'non senior citizen':
        rate = 0.05
    else:
        raise ValueError('Invalid customer type')

    interest = principal * rate * time
    return interest

# Example usage
principal = 100000
time = 2
customer_type = 'female'  # Modify this value according to the customer's details

interest = calculate_simple_interest(principal, time, customer_type)
total_amount = principal + interest

print(f"Principal amount: {principal}")
print(f"Interest amount: {interest}")
print(f"Total amount: {total_amount}")







