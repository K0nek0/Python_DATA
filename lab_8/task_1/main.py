import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS vehicles(
    vehicleId INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT,
    registrationDate DATE,
    color TEXT);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS couriers(
    courierId INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT,
    name TEXT,
    patronymic TEXT,
    passportNumber INTEGER,
    birthDate DATE,
    employmentDate DATE,
    workingDayStart TIME,
    workingDayEnd TIME,
    city TEXT,
    street TEXT,
    house INTEGER,
    flat INTEGER,
    phoneNumber INTEGER);
""")

cur.execute("""INSERT INTO vehicles(brand, registrationDate, color)
    VALUES('Volkswagen', '2019-04-21', 'gray')""")

cur.execute("""UPDATE vehicles
    SET color = 'white'
    WHERE vehicleId = 1
""")

cur.execute("""INSERT INTO vehicles(brand, registrationDate, color)
    VALUES('Mercedes', '2023-11-01', 'black')""")

conn.commit()
