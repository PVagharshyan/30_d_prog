from validate_decorators import validate_non_empty_string, validate_email

class Customer:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    @validate_non_empty_string("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def get_accounts(self):
        return list(self.accounts.values())
