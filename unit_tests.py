from requests.userrequests import UserRequests
from requests.addressrequests import AddressRequests
from requests.accountrequests import AccountRequests
from requests.eventrequests import EventRequests
from requests.transactionrequests import TransactionRequests

user_requests = UserRequests()
user = user_requests.user_with_email('dmwesterhoff@gmail.com')
print user
print

address_requests = AddressRequests()
address = address_requests.address_with_id(1)
print address
print

account_requests = AccountRequests()
account = account_requests.account_with_id(1)
print account
print

event_requests = EventRequests()
event = event_requests.event_with_id(1)
print event
print

transaction_requests = TransactionRequests()
transaction = transaction_requests.transaction_with_id(1)
print transaction
print

