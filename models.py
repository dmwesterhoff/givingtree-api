import peewee
from peewee import *
import json

# Setup and connect to the database
db = peewee.MySQLDatabase("the_giving_tree", host="localhost", user="root")
db.connect()

class User(Model):
    email = CharField(unique=True)
    password = CharField()
    first_name = CharField()
    middle_name = CharField()
    last_name = CharField()
    date_of_birth = CharField() # YYYYMMDD

    def dict(self):
        return vars(self)['_data']

    def json_string(self):
        return json.dumps(self.dict())

    def __repr__(self):
        return self.json_string()

    def __str__(self):
        return json.dumps(self.dict(), indent=3, sort_keys=True)

    class Meta:
        database = db

class Address(Model):
    line1 = CharField()
    line2 = CharField(null=True)
    city = CharField()
    postal_code = CharField()
    state = CharField()
    country = CharField()

    def dict(self):
        return vars(self)['_data']

    def json_string(self):
        return json.dumps(self.dict())

    def __repr__(self):
        return self.json_string()

    def __str__(self):
        return json.dumps(self.dict(), indent=3, sort_keys=True)

    class Meta:
        database = db

class Account(Model):
    user = ForeignKeyField(User, related_name='account')
    debit_card = CharField()
    expiry_date = CharField() # YYYYMM
    alias = CharField()
    address = ForeignKeyField(Address, related_name='account')

    def dict(self):
        return vars(self)['_data']

    def json_string(self):
        return json.dumps(self.dict())

    def __repr__(self):
        return self.json_string()

    def __str__(self):
        return json.dumps(self.dict(), indent=3, sort_keys=True)

    class Meta:
        database = db

class Event(Model):
    name = CharField()
    body = TextField(null=True)
    owner = ForeignKeyField(User, related_name='events')
    time_begins = CharField() # MM-DD-YYYY HH:MM:SS
    time_ends = CharField() # MM-DD-YYYY HH:MM:SS
    amount_raised = IntegerField(default=0) # Amount in USD, implied decimal
    latitude = FloatField()
    longitude = FloatField()
    address =  ForeignKeyField(Address, related_name='event')

    def dict(self):
        return vars(self)['_data']

    def json_string(self):
        return json.dumps(self.dict())

    def __repr__(self):
        return self.json_string()

    def __str__(self):
        return json.dumps(self.dict(), indent=3, sort_keys=True)

    class Meta:
        database = db

class Transaction(Model):
    to_user = ForeignKeyField(User, related_name='transactions_sent')
    from_user = ForeignKeyField(User, related_name='transaction_received')
    amount = IntegerField() # Amount in USD, implied decimal
    timestamp = CharField() # MM-DD-YYYY HH:MM:SS
    note = TextField(null=True)

    def dict(self):
        return vars(self)['_data']

    def json_string(self):
        return json.dumps(self.dict())

    def __repr__(self):
        return self.json_string()

    def __str__(self):
        return json.dumps(self.dict(), indent=3, sort_keys=True)

    class Meta:
        database = db
