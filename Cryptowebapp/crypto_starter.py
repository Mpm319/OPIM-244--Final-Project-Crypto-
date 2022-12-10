##Set up to convert numbers to USD
#import Crypto_App

def to_usd(my_price):
    
    return f"${my_price:,.2f}" 


# example invocations:
print(to_usd(4.5))
print(to_usd(200000.9999))


##Set up to convert numbers to percent

def to_pct(my_number):
   
    return f"{(my_number * 100):.4f}%"


# example invocation:
print(to_pct(0.5))
print(to_pct(.955555555))