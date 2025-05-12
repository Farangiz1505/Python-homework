# 1. Create and Access List Elements
fruits = ["apple", "banana", "cherry", "mango", "grape"]
print("Third fruit:", fruits[2])

# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Concatenated list:", combined_list)

# 3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print("First, middle, last:", new_list)

# 4. Convert List to Tuple
favorite_movies = ["Inception", "Titanic", "Avengers", "Matrix", "Interstellar"]
movies_tuple = tuple(favorite_movies)
print("Movies tuple:", movies_tuple)

# 5. Check Element in a List
cities = ["London", "Paris", "Rome", "Berlin"]
print("Is Paris in the list?", "Paris" in cities)

# 6. Duplicate a List Without Using Loops
original = [1, 2, 3]
duplicated = original * 2
print("Duplicated list:", duplicated)

# 7. Swap First and Last Elements of a List
nums = [1, 2, 3, 4, 5]
nums[0], nums[-1] = nums[-1], nums[0]
print("After swap:", nums)

# 8. Slice a Tuple
numbers_tuple = tuple(range(1, 11))
print("Slice from index 3 to 7:", numbers_tuple[3:8])

# 9. Count Occurrences in a List
colors = ["blue", "red", "blue", "green", "blue"]
count_blue = colors.count("blue")
print("Blue appears:", count_blue, "times")

# 10. Find the Index of an Element in a Tuple
animals = ("cat", "dog", "lion", "tiger")
lion_index = animals.index("lion")
print("Index of lion:", lion_index)

# 11. Merge Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Merged tuple:", merged_tuple)

# 12. Find the Length of a List and Tuple
sample_list = [10, 20, 30]
sample_tuple = (40, 50, 60, 70)
print("List length:", len(sample_list))
print("Tuple length:", len(sample_tuple))

# 13. Convert Tuple to List
num_tuple = (1, 2, 3, 4, 5)
num_list = list(num_tuple)
print("Converted list:", num_list)

# 14. Find Maximum and Minimum in a Tuple
values = (3, 9, 1, 7, 5)
print("Max:", max(values))
print("Min:", min(values))

# 15. Reverse a Tuple
words = ("hello", "world", "python", "tuple")
reversed_tuple = words[::-1]
print("Reversed tuple:", reversed_tuple)
