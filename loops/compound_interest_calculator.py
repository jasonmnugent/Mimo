# use a while loop to see how the amount in a bank account increases over time, with a given interest rate.

account = 100
interest_rate = 0.004
years = 3

print(f"Initial amount: {account}")

counter = 1
while counter <= years:
    accrued_interest = account * interest_rate
    account += accrued_interest
    print(f"year {counter}: {account}")
    counter += 1