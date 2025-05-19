 1. Modify String with Underscores

def insert_underscore(txt):
    result = []
    i = 0
    count = 0

    while i < len(txt):
        result.append(txt[i])
        count += 1

        if count == 3:
            # Check if current character is vowel or has underscore next
            if txt[i] in "aeiou" or (i + 1 < len(txt) and txt[i + 1] == '_'):
                count = 0  # reset count
            else:
                if i + 1 < len(txt):  # Don't add at the end
                    result.append('_')
                count = 0
        i += 1

    return ''.join(result)

# Examples
print(insert_underscore("hello"))         # hel_lo
print(insert_underscore("assalom"))       # ass_alom
print(insert_underscore("abcabcabcdeabcdefabcdefg"))  # abc_abc_abcd_abcd_abcdef
 2. Integer Squares Exercise

n = int(input())
for i in range(n):
    print(i ** 2)
3. Loop-Based Exercises

Exercise 1: First 10 natural numbers using while

i = 1
while i <= 10:
    print(i)
    i += 1

Exercise 2: Number Pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


Exercise 3: Sum from 1 to a given number

num = int(input("Enter number: "))
total = 0
for i in range(1, num + 1):
    total += i
print("Sum is:", total)

Exercise 4: Multiplication table

num = int(input())
for i in range(1, 11):
    print(num * i)


Exercise 5: Display specific numbers from list

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 75 <= num <= 150:
        print(num)

Exercise 6: Count digits in a number

num = input()
print("Output:", len(num))


Exercise 7: Reverse Number Pattern

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


Exercise 8: Reverse list using loop

list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)


⸻

Exercise 9: Print -10 to -1

for i in range(-10, 0):
    print(i)


⸻

Exercise 10: Message after loop

for i in range(5):
    print(i)
print("Done!")


⸻

Exercise 11: Prime numbers in range

start = 25
end = 50
print("Prime numbers between 25 and 50:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)


⸻

Exercise 12: Fibonacci series

a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end="  ")
    a, b = b, a + b


⸻

Exercise 13: Factorial

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"{num}! = {factorial}")


⸻
4. Return Uncommon Elements of Lists

from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)

    result = []

    for item in c1:
        if item not in c2:
            result.extend([item] * c1[item])
        else:
            diff = c1[item] - c2[item]
            if diff > 0:
                result.extend([item] * diff)

    for item in c2:
        if item not in c1:
            result.extend([item] * c2[item])
        else:
            diff = c2[item] - c1[item]
            if diff > 0:
                result.extend([item] * diff)

    return result

# Examples
print(uncommon_elements([1, 1, 2], [2, 3, 4]))            # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))            # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) # [2, 2, 5]
