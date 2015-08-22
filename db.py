import peewee
from peewee import *
from models import *
# Setup and connect to the database
db = peewee.MySQLDatabase("the_giving_tree", host="localhost", user="root")
db.connect()

# Testing Queries
# dmw = User.get(User.email == 'dmwesterhoff@gmail.com')
# print dmw.first_name

# for account in dmw.account:
#    print account.user_id

# account = Account.get(Account.user == 'dmwesterhoff@gmail.com')
# print account.alias

# Renew tables
db.drop_tables([User,Address,Account,Event,Transaction])
db.create_tables([User,Address,Account,Event,Transaction])

# Sample Create Statements
dmwesterhoff = User.create(email='dmwesterhoff@gmail.com',password='test',first_name='David',middle_name='Michael',last_name='Westerhoff',date_of_birth='03061992')

tco = User.create(email='timco92@gmail.com', password='test', first_name='Tim', middle_name='C', last_name='Co', date_of_birth='04161992')

test_address = Address.create(line1='1663 Bellville Way',city='Sunnyvale',postal_code='94566',state='CA',country='USA')

test_account = Account.create(user=1,debit_card='0000000000000000',expiry_date='201710',alias='Debit Card',address=1)

test_event = Event.create(name='Hooka Session', owner=1, time_begins='08-21-2015 06:10:00', time_ends='08-21-2015 09:15:00', latitude=00.00, longitude=00.00, address=1)

test_transaction = Transaction.create(to_user=1, from_user=2, amount=10000, timestamp='06-21-2015 06:25:00')
