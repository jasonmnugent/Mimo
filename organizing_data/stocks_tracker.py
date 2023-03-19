# use a list to keep track of a company's stock values

apple_stocks = [298.18, 304.18, 289.23]

# update the stock price in the first position, since we now have more recent data. 
# this updates the value at index 0
apple_stocks[0] = 310
print("Latest value:")
print(apple_stocks[0])


apple_stocks[1] = 310
print("Highest value:")
print(apple_stocks[1])

print("Lowest value:")
print(apple_stocks[2])