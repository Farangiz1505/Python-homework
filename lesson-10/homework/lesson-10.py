 Homework 1: ToDo List Application

1. Task Class

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False  # False = Incomplete, True = Complete

    def mark_complete(self):
        self.status = True

2. ToDoList Class

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True
        return False

    def list_tasks(self):
        return self.tasks

    def list_incomplete_tasks(self):
        return [task for task in self.tasks if not task.status]

3. Main Program (CLI)

def main():
    todo = ToDoList()
    while True:
        print("\n1. Add Task\n2. Mark Task Complete\n3. Show All Tasks\n4. Show Incomplete Tasks\n5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            date = input("Due Date: ")
            todo.add_task(Task(title, desc, date))
        elif choice == "2":
            title = input("Enter title of task to mark complete: ")
            if not todo.mark_complete(title):
                print("Task not found.")
        elif choice == "3":
            for t in todo.list_tasks():
                print(f"{t.title} - {'Done' if t.status else 'Pending'}")
        elif choice == "4":
            for t in todo.list_incomplete_tasks():
                print(f"{t.title} - Due: {t.due_date}")
        elif choice == "5":
            break

 Homework 2: Simple Blog System

1. Post Class

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

2. Blog Class

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        return self.posts

    def posts_by_author(self, author):
        return [post for post in self.posts if post.author == author]

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title != title]

    def edit_post(self, old_title, new_title, new_content):
        for post in self.posts:
            if post.title == old_title:
                post.title = new_title
                post.content = new_content
                return True
        return False

    def latest_posts(self, count=5):
        return self.posts[-count:]

3. Main Program (CLI)

def blog_cli():
    blog = Blog()
    while True:
        print("\n1. Add Post\n2. List Posts\n3. Posts by Author\n4. Delete Post\n5. Edit Post\n6. Latest Posts\n7. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
        elif choice == "2":
            for p in blog.list_posts():
                print(f"{p.title} by {p.author}")
        elif choice == "3":
            auth = input("Author: ")
            for p in blog.posts_by_author(auth):
                print(p.title)
        elif choice == "4":
            title = input("Title to delete: ")
            blog.delete_post(title)
        elif choice == "5":
            old = input("Old Title: ")
            new = input("New Title: ")
            content = input("New Content: ")
            blog.edit_post(old, new, content)
        elif choice == "6":
            for p in blog.latest_posts():
                print(p.title)
        elif choice == "7":
            break
Homework 3: Simple Banking System

1. Account Class

class Account:
    def __init__(self, number, holder, balance=0):
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def __str__(self):
        return f"{self.holder} | Acc#: {self.number} | Balance: ${self.balance}"

2. Bank Class

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.number] = account

    def get_account(self, number):
        return self.accounts.get(number)

    def transfer(self, from_acc, to_acc, amount):
        from_account = self.get_account(from_acc)
        to_account = self.get_account(to_acc)
        if from_account and to_account and from_account.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False

3. Main Program (CLI)

def bank_cli():
    bank = Bank()
    while True:
        print("\n1. Add Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transfer\n6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            num = input("Account Number: ")
            name = input("Holder Name: ")
            bank.add_account(Account(num, name))
        elif choice == "2":
            num = input("Account Number: ")
            amt = float(input("Amount: "))
            acc = bank.get_account(num)
            if acc:
                acc.deposit(amt)
        elif choice == "3":
            num = input("Account Number: ")
            amt = float(input("Amount: "))
            acc = bank.get_account(num)
            if acc and not acc.withdraw(amt):
                print("Insufficient funds.")
        elif choice == "4":
            num = input("Account Number: ")
            acc = bank.get_account(num)
            if acc:
                print(acc)
        elif choice == "5":
            from_acc = input("From Account: ")
            to_acc = input("To Account: ")
            amt = float(input("Amount: "))
            if not bank.transfer(from_acc, to_acc, amt):
                print("Transfer failed.")
        elif choice == "6":
            break
