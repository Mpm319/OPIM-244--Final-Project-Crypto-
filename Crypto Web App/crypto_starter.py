##Set up to convert numbers to USD

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    
    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" 


# example invocations:
print(to_usd(4.5))
print(to_usd(200000.9999))


##Set up to convert numbers to percent

def to_pct(my_number):
    """
    Formats a decimal number as a percentage, rounded to 4 decimal places, with a percent sign.
    
    Param my_number (float) like 0.95555555555
    
    Returns (str) like '95.5556%'
    """
    return f"{(my_number * 100):.4f}%"


# example invocation:
print(to_pct(0.5))
print(to_pct(.955555555))