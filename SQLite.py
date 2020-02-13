import sqlite3

conn = sqlite3.connect("database")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE Работник(ID integer PRIMARY KEY,
Фамилия text NOT NULL,
Имя text NOT NULL,
Отчество text NOT NULL)''')

cursor.execute("INSERT INTO Работник(Фамилия,Имя,Отчество) Values ('Комаров', 'Виктор','Павлович')")
conn.commit()
cursor.execute("INSERT INTO Работник(Фамилия,Имя,Отчество) Values ('Иванов', 'Петр','Васильевич')")
conn.commit()
for row in cursor.execute('SELECT * FROM Работник'):
    print(row)


cursor.execute('''CREATE TABLE Зарплата(ID integer PRIMARY KEY NOT NULL,
Фамилия text NOT NULL,
Выплата integer NOT NULL
,Остаток integer NOT NULL,FOREIGN KEY (ID) REFERENCES Работник (ID))''')

cursor.execute("INSERT INTO Зарплата(Фамилия,Выплата,Остаток) Values ('Комаров', '5000','5000')")
conn.commit()
cursor.execute("INSERT INTO Зарплата(Фамилия,Выплата,Остаток) Values ('Иванов', '7000','3000')")
conn.commit()
for row in cursor.execute('SELECT * FROM Зарплата'):
    print(row)

cursor.execute('''CREATE TABLE Должность(ID integer PRIMARY KEY NOT NULL,
Фамилия text NOT NULL,
Посада Text NOT NULL,
Контракт integer NOT NULL,FOREIGN KEY (ID) REFERENCES Работник (ID))''')

cursor.execute("INSERT INTO Должность(Фамилия,Посада,Контракт) Values ('Комаров', 'Консультант','104')")
conn.commit()
cursor.execute("INSERT INTO Должность(Фамилия,Посада,Контракт) Values ('Иванов', 'Директор','27')")
conn.commit()
for row in cursor.execute('SELECT * FROM Должность'):
    print(row)