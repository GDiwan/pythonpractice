# Fibonacci

#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
# is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num -1 ) + fibonacci(num -2)

fibo_six = fibonacci(6)
print(fibo_six)

# List all fib nums


