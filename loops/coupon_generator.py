# use a for loop to speed up the process of creating multiple discount coupon codes

#create base variable to hold the name of website that you're generating coupons for
base = "www.homeflix.com"
coupon = "signup/coupon"
discount = 50
amount = 4

for num in range(amount):
    print(f"{base}/{coupon}/{discount}/{num}")

print(f"{amount} coupons created")