from models import Address

class AddressRequests(object):
  
  def address_with_id(self, address_id):
    return Address.get(Address.id == address_id)
