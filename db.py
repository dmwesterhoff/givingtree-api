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
db.drop_tables([User,Organization,Address,Account,Event,Transaction])
db.create_tables([User,Organization,Address,Account,Event,Transaction])

# Sample Create Statements
dmwesterhoff = User.create(phone_number='15103665680',first_name='David',middle_name='Michael',last_name='Westerhoff',date_of_birth='03061992')

tco = User.create(phone_number='16504307593',first_name='Tim', middle_name='C', last_name='Co', date_of_birth='04161992')

cancer_awareness = Organization.create(name='Cancer Awareness Organization')

david_address = Address.create(line1='1663 Bellville Way',city='Sunnyvale',postal_code='94566',state='CA',country='USA')

tim_address = Address.create(line1='365 Sunfish Ct',city='Foster City',postal_code='94404',state='CA',country='USA')

test_account_1 = Account.create(user=1,debit_card='0000000000000000',expiry_date='201710',alias='Debit Card',address=1,cvc='222')

test_account_2 = Account.create(user=2,debit_card='9999999999999999',expiry_date='201801',alias='Credit Crd',address=2,cvc='111')

test_event = Event.create(name='Hooka Session', owner=1, time_begins='08-21-2015 06:10:00', time_ends='08-21-2015 09:15:00', latitude=00.00, longitude=00.00, address=1)

test_transaction = Transaction.create(to_user=1, from_user=2, event=1, amount=10000, timestamp='06-21-2015 06:25:00')
