import peewee
from peewee import *
import json

# Setup and connect to the database
db = peewee.MySQLDatabase("the_giving_tree", host="localhost", user="root")
db.connect()

class User(Model):
    phone_number = CharField(unique=True)
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

class Organization(Model):
    name = CharField()
    image = CharField(null=True)

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
    user = ForeignKeyField(User, null=True, related_name='account')
    organization = ForeignKeyField(Organization,null=True,related_name='account')
    address = ForeignKeyField(Address, related_name='account')
    debit_card = CharField()
    expiry_date = CharField() # YYYYMM
    cvc = CharField(null=True)
    alias = CharField()

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
    owner = ForeignKeyField(User, null=True,related_name='events')
    organization = ForeignKeyField(Organization, null=True,related_name='events')
    address =  ForeignKeyField(Address, related_name='event')
    name = CharField()
    body = TextField(null=True)
    time_begins = CharField() # MM-DD-YYYY HH:MM:SS
    time_ends = CharField() # MM-DD-YYYY HH:MM:SS
    amount_raised = IntegerField(default=0) # Amount in USD, implied decimal
    latitude = FloatField()
    longitude = FloatField()

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
    event = ForeignKeyField(Event, related_name='transactions')
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
