class Account:
    def __init__(self,owner, balance=0):
        self.owner = owner
        self.balance = balance

    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount <= 0:
            print("ยอดฝากต้องมากกว่า 0")
            return
        self._balance += amount
        print(f"ฝาก {amount} เสร็จสิ้น ")
    
    def withdraw(self,amount):
        if amount <=0:
            print("ยอดถอนต้องมากกว่า 0")
            return
        if amount> self.balance:
            print("ยอดผิดพลาด")
            return
        self.balance -=amount
        print(f"ถอน {amount} เสร็จสิ้น")

class SavingsAccount(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print("เพิ่มดอกเบี้ยทบ")

if __name__ == "_main_":
    Account = SavingsAccount("Hikari", 1000)

    Account.deposit(500)
    Account.withdraw(300)
    Account.apply_interest()

    print("Final Balance:", Account.get_balance())


       