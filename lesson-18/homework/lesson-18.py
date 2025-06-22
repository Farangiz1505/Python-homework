

⸻

✅ Homework 2 — StackOverflow savollar jadvali

1. 2014-yilgacha yaratilgan savollar:

df[df['creationdate'] < '2014-01-01']

2. Skori 50 dan katta savollar:

df[df['score'] > 50]

3. Skori 50 dan 100 gacha bo‘lgan savollar:

df[(df['score'] >= 50) & (df['score'] <= 100)]

4. Scott Boston tomonidan javob berilgan savollar:

df[df['ans_name'] == 'Scott Boston']

5. Quyidagi 5 foydalanuvchi tomonidan javob berilgan savollar (masalan):

users = ['Unutbu', 'jezrael', 'cs95', 'Scott Boston', 'Warren Weckesser']
df[df['ans_name'].isin(users)]

6. 2014 yil mart va oktyabr oralig‘ida, Unutbu javob bergan, skori 5 dan kichik savollar:

df[
    (df['creationdate'] >= '2014-03-01') & 
    (df['creationdate'] <= '2014-10-31') & 
    (df['ans_name'] == 'Unutbu') & 
    (df['score'] < 5)
]

7. Skori 5–10 orasida yoki ko‘rilganlar soni 10,000 dan ko‘p bo‘lgan savollar:

df[
    ((df['score'] >= 5) & (df['score'] <= 10)) | 
    (df['viewcount'] > 10000)
]

8. Scott Boston tomonidan javob berilmagan savollar:

df[df['ans_name'] != 'Scott Boston']


⸻

✅ Homework 3 — Titanic ma’lumotlar to‘plami

1. Ayol, 1-sinf, yoshi 20–30 orasida:

titanic_df[
    (titanic_df['Sex'] == 'female') & 
    (titanic_df['Pclass'] == 1) & 
    (titanic_df['Age'] >= 20) & 
    (titanic_df['Age'] <= 30)
]

2. Narxi $100 dan yuqori bo‘lgan yo‘lovchilar:

titanic_df[titanic_df['Fare'] > 100]

3. Yolg‘iz bo‘lgan va omon qolgan yo‘lovchilar:

titanic_df[
    (titanic_df['Survived'] == 1) & 
    (titanic_df['SibSp'] == 0) & 
    (titanic_df['Parch'] == 0)
]

4. ‘C’ portidan chiqib, $50 dan ortiq to‘laganlar:

titanic_df[
    (titanic_df['Embarked'] == 'C') & 
    (titanic_df['Fare'] > 50)
]

5. Hamroh va oiladoshlari bo‘lganlar:

titanic_df[
    (titanic_df['SibSp'] > 0) & 
    (titanic_df['Parch'] > 0)
]

6. 15 yoshgacha bo‘lgan va omon qolmaganlar:

titanic_df[
    (titanic_df['Age'] <= 15) & 
    (titanic_df['Survived'] == 0)
]

7. Cabin ko‘rsatilgan va $200 dan ko‘p to‘laganlar:

titanic_df[
    (titanic_df['Cabin'].notna()) & 
    (titanic_df['Fare'] > 200)
]

8. PassengerId toq bo‘lgan yo‘lovchilar:

titanic_df[titanic_df['PassengerId'] % 2 == 1]

9. Takrorlanmagan (unikal) chiptaga ega bo‘lgan yo‘lovchilar:

titanic_df[titanic_df['Ticket'].duplicated(keep=False) == False]

10. Ismida ‘Miss’ bo‘lgan, 1-sinfdagi ayollar:

titanic_df[
    (titanic_df['Name'].str.contains('Miss')) & 
    (titanic_df['Pclass'] == 1) & 
    (titanic_df['Sex'] == 'female')
]


