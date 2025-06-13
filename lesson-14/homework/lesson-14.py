1. JSON Parsing (students.json)

import json

# Load and read JSON file
with open('students.json', 'r') as file:
    students = json.load(file)

# Print details of each student
for student in students:
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grade: {student['grade']}")
    print("-" * 30)


 2. Weather API (Tashkent Example)

You must register on https://openweathermap.org/ and get your API key.

import requests

API_KEY = 'your_api_key_here'  # replace with your actual API key
CITY = 'Tashkent'
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Error fetching data:", data.get("message", "Unknown error"))

 3. JSON Modification (books.json)

import json

def load_books():
    try:
        with open('books.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open('books.json', 'w') as f:
        json.dump(books, f, indent=4)

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")
    books.append({"title": title, "author": author, "year": year})
    save_books(books)
    print("Book added!")

def update_book():
    title = input("Enter title of the book to update: ")
    for book in books:
        if book["title"].lower() == title.lower():
            book["author"] = input("New author: ")
            book["year"] = input("New year: ")
            save_books(books)
            print("Book updated!")
            return
    print("Book not found.")

def delete_book():
    title = input("Enter title of the book to delete: ")
    global books
    books = [book for book in books if book["title"].lower() != title.lower()]
    save_books(books)
    print("Book deleted (if it existed).")

books = load_books()

while True:
    print("\n1. Add Book\n2. Update Book\n3. Delete Book\n4. Show All\n5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        for book in books:
            print(book)
    elif choice == '5':
        break
    else:
        print("Invalid option")


 4. Movie Recommendation System (OMDb API)

Register at http://www.omdbapi.com/apikey.aspx to get your free API key.

import requests
import random

API_KEY = 'your_api_key_here'  # Replace with your OMDb API key
genres = {
    "action": ["Mad Max", "John Wick", "Die Hard", "Gladiator"],
    "romance": ["Pride and Prejudice", "The Notebook", "La La Land", "Titanic"],
    "comedy": ["Superbad", "The Hangover", "Step Brothers", "The Mask"]
}

genre = input("Enter a movie genre (action, romance, comedy): ").lower()
if genre in genres:
    movie_title = random.choice(genres[genre])
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
    response = requests.get(url)
    movie = response.json()

    if movie["Response"] == "True":
        print(f"Title: {movie['Title']}")
        print(f"Year: {movie['Year']}")
        print(f"Genre: {movie['Genre']}")
        print(f"Plot: {movie['Plot']}")
        print(f"IMDB Rating: {movie['imdbRating']}")
    else:
        print("Movie not found.")
else:
    print("Genre not supported.")

