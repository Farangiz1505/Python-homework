

⸻

1. Create the database and the Roster table

If you’re using SQLite, MySQL, or PostgreSQL, you’d first create the table like this (assuming the database already exists):

CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);


⸻

2. Insert the values into the table

INSERT INTO Roster (Name, Species, Age)
VALUES 
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29);


⸻

3. Update the name of Jadzia Dax to Ezri Dax

UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax';


⸻

4. Display the Name and Age of everyone classified as Bajoran

SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran';


l
