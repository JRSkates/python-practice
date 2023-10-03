import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(1000)  # Initial balance of $1000
        
    def test_deposit(self):
        self.assertTrue(self.account.deposit(500))  # Deposit $500
        self.assertEqual(self.account.get_balance(), 1500)  # Balance should be $1500
        
    def test_withdraw(self):
        self.assertTrue(self.account.withdraw(300))  # Withdraw $300
        self.assertEqual(self.account.get_balance(), 700)  # Balance should be $700
        
    def test_overdraft(self):
        self.assertFalse(self.account.withdraw(1200))  # Attempt to withdraw more than balance, should fail
        self.assertEqual(self.account.get_balance(), 1000)  # Balance should remain $1000
        
    def test_interest_calculation(self):
        interest = self.account.calculate_interest(5)  # Calculate 5% interest on $1000
        self.assertEqual(interest, 50)  # Interest should be $50

if __name__ == "__main__":
    unittest.main()
