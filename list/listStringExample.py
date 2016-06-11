def list_to_string(list_input):
    index = 0
    string = ""
    while index < len(list_input):
        if index == len(list_input) - 1:
            string = string + list_input[index]
        else:
            string = string + list_input[index] + ", "
        index = index + 1
    return string

spam = ['apples', 'bananas', 'tofu', 'cats']
stringValue = list_to_string(spam)
print(stringValue)
#print("List")