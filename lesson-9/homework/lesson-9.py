
1. Circle Class

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


---

2. Person Class

from datetime import date

class Person:
    def __init__(self, name, country, dob):  # dob format: 'YYYY-MM-DD'
        self.name = name
        self.country = country
        self.dob = date.fromisoformat(dob)

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))


---

3. Calculator Class

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed"


---

4. Shape and Subclasses

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c, height=None):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        if self.height:
            return 0.5 * self.b * self.height
        else:
            s = self.perimeter() / 2
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


---

5. Binary Search Tree Class

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(root, value):
            if not root:
                return Node(value)
            elif value < root.value:
                root.left = _insert(root.left, value)
            else:
                root.right = _insert(root.right, value)
            return root

        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(root, value):
            if not root:
                return False
            elif root.value == value:
                return True
            elif value < root.value:
                return _search(root.left, value)
            else:
                return _search(root.right, value)

        return _search(self.root, value)


---

6. Stack Data Structure

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is empty"


---

7. Linked List Data Structure

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


---

8. Shopping Cart Class

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())


---

9. Stack with Display

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is empty"

    def display(self):
        print("Stack:", self.stack)


---

10. Queue Data Structure

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return "Queue is empty"


---

11. Bank Class

class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            return "Insufficient balance"

    def display(self):
        print(f"Account: {self.account_number}, Name: {self.name}, Balance: {self.balance}")

