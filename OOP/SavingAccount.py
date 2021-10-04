class BankAccount:
    def __init__(self, acct_no, owner, balance=0):
        self._acct_no = acct_no
        self._owner  = owner
        self._balance = balance
    @property
    def acct_no(self):
        return self._acct_no

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,balance):
        if balance < 0:
            return "So du khong hop le"
        self._balance = balance

    def display(self):
        print(f'So tai khoan: {self.acct_no}\nSo du: {self.balance}')
        self._owner.get_info()

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            # self.set_balance(self.get_balance() - amount)
        else:
            return "So tien khong hop le"

    def deposit(self, amount):
        if amount < 0:
            return "So tien khong hop le"
        # self.set_balance(self.get_balance() + amount)
        self.balance = self.balance + amount
    
class SavingAccount(BankAccount):
    def __init__(self, monthly_interest_rate = 0.005):
        self._monthly_interest_rate = monthly_interest_rate

    @property
    def monthly_interest_rate(self):
        return self._monthly_interest_rate
        
    @monthly_interest_rate.setter
    def monthly_interest_rate(self,monthly_interest_rate):
        self._monthly_interest_rate = monthly_interest_rate
    
    def calculate_interest(self):
        calculate_interest1 = self.balance * self.monthly_interest_rate
        return calculate_interest1
class Customer ():
    def __init__(self, name, date_of_birth, email, phone):
        self._name = name
        self._date_of_birth = date_of_birth
        self._email = email
        self._phone = phone
    def get_info(self):
         print (f'tên khách hàng: {self._name}\nNgày sinh: {self._date_of_birth}\nEmail: {self._email}\nSo DT: {self._phone}')

# ka = BankAccount(9998777, "kimanh", 1000000)
# ka.display()
# ka.withdraw(10000)
# ka.deposit(1000000)
# ka.display()
cusA = Customer("Kim Anh","12/09/1993","kimanhpham1209@gmail.com","0348458715")
ka = BankAccount(9998777, cusA, 1000000)
ka.display()

