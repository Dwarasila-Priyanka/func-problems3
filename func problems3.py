# 1. Sum of Digits Using a While Loop
def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

print("Sum of digits:", sum_of_digits(123))  # Output: 6

#  2. Reverse a Number Using a While Loop
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev

print("Reversed number:", reverse_number(123))  # Output: 321

# 3. Check Palindrome Using a While Loop
def is_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    if original == rev:
        return True
    else:
        return False

num = 121
if is_palindrome(num):
    print(num, "is a Palindrome")
else:
    print(num, "is NOT a Palindrome")

