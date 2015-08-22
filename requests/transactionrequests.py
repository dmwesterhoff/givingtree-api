from models import Transaction

class TransactionRequests(object):

    def transaction_with_id(self, transaction_id):
        return Transaction.get(Transaction.id == transaction_id)

    def transactions(self):
        transactions = []
        for transaction in Transaction.select():
            transactions.append(transaction.dict())
        return transactions
