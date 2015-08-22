from models import Transaction

class TransactionRequests(object):
  
    def transaction_with_id(self, transaction_id):
        return Transaction.get(Transaction.id == transaction_id)
