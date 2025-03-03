class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print("Rs.", amount ,"is debited from", self.account_no)
            print("Current balance is", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount ,"is credited into", self.account_no)
        print("Current balance is", self.get_balance())

    def get_balance(self):
        return self.balance

obj = Account(12000, "UBI12344567")
obj.debit(1000)
obj.credit(21050)
obj.debit(1000)