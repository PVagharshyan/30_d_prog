from abc import ABC, abstractmethod
from typing import List
from accounts import Account, IndividualAccount, BusinessAccount
from customers import Customer
from transactions import Transaction
from bank_system import BankSystem

def main():
    customer1 = Customer("Alice", "alice@example.com")
    individual_account1 = IndividualAccount("12345")
    individual_account2 = IndividualAccount("67890")

    customer2 = Customer("Bob", "bob@example.com")
    business_account1 = BusinessAccount("54321")

    bank_system = BankSystem()
    bank_system.manage_account(customer1, individual_account1)
    bank_system.manage_account(customer1, individual_account2)
    bank_system.manage_account(customer2, business_account1)

    bank_system.transfer_funds(individual_account1, individual_account2, 100.0)

if __name__ == "__main__":
    main()
