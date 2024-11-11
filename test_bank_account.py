import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    
    def test_create_account_with_initial_balance(self):
        account = BankAccount(100)
        self.assertEqual(account.get_balance(), 100)
    
    def test_deposit_funds(self):
        account = BankAccount(50)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 100)

    def test_withdraw_funds(self):
        account = BankAccount(100)
        account.withdraw(40)
        self.assertEqual(account.get_balance(), 60)

    def test_withdraw_more_than_balance(self):
        account = BankAccount(30)
        with self.assertRaises(ValueError):
            account.withdraw(50)
    
    def test_invalid_deposit(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.deposit(-20)
    
    def test_invalid_withdrawal(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.withdraw(-10)

if __name__ == '__main__':
    unittest.main()