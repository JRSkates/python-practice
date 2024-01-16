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