conversion_rate = 1.35  

pounds = float(input("Please enter amount in pounds: £"))

# Convert to dollars
dollars = pounds * conversion_rate

# Print the result
print(f"£{pounds} are ${dollars:.2f}")