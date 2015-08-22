from models import Address

class AddressRequests(object):

    def address_with_id(self, address_id):
        return Address.get(Address.id == address_id)

    def addresses(self):
        addresses = []
        for address in Address.select():
            addresses.append(address.dict())
        return addresses
