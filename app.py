from flask import Flask, request
from flask_restful import Resource, Api
from models import *
from requests.userrequests import UserRequests
from requests.accountrequests import AccountRequests
from requests.addressrequests import AddressRequests
from requests.eventrequests import EventRequests
from requests.transactionrequests import TransactionRequests
from requests.organizationrequests import OrganizationRequests

app = Flask(__name__)
api = Api(app)

@api.resource('/status/')
class Status(Resource):
    def get(self):
        return {'status':'success'}

    def delete(self):
        return {'status':'success'}

@api.resource('/users/<int:id>/addresses/')
class UserAddressViewSet(Resource):
    def __init__(self):
        self.accounts = AccountRequests()

    def get(self,id):
        for account in self.accounts.accounts():
            if account["user"] == id:
                address = Address.get(Address.id==account["address"]).dict()

        return {'status':'success',
                'data':address }

@api.resource('/users/<int:id>/transactions/')
class UserTransactionViewSet(Resource):
    def __init__(self):
        self.requests = TransactionRequests()

    def get(self, id):
        to_user = []
        from_user = []
        for transaction in self.requests.transactions():
            if transaction["to_user"]==id:
                to_user.append(transaction)

            if transaction["from_user"]==id:
                from_user.append(transaction)

        return {'status':'success',
                'data':{'to_user':to_user,'from_user':from_user}}

@api.resource('/users/<int:id>/')
class UserItemViewSet(Resource):
    def get(self, id):
        return {'status':'success',
                'data':User.get(User.id==id).dict()}

    def put(self, id):
        return

@api.resource('/users/')
class UserViewSet(Resource):
    def __init__(self):
        self.requests = UserRequests()

    def get(self):
        return {'status':'success','data':self.requests.users()}

    def post(self):
        _phone_number = request.form['phone_number']
        _first_name = request.form['first_name']
        _middle_name = request.form['middle_name']
        _last_name = request.form['last_name']
        _date_of_birth = request.form['date_of_birth']
        return {'status':'success',
                'data': User.create(phone_number=_phone_number,
                           first_name=_first_name,
                           middle_name=_middle_name,
                           last_name=_last_name,
                           date_of_birth=_date_of_birth).dict()}

    def delete(self):
        return {'status':'success'}


@api.resource('/organizations/<int:id>/')
class OrganizationItemViewSet(Resource):
    def get(self, id):
        return {'status':'success',
                'data':Organization.get(Organization.id==id).dict()}

    def put(self, id):
        return

@api.resource('/organizations/')
class OrganizationViewSet(Resource):
    def __init__(self):
        self.requests = OrganizationRequests()

    def get(self):
        return {'status':'success','data':self.requests.organizations()}

    def post(self):
        _name = request.form['name']
        _image = request.form['image']
        return {'status':'success',
                'data':Organization.create(name=_name,
                                   image=_image).dict() }

    def delete(self):
        return {'status':'success'}

@api.resource('/addresses/<int:id>/')
class AddressItemViewSet(Resource):
    def get(self, id):
        return {'status':'success',
                'data':Address.get(Address.id==id).dict()}

    def put(self, id):
        return

@api.resource('/addresses/')
class AddressViewSet(Resource):
    def __init__(self):
        self.requests = AddressRequests()

    def get(self):
        return {'status':'success','data':self.requests.addresses()}

    def post(self):
        _line1 = request.form['line1']
        _line2 = request.form['line2']
        _city = request.form['city']
        _postal_code = request.form['postal_code']
        _state = request.form['state']
        _country = request.form['country']
        return {'status':'success',
                'data': Address.create(line1=_line1,
                              line2=_line2,
                              city=_city,
                              postal_code=_postal_code,
                              state=_state,
                              country=_country).dict() }

    def delete(self):
        return {'status':'success'}

@api.resource('/accounts/<int:id>/')
class AccountItemViewSet(Resource):
    def get(self, id):
        return {'status':'success',
                'data':Account.get(Account.id==id).dict()}

    def put(self, id):
        return

