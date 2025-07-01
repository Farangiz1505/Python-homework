
 1. Customer Purchases Analysis

Maqsad: Har bir mijoz qancha pul sarflaganini topish va eng ko‘p xarid qilgan 5 nafar mijozni aniqlash.

 Kod:

import sqlite3
import pandas as pd

# Bazaga ulanish
conn = sqlite3.connect("chinook.db")

# Kerakli jadval ma'lumotlarini yuklash
invoices = pd.read_sql_query("SELECT * FROM Invoice", conn)
customers = pd.read_sql_query("SELECT * FROM Customer", conn)

# Har bir mijoz qancha pul sarflaganini topish
customer_total = invoices.groupby("CustomerId")["Total"].sum().reset_index()

# Top 5 eng ko‘p sarflagan mijozlar
top_5 = customer_total.sort_values(by="Total", ascending=False).head(5)

# Customer ID, ismi va umumiy sarflagan summani ko‘rsatish
top_5 = top_5.merge(customers, on="CustomerId")
top_5_result = top_5[["CustomerId", "FirstName", "LastName", "Total"]]
print("Top 5 Customers by Total Purchases:")
print(top_5_result)


⸻

 2. Album vs. Individual Track Purchases

Maqsad: Mijozlar asosan butun albomni xarid qiladimi yoki alohida treklarni afzal ko‘radimi, foizlarda aniqlash.

 Asosiy tushuncha:

Agar mijoz bir albomdagi barcha treklarni olgan bo‘lsa, bu “album purchase” hisoblanadi. Agar ba’zi treklarni olgan bo‘lsa, bu “individual track purchase” bo‘ladi.



# Kerakli jadvallarni chaqiramiz
invoice_lines = pd.read_sql_query("SELECT * FROM InvoiceLine", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track", conn)

# InvoiceLine'ni track bilan birlashtirish (albumId'ni olish uchun)
invoice_tracks = invoice_lines.merge(tracks, on="TrackId")

# Har bir mijoz va album uchun ular sotib olgan tracklar sonini hisoblash
customer_album_track_counts = invoice_tracks.groupby(["CustomerId", "AlbumId"]).agg({"TrackId": "nunique"}).reset_index()
customer_album_track_counts.rename(columns={"TrackId": "PurchasedTracks"}, inplace=True)

# Har bir albomda nechta track borligini aniqlaymiz
album_track_counts = tracks.groupby("AlbumId")["TrackId"].nunique().reset_index()
album_track_counts.rename(columns={"TrackId": "TotalTracks"}, inplace=True)

# Mijozning xaridi bilan solishtirish
df = customer_album_track_counts.merge(album_track_counts, on="AlbumId")

# To'liq albom sotib olinganmi yoki yo‘qmi aniqlash
df["FullAlbum"] = df["PurchasedTracks"] == df["TotalTracks"]

# Har bir mijoz uchun u albomlarni to‘liq sotib olganmi yoki qisman
customer_album_pref = df.groupby("CustomerId")["FullAlbum"].any().reset_index()

# Agar hech bir albom to‘liq xarid qilinmagan bo‘lsa -> individual track buyer
customer_album_pref["PurchaseType"] = customer_album_pref["FullAlbum"].apply(
    lambda x: "Album Buyer" if x else "Individual Track Buyer"
)

# Foizlarni hisoblash
summary = customer_album_pref["PurchaseType"].value_counts(normalize=True) * 100
print("\nPercentage of Customers by Purchase Preference:")
print(summary)


⸻

📊 Natijalar:
	1.	Top 5 mijoz — CustomerId, FirstName, LastName, va sarflagan Total.
	2.	Mijozlarning xarid odatlari: necha foizi albomni butunlay olgan, necha foizi individual trek olgan.

⸻



