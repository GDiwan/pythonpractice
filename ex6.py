#Exercise 6 (and Solution)

#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

user_input = input('Please, enter a string to check if it\'s Plaindrome: ')

reverse_string = user_input[::-1]
if user_input == reverse_string:
    print(f'{user_input} is palindrome')
else:
    print(f'{user_input} is not a plaindrome')


