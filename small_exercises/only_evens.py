
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def only_evens(num_list):
    new_list = []
    for num in num_list:
        if is_even(num) == True:
            new_list.append(num)
    return new_list
    
print(only_evens([11, 20, 42, 97, 23, 10]))