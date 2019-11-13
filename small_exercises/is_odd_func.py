def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def is_odd(num):
    if is_even(num) == True:
        return False
    else:
        return True

print(is_odd(6))