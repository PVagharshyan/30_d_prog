import utility

class Account:
    ...

class Transaction:
    def __init__(self, account: 'Account', amount: float, transaction_type: str):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    @property
    def account(self) -> 'Account':
        return self._account

    @account.setter
    @utility.type_checking(Account)
    def account(self, value: 'Account'):
        if not isinstance(value, Account):
            raise ValueError("Account must be an instance of the Account class")
        self._account = value

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    @utility.type_checking((float, int))
    def amount(self, value: float):
        if not isinstance(value, (float, int)):
            raise ValueError("Amount must be a float or int")
        self._amount = float(value)

    @property
    def transaction_type(self) -> str:
        return self._transaction_type

    @transaction_type.setter
    @utility.type_checking(str)
    def transaction_type(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Transaction type must be a string")
        self._transaction_type = value
