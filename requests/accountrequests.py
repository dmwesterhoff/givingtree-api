from models import Account

class AccountRequests(object):

    def account_with_id(self, account_id):
        return Account.get(Account.id == account_id)

    def accounts(self):
        accounts = []
        for account in Account.select():
            accounts.append(account.dict())
        return accounts
