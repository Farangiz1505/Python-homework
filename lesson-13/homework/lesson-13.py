

1. Age Calculator

from datetime import datetime
from dateutil.relativedelta import relativedelta

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()

age = relativedelta(today, birthdate)
print(f"You are {age.years} years, {age.months} months, and {age.days} days 

2. Days Until Next Birthday

from datetime import datetime, timedelta

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()

next_birthday = birthdate.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days
print(f"There are {days_left} days left until your next birthday.")


⸻

3. Meeting Scheduler

from datetime import datetime, timedelta

current_str = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
hours = int(input("Meeting duration - Hours: "))
minutes = int(input("Meeting duration - Minutes: "))

start = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
end = start + timedelta(hours=hours, minutes=minutes)

print(f"The meeting will end at: {end}")


⸻

4. Timezone Converter

from datetime import datetime
import pytz

date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
from_tz = input("Enter your timezone (e.g., Asia/Tashkent): ")
to_tz = input("Enter target timezone (e.g., Europe/London): ")

from_zone = pytz.timezone(from_tz)
to_zone = pytz.timezone(to_tz)

naive_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
from_dt = from_zone.localize(naive_dt)
to_dt = from_dt.astimezone(to_zone)

print("Converted date and time:", to_dt.strftime("%Y-%m-%d %H:%M (%Z)"))


⸻

5. Countdown Timer

from datetime import datetime
import time

future_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    if future_time <= now:
        print("Time's up!")
        break
    remaining = future_time - now
    print("Time remaining:", remaining, end="\r")
    time.sleep(1)


⸻

6. Email Validator

import re

email = input("Enter your email address: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")


⸻

7. Phone Number Formatter

number = input("Enter a 10-digit phone number: ")

if len(number) == 10 and number.isdigit():
    formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
    print("Formatted phone number:", formatted)
else:
    print("Invalid phone number.")


⸻

8. Password Strength Checker

import re

password = input("Enter your password: ")
length = len(password) >= 8
uppercase = re.search(r'[A-Z]', password)
lowercase = re.search(r'[a-z]', password)
digit = re.search(r'\d', password)

if length and uppercase and lowercase and digit:
    print("Strong password.")
else:
    print("Weak password. Make sure it has at least 8 characters, one uppercase letter, one lowercase letter, and one digit.")


⸻

9. Word Finder

text = "This is a sample text. This text is used for testing word finding."
word = input("Enter the word to search for: ")

words = text.lower().split()
found = [i for i, w in enumerate(words) if w.strip(".,!?") == word.lower()]

print(f"Found {len(found)} occurrences at positions: {found}")


⸻

10. Date Extractor

import re

text = input("Enter text with dates (e.g., 2023-05-10 or 10/06/2022): ")

# Match formats like YYYY-MM-DD or DD/MM/YYYY
pattern = r'\b(?:\d{4}-\d{2}-\d{2})|\b(?:\d{2}/\d{2}/\d{4})'

dates = re.findall(pattern, text)
print("Dates found:", dates)
