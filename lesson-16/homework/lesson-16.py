

⸻
1. Convert List to 1D Array

import numpy as np

lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)
print("One-dimensional NumPy array:", arr)


⸻
 2. Create 3x3 Matrix (2–10)

matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)


⸻
3. Null Vector (10) & Update Sixth Value

null_vec = np.zeros(10)
null_vec[6] = 11
print(null_vec)


⸻

4. Array from 12 to 38

arr = np.arange(12, 38)
print(arr)


⸻

5. Convert Array to Float Type

int_arr = np.array([1, 2, 3, 4])
float_arr = int_arr.astype(float)
print("Array converted to float:", float_arr)


⸻
 6. Celsius to Fahrenheit Conversion

celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = celsius * 9/5 + 32

print("Values in Centigrade degrees:")
print(celsius)
print("Values in Fahrenheit degrees:")
print(fahrenheit)


⸻

7. Append Values to Array

arr = np.array([10, 20, 30])
new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])
print(new_arr)


⸻
 8. Array Statistical Functions

arr = np.random.rand(10)
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))


⸻
9. Find min and max in 10x10 array

arr = np.random.rand(10, 10)
print("Min value:", np.min(arr))
print("Max value:", np.max(arr))


⸻
10. Create a 3x3x3 array with random values

arr = np.random.rand(3, 3, 3)
print(arr)

