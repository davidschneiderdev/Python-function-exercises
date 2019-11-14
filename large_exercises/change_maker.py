
import math

def bills_breakdown(bills):
    bills_tuple = ()
    print(bills)
    if bills > 100:
        hundreds = bills/100
        print(hundreds)
        bills -= (hundreds * 100)
        bills_tuple += (hundreds, )
        print(bills)
    if bills > 49:
        print(bills)
    print(bills_tuple)

    # print(bills_tuple)

def coins_breakdown(coins):
    coins_tuple = ()

def make_change(total_charge, payment):
    change = payment - total_charge
    coin_bill_seperate = math.modf(change)
    # print(coin_bill_seperate)
    coins_breakdown(coin_bill_seperate[0])
    bills_breakdown(coin_bill_seperate[1])
    

# if 100 % 80:
#     print("It divides")
#     print(100 % 80)

(make_change(200, 452))
