from typing import List, Union
from abc import ABC, abstractmethod
from bank import Bank, BankSystem
from accounts import Account, IndividualAccount, JointAccount
from transactions import Transaction
from customers import Customer

def main():
    bank = Bank()
    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")

    individual_account1 = IndividualAccount("123456", 1000, "Checking")
    joint_account1 = JointAccount("987654", 5000, "Savings")

    individual_account2 = IndividualAccount("654321", 1500, "Savings")
    joint_account2 = JointAccount("456789", 3000, "Checking")

    bank.manage_account(customer1, individual_account1)
    bank.manage_account(customer1, joint_account1)
    bank.manage_account(customer2, individual_account2)
    bank.manage_account(customer2, joint_account2)

    transaction1 = bank.transfer_funds(individual_account1, joint_account1, 300)
    transaction2 = bank.transfer_funds(joint_account2, individual_account2, 1000)

    print(f"Transaction History for {customer1.name}:")
    for account in customer1.accounts:
        print(f"Account Number: {account.account_number}")
        for transaction in bank.view_transaction_history(customer1, account):
            print(f"Transaction Type: {transaction.transaction_type}, Amount: {transaction.amount}")

    print(f"Transaction History for {customer2.name}:")
    for account in customer2.accounts:
        print(f"Account Number: {account.account_number}")
        for transaction in bank.view_transaction_history(customer2, account):
            print(f"Transaction Type: {transaction.transaction_type}, Amount: {transaction.amount}")

if __name__ == "__main__":
    main()
