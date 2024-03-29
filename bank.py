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
    
  def transfer(self, from_account, to_account, amount, account_type):
    if from_account in self.accounts and to_account in self.accounts and account_type in self.accounts[from_account]:
      if self.accounts[from_account][account_type] >= amount:
        self.accounts[from_account][account_type] -= amount
        self.accounts[to_account][account_type] += amount
        return True
      else:
        print("Insufficient funds")
        return False # Insufficient funds
    else:
      print("account or account type doesn't exist")
      return False # account or account type doesn't exist
    
  def check_balance(self, account_number, account_type):
    if account_number in self.accounts and account_type in self.accounts[account_number]:
      return self.accounts[account_number][account_type]
    return None # could be refactored
  
  def apply_interest(self, account_number, account_type, interest_rate):
    if account_number in self.accounts and account_type in self.accounts[account_number]:
      self.accounts[account_number][account_type] *= (1 + interest_rate)
      return True
    return False

  def close_account(self, account_number):
    if account_number in self.accounts:
      del self.accounts[account_number]
      return True
    return False

# More to add
# --------------
# =========================