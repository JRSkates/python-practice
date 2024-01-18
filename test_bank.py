from bank import Bank

def test_create_account():
    bank = Bank()
    assert bank.create_account("12345")
    assert "12345" in bank.accounts
    assert bank.create_account("12345") == False  # Account already exists

def test_deposit():
    bank = Bank()
    bank.create_account("54321")
    assert bank.deposit("54321", "checking", 100)
    assert bank.accounts["54321"]["checking"] == 100
    assert bank.deposit("54321", "savings", 50)
    assert bank.accounts["54321"]["savings"] == 50
    assert bank.deposit("54321", "invalid_account", 20) == False  # Invalid account type

def test_withdraw():
    bank = Bank()
    bank.create_account("98765", initial_balance=200)
    assert bank.withdraw("98765", "checking", 50)
    assert bank.accounts["98765"]["checking"] == 150
    assert bank.withdraw("98765", "savings", 250) == False  # Insufficient funds
    assert bank.withdraw("12345", "checking", 30) == False  # Account doesn't exist

def test_transfer():
    bank = Bank()
    bank.create_account("11111", initial_balance=300)
    bank.create_account("22222")
    assert bank.transfer("11111", "22222", 100, "checking")
    assert bank.accounts["11111"]["checking"] == 200
    assert bank.accounts["22222"]["checking"] == 100
    assert bank.transfer("11111", "22222", 250, "savings") == False  # Insufficient funds
    assert bank.transfer("11111", "33333", 50, "checking") == False  # To account doesn't exist

def test_check_balance():
    bank = Bank()
    bank.create_account("44444", initial_balance=500)
    assert bank.check_balance("44444", "checking") == 500
    assert bank.check_balance("44444", "savings") == 0
    assert bank.check_balance("54444", "checking") == None

def test_apply_interest():
    bank = Bank()
    bank.create_account("66666", initial_balance=1000)
    bank.apply_interest("66666", "checking", 0.05) # 5% interest applied
    bank.check_balance("66666", "checking") == 1050