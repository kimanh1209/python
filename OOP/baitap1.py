# Thay đổi các thuộc tính account_number, account_name, balance trong class BankAccount thành thuộc tính ẩn,
# và triển khai thêm các phương thức:

# get_account_number()
# get_account_name()
# get_balance()
# set_balance() - balance phải lớn hơn hoặc bằng 0
# Thay đổi các phương thức display(), withdraw() và deposit() sử dụng các phương thức getter và setter trên.

# Chú ý:

# Với withdraw(), amount phải lớn hơn 0 và nhỏ hơn balance
# Với deposit(), amount phải lớn hơn 0
# Nếu giá trị không phù hợp thì thông báo ra console

class BankAccount:
    def set_details(self, acct_no, acct_name, balance=0):
        self._acct_no = acct_no
        self._acct_name = acct_name
        self._balance = balance

    def get_account_number(self):
        return self._acct_no

    def get_account_name(self):
        return self._acct_name

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance < 0:
            return "So du khong hop le"
        self._balance = balance

    def display(self):
        print(
            f'So tai khoan: {self.get_account_number()}\nTen tai khoan: {self.get_account_name()}\nSo du: {self.get_balance()}\n')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
        else:
            return "So tien khong hop le"

    def deposit(self, amount):
        if amount < 0:
            return "So tien khong hop le"
        self.set_balance(self.get_balance() + amount)


ka = BankAccount()
ka.set_details(9998777, "kimanh", 1000000)
ka.display()
ka.withdraw(10000)
ka.deposit(1000000)
ka.display()
