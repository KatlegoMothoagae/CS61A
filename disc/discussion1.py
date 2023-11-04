def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    return temp < 60 or raining

def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    """
    "*** YOUR CODE HERE ***"
    if n % 10 >= 5:
        return n - n % 10 + 10 
    
    return n - n % 10

# Implement the classic Fizz Buzz sequence. The fizzbuzz function takes a positive integer n and prints out a single line for each integer from 1 to n. For each i:

#     If i is divisible by both 3 and 5, print fizzbuzz.
#     If i is divisible by 3 (but not 5), print fizz.
#     If i is divisible by 5 (but not 3), print buzz.
#     Otherwise, print the number i.

def fizzbuzz_recursive(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"

    string = ""
    if n == 0:
        return
    if n % 3 == 0:
        string += "fizz"
    if n % 5 == 0:
        string += "buzz"
    if not string:
        print(n)
    else:
        print(string)
    fizzbuzz_recursive(n -1)
    
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"

    string = ""
    for i in range(1, n+1):
        if i % 3 == 0:
            string += "fizz"
        if i % 5 == 0:
            string += "buzz"
        if not string:
            print(i)
        else:
            print(string)
        string = ""
    
# Write a function that returns True if a positive integer n is a prime number and False otherwise.

# A prime number n is a number that is not divisible by any numbers other than 1 and n itself. 
# For example, 13 is prime, since it is only divisible 
# by 1 and 13, but 14 is not, since it is divisible by 1, 2, 7, and 14.

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n < 2:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

'''Write a function that returns the number of unique digits in a positive integer.

    Hints: You can use // and % to separate a positive integer into its one's digit and the rest of its 
    digits.

    You may find it helpful to first define a function has_digit(n, k), 
    which determines whether a number n has digit k.'''

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    count = 1
    while True:
        digit = n % 10
        n //= 10
        if not has_digit(n, digit): 
            count += 1
        if n < 10:
            break
        
    return count

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while True:

        if n % 10 == k:
            return True
        
        if n < 10:
            break
        n //= 10
    return False

print(unique_digits(123))
