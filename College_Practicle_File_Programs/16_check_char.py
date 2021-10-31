test_str = input("Input a char or str: ")
test_str = test_str.lower()
if test_str in ['a','e','i','o','u']:
    print("test char is a vowel")
elif test_str.isalpha():
    print("Test char/str is alphabet")
elif test_str.isdigit():
    print("Test char/str is digit")
elif (not test_str.isalnum()):
    print("Test char/str is special character")