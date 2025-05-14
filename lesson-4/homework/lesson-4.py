

Dictionary Exercises

1. Sort a Dictionary by Value

my_dict = {'a': 3, 'b': 1, 'c': 2}

# Ascending
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", sorted_asc)

# Descending
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_desc)


---

2. Add a Key to a Dictionary

my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)


---

3. Concatenate Multiple Dictionaries

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Method 1: Using update()
result = {}
for d in (dic1, dic2, dic3):
    result.update(d)

print(result)


---

4. Generate a Dictionary with Squares (n = 5)

n = 5
squares = {x: x**2 for x in range(1, n + 1)}
print(squares)


---

5. Dictionary of Squares (1 to 15)

squares = {x: x**2 for x in range(1, 16)}
print(squares)


---

Set Exercises

1. Create a Set

my_set = {1, 2, 3}
print(my_set)


---

2. Iterate Over a Set

my_set = {10, 20, 30}
for item in my_set:
    print(item)


---

3. Add Member(s) to a Set

my_set = {1, 2}
my_set.add(3)  # Add one item
my_set.update([4, 5])  # Add multiple items
print(my_set)


---

4. Remove Item(s) from a Set

my_set = {1, 2, 3, 4}
my_set.remove(2)  # Raises error if item not found
print(my_set)


---

5. Remove an Item if Present in the Set

my_set = {1, 2, 3}
my_set.discard(2)  # No error if item is missing
print(my_set)



