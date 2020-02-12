import sqlite3

conn = sqlite3.connect("database2")
cursor = conn.cursor()

try:
    cursor.execute('''CREATE TABLE Работник(Фамилия text,Имя text,Отчество text)''')
except:
    pass
cursor.execute("INSERT INTO Работник(Фамилия,Имя,Отчество) Values ('Комаров', 'Виктор','Павлович')")
conn.commit()
cursor.execute("INSERT INTO Работник(Фамилия,Имя,Отчество) Values ('Иванов', 'Петр','Васильевич')")
conn.commit()
for row in cursor.execute('SELECT * FROM Работник'):
    print(row)

try:
    cursor.execute('''CREATE TABLE Зарплата(Фамилия text,Выплата integer text,Остаток integer)''')
except:
    pass
cursor.execute("INSERT INTO Зарплата(Фамилия,Выплата,Остаток) Values ('Комаров', '5000','5000')")
conn.commit()
cursor.execute("INSERT INTO Зарплата(Фамилия,Выплата,Остаток) Values ('Иванов', '7000','3000')")
conn.commit()
for row in cursor.execute('SELECT * FROM Зарплата'):
    print(row)

try:
    cursor.execute('CREATE TABLE Должность(Фамилия text, Посада Text,Контракт integer)')
except:
    pass
cursor.execute("INSERT INTO Должность(Фамилия,Посада,Контракт) Values ('Комаров', 'Консультант','104')")
conn.commit()
cursor.execute("INSERT INTO Должность(Фамилия,Посада,Контракт) Values ('Иванов', 'Директор','27')")
conn.commit()
for row in cursor.execute('SELECT * FROM Должность'):
    print(row)
