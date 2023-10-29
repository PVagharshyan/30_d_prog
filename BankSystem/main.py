from account import BasicAccount
from customer import Customer
from transactions import DepositTransaction, WithdrawTransaction, TransferTransaction

if __name__ == '__main__':
    try:
        bob = Customer("Bob", "bob@email.com")
        account1 = BasicAccount("12345", 1000, "Checking")
        account2 = BasicAccount("67890", 2000, "Savings")

        bob.add_account(account1)
        bob.add_account(account2)

        deposit = DepositTransaction(account1, 500)
        deposit.execute()

        withdraw = WithdrawTransaction(account2, 1500)
        withdraw.execute()

        transfer = TransferTransaction(account1, account2, 200)
        transfer.execute()

        for account in bob.get_accounts():
            print(f"Account Number: {account.account_number}, Balance: {account.balance}, Transactions: {len(account.get_transaction_history())}")

    except ValueError as e:
        print(e)

