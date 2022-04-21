import constant

def user_num_input(msg):
    num = ""
    while True:
        num = input(msg)
        try:
            int(num)
            break;
        except ValueError:
            try:
                float(num)
                break;
            except ValueError:
                print("Error, numerical input expected, please try again: ")
    
    return num
    
"""
A = amount after time t

P = principal amount (your initial investment)

r = annual interest rate (divide the number by 100)

t = number of years

n = number of times the interest is compounded per year

Amount returned = P * (1+r/t) ^ (nt)

"""
def compound_interest(principal, apr, t, n):
    return (principal * (1 + (apr / t)**(n * t)))


"""
Formula = Interest rate - (Interest rate*tax rate)

"""
def post_tax_return(interest_rate, tax_rate):
    return (interest_rate - (interest_rate * tax_rate))

"""
Future amount = Present amount * (1+inflation rate) ^number of years
"""
def inflation(present_amt, inf_rate, num_years):
    return(present_amt * (1 + inf_rate)**(num_years))

"""
Future Value = Present value/(1+inflation rate)^number of years

"""
def purchasing_power(present_val, inf_rate, num_years):
    return (present_val / (1 + inf_rate)**(num_years))

"""
r = interest rate

n = number of times compounding is done in a year

Effective Annual Rate = (1+(r/n))^n)-1

"""
def effective_annual_rate(interest_rate, period):
    return ((1 + (interest_rate / period))**(period) - 1)

"""
FV is the investment's ending/maturity value

PV is the investment's beginning/opening value

n is the duration in years

CAGR=((FV/PV)^(1/n)) - 1

"""
def compound_annual_growth_rate(final_val, present_val, duration):
    return ((final_val / present_val)**(1 / duration) - 1)

"""
A = Periodic EMI amount

P = Principal borrowed

r = periodic interest rate (apr / 12)

n = total number of payments (months of loan term)

A = P * ((r(1 + r)^n)/((1 + r)^n - 1))

"""
def equated_monthly_installments(principal, interest_rate, duration):
    r = interest_rate / 12
    return (principal * ((r(1 + r)**(duration))/((1 + r)**(duration) - 1)))

"""
Liquidity Ratio = Total liquid assets / Total current debt

"""
def liquidity_ratio(liquid, current_debt):
    return (liquid / current_debt)



user_n = user_num_input("Please enter expected APR: ")
print(user_n)
print(constant.GRAVITY)

