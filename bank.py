class Bank:
  def __init__(self):
    self.accounts = {}

  def create_account(self, account_number, initial_balance=0):
    if account_number not in self.accounts:
      self.accounts[account_number] = {"checking": initial_balance, "savings": 0}
      return True
    else:
      print("Account already exists: %s", account_number)
      return False # account already exists
    
  def deposit(self, account_number, account_type, amount):
    if account_number in self.accounts and account_type in self.accounts[account_number]:
      self.accounts[account_number][account_type] += amount
      return True
    else:
      print("account or account type doesn't exist")
      return False # account or account type doesn't exist
    
  def withdraw(self, account_number, account_type, amount):
    if account_number in self.accounts and account_type in self.accounts[account_number]:
      if self.accounts[account_number][account_type] >= amount:
        self.accounts[account_number][account_type] -= amount
        return True
      else:
        print("Insufficient funds")
        return False # Insufficient funds
    else:
      print("account or account type doesn't exist")
      return False # account or account type doesn't exist