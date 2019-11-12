
# convert a letter
def convert_letter(letter, rotate_by=13):
    # rotate_by is an optional argument.

    # 1. Setup/configuration
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    # 2. Work
    position = alphabet.index(letter)
    new_position = (position + rotate_by) % 26
    new_letter = alphabet[new_position]

    # 3. Result
    return new_letter

def convert_sentence(sentence):
    # new_list = []
    # for letter in list(sentence):
    #     if letter == " ":
    #         new_list.append(letter)
    #     else:    
    #         new_list.append(convert_letter(letter))
    # new_sentence = ''.join(new_list)
    # return new_sentence

    new_sentence = ""
    for letter in sentence:
        try:
            new_sentence += convert_letter(letter)
        except ValueError:
            new_sentence += letter
    return new_sentence

sentence = "lbh zhfg hayrnea jung lbh unir yrnearq"
new_sentence = convert_sentence(sentence)
print(new_sentence)