@api.resource('/accounts/')
class AccountViewSet(Resource):
    def __init__(self):
        self.requests = AccountRequests()

    def get(self):
        return {'status':'success','data':self.requests.accounts()}

    def post(self):
        _user = request.form['user']
        _organization = request.form['organization']
        _address = request.form['address']
        _debit_card = request.form['debit_card']
        _expiry_date = request.form['expiry_date']
        _cvc = request.form['cvc']
        _alias = request.form['alias']
        return {'status':'success',
                'data': Account.create(user=_user,
                              organization=_organization,
                              address=_address,
                              debit_card=_debit_card,
                              expiry_date=_expiry_date,
                              cvc=_cvc,
                              alias=_alias).dict() }

    def delete(self):
        return {'status':'success'}

@api.resource('/events/<int:id>/transactions/')
class EventTransactionViewSet(Resource):
    def __init__(self):
        self.requests = TransactionRequests()

    def get(self, id):
        return {'status':'success',
                'data':self.requests.transactions()}

@api.resource('/events/<int:id>/')
class EventItemViewSet(Resource):
    def get(self, id):
        return {'status':'success',
                'data':Event.get(Event.id==id).dict()}

    def put(self, id):
        event = Event.get(Event.id==id)
        _owner = request.form['owner']
        _organization = request.form['organization']
        _address = request.form['address']
        _name = request.form['name']
        _body = request.form['body']
        _time_begins = request.form['time_begins']
        _time_ends = request.form['time_ends']
        _amount_raised = request.form['amount_raised']
        _latitude = request.form['latitude']
        _longitude = request.form['longitude']
        event.owner=_owner
        event.organization=_organization
        event.address=_address
        event.name=_name
        event.body=_body
        event.time_begins=_time_begins
        event.time_ends=_time_ends
        event.amount_raised=_amount_raised
        event.latitude=_latitude
        event.longitude=_longitude
        event.amount_raised = _amount_raised
        return {'status':'success',
                'data': event.dict() }

@api.resource('/events/')
class EventViewSet(Resource):
    def __init__(self):
        self.requests = EventRequests()

    def get(self):
        return {'status':'success','data':self.requests.events()}

    def post(self):
        _owner = request.form['owner']
        _organization = request.form['organization']
        _address = request.form['address']
        _name = request.form['name']
        _body = request.form['body']
        _time_begins = request.form['time_begins']
        _time_ends = request.form['time_ends']
        _amount_raised = request.form['amount_raised']
        _latitude = request.form['latitude']
        _longitude = request.form['longitude']
        return {'status':'success',
                'data': Event.create(owner=_owner,
                            organization=_organization,
                            address=_address,
                            name=_name,
                            body=_body,
                            time_begins=_time_begins,
                            time_ends=_time_ends,
                            amount_raised=_amount_raised,
                            latitude=_latitude,
                            longitude=_longitude).dict() }

    def delete(self):
        return {'status':'success'}

@api.resource('/transactions/<int:id>/')
class TransactionItemViewSet(Resource):
    def get(self, id):
        return {'status':'success',
                'data':Transaction.get(Transaction.id==id).dict()}

    def put(self, id):
        return

@api.resource('/transactions/')
class TransactionViewSet(Resource):
    def __init__(self):
        self.requests = TransactionRequests()

    def get(self):
        return {'status':'success','data':self.requests.transactions()}

    def post(self):
        _to_user = request.form['to_user']
        _from_user = request.form['from_user']
        _event = request.form['event']
        _amount = request.form['amount']
        _timestamp = request.form['timestamp']
        _note = request.form['note']
        return {'status':'success',
                'data': Transaction.create(to_user=_to_user,
                                  from_user=_from_user,
                                  event=_event,
                                  amount=_amount,
                                  timestamp=_timestamp,
                                  note=_note).dict() }

    def delete(self):
        return {'status':'success'}

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.78')
