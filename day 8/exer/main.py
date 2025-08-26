
class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
        else:
            print("❌ Withdrawal denied.")

    def display_balance(self):
        print(f"💰 Balance for {self.account_holder}: ${self.__balance:.2f}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account({self.account_number}) - {self.account_holder}"

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.account_number == other.account_number
        return False


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.get_balance() - amount >= 100:
            super().withdraw(amount)
        else:
            print("❌ Cannot withdraw. Minimum balance of $100 must be maintained.")


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.overdraft_limit:
            super().withdraw(amount)
        else:
            print("❌ Overdraft limit exceeded.")


class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.__price = price
        self.quantity = quantity

    def apply_discount(self, percent):
        if 0 < percent <= 100:
            discount = self.__price * (percent / 100)
            self.__price -= discount

    def restock(self, amount):
        if amount > 0:
            self.quantity += amount

    def get_price(self):
        return self.__price

    def __add__(self, other):
        if isinstance(other, Product) and self.product_id == other.product_id:
            return Product(self.product_id, self.name, self.__price, self.quantity + other.quantity)
        else:
            raise ValueError("Cannot add different products.")

    def __call__(self):
        return f"📦 {self.name} (ID: {self.product_id}) - ${self.__price:.2f}, Qty: {self.quantity}"


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, file_size):
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size

    def apply_discount(self, percent):
        if percent > 20:
            percent = 20
        super().apply_discount(percent)


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight

    def apply_discount(self, percent):
        super().apply_discount(percent)
        if self.get_price() < 5:
            print("⚠️ Price cannot go below $5. Resetting to $5.")
            self._Product__price = 5  



class Person:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.__email = email

    def display_info(self):
        print(f"👤 {self.name} (ID: {self.id})")

    def get_email(self):
        return self.__email


class Student(Person):
    def __init__(self, id, name, email, major, gpa):
        super().__init__(id, name, email)
        self.major = major
        self.gpa = gpa
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.gpa < other.gpa
        return NotImplemented

    def __repr__(self):
        return f"Student({self.name}, GPA: {self.gpa})"


class Professor(Person):
    def __init__(self, id, name, email, department):
        super().__init__(id, name, email)
        self.department = department
        self.courses_teaching = []

    def add_course(self, course):
        self.courses_teaching.append(course)

    def __repr__(self):
        return f"Professor({self.name}, Dept: {self.department})"


def main():
    print("\n=== 💰 Banking System ===")
    acc1 = SavingsAccount("001", "Alice", 500, 0.02)
    acc2 = CheckingAccount("002", "Bob", 300, 200)

    acc1.withdraw(450)  
    acc2.withdraw(450)  

    acc1.deposit(100)
    acc1.display_balance()
    acc2.display_balance()

    print(acc1)
    print("Accounts equal?", acc1 == acc2)

    print("\n=== 🛒 Product System ===")
    dp = DigitalProduct("D101", "Ebook", 30, 100, "5MB")
    pp = PhysicalProduct("P202", "Notebook", 10, 50, "500g")

    dp.apply_discount(25)  
    pp.apply_discount(60)  

    print(dp())
    print(pp())

    combined = pp + PhysicalProduct("P202", "Notebook", 10, 20, "500g")
    print(combined())

    print("\n=== 🎓 University System ===")
    student1 = Student(1, "Charlie", "charlie@uni.edu", "CS", 3.8)
    student2 = Student(2, "Diana", "diana@uni.edu", "Math", 3.6)
    prof = Professor(100, "Dr. Smith", "smith@uni.edu", "Engineering")

    student1.enroll("Data Structures")
    prof.add_course("Machine Learning")

    student1.display_info()
    prof.display_info()

    print("Student 1 Email:", student1.get_email())
    print("Student Comparison (Charlie < Diana):", student1 < student2)

    print(repr(student1))
    print(repr(prof))



if __name__ == "__main__":
    main()
