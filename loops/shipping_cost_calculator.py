# use if, elif, and else statement to code a shipping cost calculator

international_shipping = True
total = 150
shipping_cost = 0

# add cost of international shipping
if international_shipping:
    shipping_cost += 15
    print("International base cost applied")

#update the shipping cost based on total purchase. 
if total <= 50:
    shipping_cost += 20
elif total <= 100:
    shipping_cost += 15
else:
    shipping_cost += 5

#print the result
print(f"Shipping cost: {shipping_cost}")