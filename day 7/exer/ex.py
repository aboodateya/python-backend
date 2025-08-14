class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."



class Dog:
    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def describe(self):
        return f"{self.name} is a {self.breed}. Species: {self.species}."



class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("❌ Insufficient funds.")
        else:
            print("❌ Withdraw amount must be positive.")

    def get_balance(self):
        return self.balance


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Added: {book.title}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"✅ Removed: {book.title}")
                return
        print("❌ Book not found.")

    def list_books(self):
        if not self.books:
            print("📚 No books in the library.")
        for book in self.books:
            print(book.display_info())


class Car:
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1

    def display_car(self):
        return f"{self.make} {self.model}"

    @staticmethod
    def get_total_cars():
        return Car.total_cars



class Student:
    school_name = "Green Valley High School"

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, score):
        if 0 <= score <= 100:
            self.grades.append(score)
        else:
            print("❌ Invalid score. Must be between 0 and 100.")

    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def student_info(self):
        avg = self.average_grade()
        return f"{self.name}, School: {Student.school_name}, Average Grade: {avg:.2f}"



class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        return f"{self.name} (${self.price:.2f}) - {self.category}"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"✅ Added: {item.name}")

    def remove_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"✅ Removed: {item.name}")
                return
        print("❌ Item not found in order.")

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def display_order(self):
        if not self.items:
            print("🛒 Your order is empty.")
            return
        print("🧾 Order summary:")
        for item in self.items:
            print(item.display())
        print(f"Total: ${self.calculate_total():.2f}")



def main():
    print("----- Exercise 1: Person -----")
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)
    print(person1.introduce())
    print(person2.introduce())

    print("\n----- Exercise 2: Dog -----")
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Max", "Bulldog")
    print(dog1.describe())
    print(dog2.describe())
    dog1.species = "Wolf"
    print("After changing dog1's species:")
    print(dog1.describe())
    print(dog2.describe())

    print("\n----- Exercise 3: BankAccount -----")
    acc = BankAccount("John Doe")
    acc.deposit(500)
    acc.withdraw(200)
    print(f"Balance: ${acc.get_balance()}")
    acc.withdraw(500)  
    acc.deposit(-100)  

    print("\n----- Exercise 4: Library -----")
    lib = Library()
    b1 = Book("1984", "George Orwell", "001")
    b2 = Book("Dune", "Frank Herbert", "002")
    lib.add_book(b1)
    lib.add_book(b2)
    lib.list_books()
    lib.remove_book("001")
    lib.list_books()

    print("\n----- Exercise 5: Car Counter -----")
    car1 = Car("Toyota", "Camry")
    car2 = Car("Honda", "Civic")
    print(car1.display_car())
    print(car2.display_car())
    print(f"Total cars: {Car.get_total_cars()}")

    print("\n----- Exercise 6: Student -----")
    student = Student("Lily")
    student.add_grade(85)
    student.add_grade(92)
    student.add_grade(78)
    student.add_grade(105)  
    print(student.student_info())

    print("\n----- Exercise 7: Restaurant Order -----")
    item1 = MenuItem("Burger", 10.99, "Main")
    item2 = MenuItem("Fries", 3.50, "Side")
    item3 = MenuItem("Coke", 1.99, "Drink")

    order = Order()
    order.add_item(item1)
    order.add_item(item2)
    order.add_item(item3)
    order.display_order()
    order.remove_item("Fries")
    order.display_order()



if __name__ == "__main__":
    main()
