
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

def only_odds(num_list):
    new_list = []
    for num in num_list:
        if is_odd(num) == True:
            new_list.append(num)
    return new_list

print(only_odds([11, 20, 42, 97, 23, 10]))
