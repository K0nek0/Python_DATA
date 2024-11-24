from peewee import *
from datetime import date, time

db = SqliteDatabase("database.db")


class Couriers(Model):
    courierId = PrimaryKeyField()
    surname = TextField()
    name = TextField()
    patronymic = TextField()
    passportNumber = IntegerField()
    birthDate = DateField()
    employmentDate = DateField()
    workingDayStart = TimeField()
    workingDayEnd = TimeField()
    city = TextField()
    street = TextField()
    house = IntegerField()
    flat = IntegerField()
    phoneNumber = IntegerField()

    class Meta:
        database = db


class Vehicles(Model):
    vehicleId = PrimaryKeyField()
    brand = TextField()
    registrationDate = DateField()
    color = TextField()

    class Meta:
        database = db


class Senders(Model):
    senderId = PrimaryKeyField()
    surname = TextField()
    name = TextField()
    patronymic = TextField()
    birthDate = DateField()
    postIndex = IntegerField()
    city = TextField()
    street = TextField()
    house = IntegerField()
    flat = IntegerField()
    phoneNumber = IntegerField()

    class Meta:
        database = db


class Recipients(Model):
    recipientId = PrimaryKeyField()
    surname = TextField()
    name = TextField()
    patronymic = TextField()
    birthDate = DateField()
    postIndex = IntegerField()
    city = TextField()
    street = TextField()
    house = IntegerField()
    flat = IntegerField()
    phoneNumber = IntegerField()

    class Meta:
        database = db


class Orders(Model):
    orderId = PrimaryKeyField()
    senderId = ForeignKeyField(Senders, backref="Orders")
    recipientId = ForeignKeyField(Recipients, backref="Orders")
    orderDate = DateField()
    deliveryDate = DateField()
    deliveryCost = IntegerField()
    courierId = ForeignKeyField(Couriers, backref="Orders")
    vehicleId = ForeignKeyField(Vehicles, backref="Orders")

    class Meta:
        database = db


db.connect()
db.create_tables([Senders, Recipients, Orders])


sender1, created = Senders.get_or_create(surname="Timoshchenko",
                                         name="Nikolay",
                                         patronymic="Stepanovich",
                                         birthDate=date(2004, 1, 4),
                                         postIndex=257999,
                                         city="Amsterdam",
                                         street="Krutaya Street",
                                         house=44,
                                         flat=4,
                                         phoneNumber=88005553535)
sender2, created = Senders.get_or_create(surname="Ivanov",
                                         name="Ivan",
                                         patronymic="Ivanovich",
                                         birthDate=date(1972, 6, 17),
                                         postIndex=257899,
                                         city="Amsterdam",
                                         street="Meneekrutaya Street",
                                         house=20,
                                         flat=1,
                                         phoneNumber=30430403229)


recipient1, created = Recipients.get_or_create(surname="Chelovekov",
                                               name="Chelovek",
                                               patronymic="Chelovekovich",
                                               birthDate=date(1980, 2, 3),
                                               postIndex="235227",
                                               city="Mobil",
                                               street="Bruh",
                                               house=1,
                                               flat=1,
                                               phoneNumber=12312312312)
recipient2, created = Recipients.get_or_create(surname="Testov",
                                               name="Test",
                                               patronymic="Testovich",
                                               birthDate=date(1800, 1, 1),
                                               postIndex="213245",
                                               city="Kaliningrad",
                                               street="Testovaya Street",
                                               house=1,
                                               flat=1,
                                               phoneNumber=2315663)


courier1, created = Couriers.get_or_create(
    surname="Antonov",
    name="Anton",
    patronymic="-",
    passportNumber=999922,
    birthDate=date(2000, 6, 11),
    employmentDate=date(2023, 8, 11),
    workingDayStart=time(9, 16, 13),
    workingDayEnd=time(18, 37, 56),
    city="Amsterdam",
    street="Street",
    house=11,
    flat=99,
    phoneNumber=28712861
)

order1, created = Orders.get_or_create(senderId=sender1,
                                       recipientId=recipient1,
                                       courierId=courier1,
                                       vehicleId=Vehicles.get(Vehicles.vehicleId == 1),
                                       orderDate=date(2024, 12, 1),
                                       deliveryDate=date(2025, 1, 13),
                                       deliveryCost=1600,
                                       )
order2, created = Orders.get_or_create(senderId=sender2,
                                       recipientId=recipient2,
                                       courierId=courier1,
                                       vehicleId=Vehicles.get(Vehicles.vehicleId == 1),
                                       orderDate=date(2024, 12, 1),
                                       deliveryDate=date(2025, 1, 13),
                                       deliveryCost=2600,
                                       )

db.close()
