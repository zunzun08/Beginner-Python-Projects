
string = input("Input: ")
if string == 'x':
    print('There are no vowels in this sentence, please re enter.')
    exit()
else:
    new_string = string
    vowels = ('a', 'e', 'i', 'o', 'u')
    for word in string:
        if x in vowels:
            new_string = new_string.replace(x, "")
    print("Output: " + new_string)
