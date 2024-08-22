text = input("Input a string: ")
text = text.strip()
if len(text) < 1:
    print("Input a valid text")
else:
    if all(text[i] in "0123456789" for i in range(len(text))):
        print("The string is an integer.")
    elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         print("The string is an integer.")
    else:
        print("The string is not an integer.") 