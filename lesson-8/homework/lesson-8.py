1. ZeroDivisionError ni ushlash:
try:
    a = 10
    b = 0
    natija = a / b
except ZeroDivisionError:
    print("Xatolik: Sonni nolga bo‘lib bo‘lmaydi!")
 2. Foydalanuvchi kiritgan qiymat integer bo‘lmasa ValueError:
try:
    num = int(input("Iltimos, butun son kiriting: "))
except ValueError:
    print("Xatolik: Bu butun son emas!")
 3. Fayl topilmasa FileNotFoundError ushlash:
try:
    with open("ma'lumot.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Xatolik: Fayl topilmadi!")
 4. Ikkita son kiritishda son bo‘lmasa TypeError ko‘rsatish:

try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
except ValueError:
    raise TypeError("Xatolik: Iltimos, faqat son kiriting!")
5. PermissionError (ruxsat xatosi)ni ushlash:

try:
    with open("himoyalangan_fayl.txt", "r") as f:
        content = f.read()
except PermissionError:
    print("Xatolik: Faylga kirish uchun ruxsat yo‘q!")
 6. IndexError ni ushlash:

my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Xatolik: Indeks chegaradan tashqarida!")
 7. KeyboardInterrupt (Ctrl+C bilan bekor qilish) ni ushlash:

try:
    num = int(input("Son kiriting: "))
except KeyboardInterrupt:
    print("\nXatolik: Kirishni foydalanuvchi bekor qildi!")
 8. ArithmeticError ni ushlash:

try:
    a = 10
    b = 0
    natija = a // b
except ArithmeticError:
    print("Xatolik: Arifmetik xato yuz berdi!")
 9. UnicodeDecodeError ni ushlash:

try:
    with open("fayl.txt", "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    print("Xatolik: Fayl kodlashida muammo bor!")
10. AttributeError ni ushlash:

my_list = [1, 2, 3]
try:
    my_list.push(4)  # push metodi listda yo‘q
except AttributeError:
    print("Xatolik: Bu obyektda bunday atribut yo‘q!")

# Python File Input/Output — Misollar va Yechnolar
 1. Fayldan butun matnni o‘qish:

with open("matn.txt", "r") as f:
    data = f.read()
print(data)
 2. Fayldan birinchi n qatorni o‘qish:

n = 3
with open("matn.txt", "r") as f:
    for i in range(n):
        print(f.readline().strip())
3. Faylga matn qo‘shish va ko‘rsatish:

with open("matn.txt", "a") as f:
    f.write("\nYangi qo‘shimcha matn.")

with open("matn.txt", "r") as f:
    print(f.read())
 4. Fayldan oxirgi n qatorni o‘qish:

n = 3
with open("matn.txt", "r") as f:
    lines = f.readlines()
    for line in lines[-n:]:
        print(line.strip())
 5. Faylni qatorma-qator o‘qib, ro‘yxatga saqlash:

with open("matn.txt", "r") as f:
    lines = f.readlines()
print(lines)
 6. Faylni qatorma-qator o‘qib, bitta o‘zgaruvchiga saqlash:

with open("matn.txt", "r") as f:
    content = f.read()
print(content)
 7. Faylni qatorma-qator o‘qib, arrayga saqlash (list bilan bir xil):

with open("matn.txt", "r") as f:
    arr = f.readlines()
print(arr)
 8. Eng uzun so‘zlarni topish:
with open("matn.txt", "r") as f:
    words = f.read().split()
max_len = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_len]
print("Eng uzun so‘zlar:", longest_words)
# 9. Fayldagi qatorlar sonini hisoblash:


with open("matn.txt", "r") as f:
    count = sum(1 for line in f)
print("Qatorlar soni:", count)
 10. So‘zlarning fayldagi takrorlanish sonini hisoblash:
from collections import Counter

with open("matn.txt", "r") as f:
    words = f.read().lower().split()
counts = Counter(words)
print(counts)
 11. Fayl hajmini olish:

import os

size = os.path.getsize("matn.txt")
print(f"Fayl hajmi: {size} bayt")
 12. Ro‘yxatni faylga yozish:

my_list = ["Olma", "Banan", "Gilos"]
with open("mevalar.txt", "w") as f:
    for item in my_list:
        f.write(item + "\n")
13. Fayl mazmunini boshqa faylga ko‘chirish:

with open("manba.txt", "r") as source, open("nusxa.txt", "w") as dest:
    for line in source:
        dest.write(line)
 14. Birinchi va ikkinchi fayldagi qatorlarni qo‘shib chiqish:

with open("fayl1.txt", "r") as f1, open("fayl2.txt", "r") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())
 15. Fayldan tasodifiy qator o‘qish:

import random

with open("matn.txt", "r") as f:
    lines = f.readlines()
print(random.choice(lines).strip())
16. Fayl yopilgan yoki yopilmaganini tekshirish:

f = open("matn.txt", "r")
print(f.closed)  # False
f.close()
print(f.closed)  # True
17. Fayldagi yangi qator belgilarini olib tashlash:

with open("matn.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)
 18. Fayldagi so‘zlar sonini hisoblash (vergul bilan ajratilgan so‘zlar ham):

import re

with open("matn.txt", "r") as f:
    text = f.read()
words = re.split(r'[,\s]+', text.strip())
print("So‘zlar soni:", len(words))
19. Fayldan belgilarni ajratib ro‘yxatga joylash:

with open("matn.txt", "r") as f:
    chars = list(f.read())
print(chars)
 20. A.txt, B.txt, ... Z.txt nomli 26 fayl yaratish:

for c in range(65, 91):  # ASCII kodlari A dan Z gacha
    with open(chr(c) + ".txt", "w") as f:
        f.write("")
 21. Har qatorda belgilangan sonli harflar bilan ingliz alifbosini faylga yozish:

harf_soni = 5  # har qatorda nechta harf yoziladi
alfavit = [chr(c) for c in range(65, 91)]  # A-Z

with open("alphabet.txt", "w") as f:
    for i in range(0, len(alfavit), harf_soni):
        f.write("".join(alfavit[i:i+harf_soni]) + "\n")

