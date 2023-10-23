from main import Wallet

balance = Wallet()

def test_add_balance():  # Function names should start with 'test_'
    balance.add_balance(100)
    assert balance.get_balance() == 100

def test_remove_balance():  # Function names should start with 'test_'
    balance.remove_balance(100)
    assert balance.get_balance() == 0

def test_check_balance():  # Function names should start with 'test_'
    assert balance.get_balance() == 0
