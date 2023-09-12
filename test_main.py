from main import wallet

balance = wallet()

#here we made 3 different test cases
def addBalance():
    balance.addBalance(100)
    assert balance.addBalance()==100

def removeBalance():
    balance.removeBalance(100)
    assert balance.removeBalance()==0

def checkBalance():
    assert balance.getBalance() == 0 


#after making test cases, we need to push to GitHub
