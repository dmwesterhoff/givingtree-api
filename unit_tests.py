from requests.userrequests import UserRequests
from requests.addressrequests import AddressRequests
from requests.accountrequests import AccountRequests
from requests.eventrequests import EventRequests
from requests.transactionrequests import TransactionRequests

print '----- User request tests -----'
user_requests = UserRequests()
user = user_requests.user_with_email('dmwesterhoff@gmail.com')
print user
print

print '----- Address request tests -----'
address_requests = AddressRequests()
address = address_requests.address_with_id(1)
print address
print

print '----- Account request tests -----'
account_requests = AccountRequests()
account = account_requests.account_with_id(1)
print account
print

print '----- Event request tests -----'
event_requests = EventRequests()
event = event_requests.event_with_id(1)
print event
print

print '----- Transaction request tests -----'
transaction_requests = TransactionRequests()
transaction = transaction_requests.transaction_with_id(1)
print transaction
print

