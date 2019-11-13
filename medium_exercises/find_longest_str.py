
str_list = ["banana", "far", "apple", "orange", "pineapple"]

def longest_str(str_list):
    return sorted(str_list, key=len)[-1]

print(longest_str(str_list))

