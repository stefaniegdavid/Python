#1. Countdown - Create a function that accepts a number as an input. 
#Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(x):
    result = []
    for i in range(x, -1, -1):
        result.append(i)
    return result
countdown(5)


#2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

#3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

#4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

#5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.