1. is_leap(year) Function

(Already provided by you and correct!)

def is_leap(year):
    """
    Determines whether a given year is a leap year.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


---

2. Conditional Statements Exercise

n = int(input())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")


---

3. Find Even Numbers Between Two Integers (Inclusive, Without Loops)

Solution 1: Using if-else statement and range() + filter()

a = 3
b = 10

# Ensure a is less than or equal to b
if a > b:
    a, b = b, a

even_numbers = list(filter(lambda x: x % 2 == 0, range(a, b + 1)))
print(even_numbers)


---

Solution 2: Using range() and filter() directly without if-else

a = 3
b = 10

# This works no matter the order of a and b
even_numbers = list(filter(lambda x: x % 2 == 0, range(min(a, b), max(a, b) + 1)))
print(even_numbers)

