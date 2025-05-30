Step 1: Create a Virtual Environment
	1.	Open Command Prompt (Win + R → type cmd → Enter).
	2.	Navigate to the folder where you want to create your project:

cd path\to\your\project\folder

Example:

cd C:\Users\YourName\Desktop\PythonProjects


	3.	Create a virtual environment:

python -m venv myenv


	4.	Activate the virtual environment:

myenv\Scripts\activate

You’ll see something like (myenv) at the beginning of the line — this means it’s activated.

	5.	Install Python packages (like requests and numpy):

pip install requests numpy

 Step 2: Create Custom Modules

Create a new folder named modules (or use your main folder), and create these two files:

📄 math_operations.py

# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
string_utils.py

# string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


⸻
Step 3: Create Custom Packages

📁 geometry Package Structure

Create a folder called geometry and inside it:

geometry/
    __init__.py
    circle.py

📄 geometry/__init__.py

# geometry/__init__.py
from .circle import calculate_area, calculate_circumference

 geometry/circle.py

# geometry/circle.py
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius


⸻

 file_operations Package Structure

Create a folder called file_operations and inside it:

file_operations/
    __init__.py
    file_reader.py
    file_writer.py
file_operations/__init__.py

# file_operations/__init__.py
from .file_reader import read_file
from .file_writer import write_file

file_reader.py

# file_operations/file_reader.py

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

 file_writer.py

# file_operations/file_writer.py

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


⸻

 Step 4: Create a Test File main.py

In the same root directory:

# main.py

from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry import calculate_area, calculate_circumference
from file_operations import write_file, read_file

# Math
print("Add:", add(5, 3))
print("Divide:", divide(10, 2))

# String
print("Reverse:", reverse_string("hello"))
print("Vowels:", count_vowels("OpenAI"))

# Geometry
print("Area:", calculate_area(7))
print("Circumference:", calculate_circumference(7))

# File Ops
write_file("example.txt", "This is a test content.")
print("File content:", read_file("
main.py

