from abc import ABC, abstractmethod

# Pillar 1: Abstraction (The Payment "Contract") & Pillar 2: Inheritance
# ----------------------------------------------------------------------
class PaymentProcessor(ABC):
    """ABSTRACT BASE CLASS: Defines the contract for all payment methods."""
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    """A concrete class that inherits from the abstract one."""
    def pay(self, amount):
        print(f"Processing ${amount} payment via Credit Card...")
        # Add logic for credit card transaction
        return True

class UPIProcessor(PaymentProcessor):
    """Another concrete class for a different payment type."""
    def pay(self, amount):
        print(f"Processing ${amount} payment via UPI...")
        # Add logic for UPI transaction
        return True

# Pillar 2: Inheritance (Product Hierarchy) & Pillar 3: Encapsulation
# --------------------------------------------------------------------
class Product:
    """PARENT CLASS: A general product."""
    def __init__(self, name, price):
        self.name = name
        self.__price = price  # ENCAPSULATION: Price is private

    def get_price(self):
        """A 'getter' provides safe, read-only access."""
        return self.__price

    def set_price(self, new_price):
        """A 'setter' allows controlled modification."""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive.")

class Book(Product):
    """CHILD CLASS: Inherits from Product."""
    def __init__(self, name, price, author):
        super().__init__(name, price) # Call parent constructor
        self.author = author

class ElectronicDevice(Product):
    """CHILD CLASS: Inherits from Product."""
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

# Pillar 4: Classes/Objects and Pillar 5: Polymorphism
# -----------------------------------------------------
class Order:
    """This class brings everything together."""
    def __init__(self, user, cart, payment_processor):
        self.user = user
        self.cart = cart # A list of Product objects
        self.payment_processor = payment_processor # A PaymentProcessor object

    def calculate_total(self):
        return sum(item.get_price() for item in self.cart)

    def process_order(self):
        """POLYMORPHISM in action!"""
        total = self.calculate_total()
        print(f"Processing order for {self.user} with a total of ${total}.")
        
        # This one line works with ANY object that follows the PaymentProcessor contract.
        # It doesn't care if it's a CreditCardProcessor or UPIProcessor.
        self.payment_processor.pay(total)
        print("Order processed successfully!")

# --- Let's run the system! ---

# 1. Create some products (Objects)
book = Book("The Lord of the Rings", 25, "J.R.R. Tolkien")
laptop = ElectronicDevice("Dell XPS 15", 1500, "2 years")

# 2. Define the shopping cart and user
current_user = "John Doe"
shopping_cart = [book, laptop]

# 3. Choose a payment method
credit_card_payment = CreditCardProcessor()
upi_payment = UPIProcessor()

# 4. Create and process an order with a Credit Card
print("--- Scenario 1: Paying with Credit Card ---")
order1 = Order(current_user, shopping_cart, credit_card_payment)
order1.process_order()

print("\n" + "="*40 + "\n")

# 5. Create and process the same order with UPI
print("--- Scenario 2: Paying with UPI ---")
order2 = Order(current_user, shopping_cart, upi_payment)
order2.process_order()



# e commerce

from abc import ABC,abstractmethod

class payment_method(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class upi(payment_method):
    def pay(self, amount):
        print("payment in upi ", amount)
class credit(payment_method):
    def pay(self, amount):
        print("payment in credit ", amount)


class product:
    def __init__(self,name ,price):
        self.name = name
        self.__price = price
    def get_price(self):
        return self.__price
    def set_price(self,price):
        if price > 0:
            self.__price = price
        else:
            print("price must be positive")
class book(product):
    def __init__(self, name, price,author):
        super().__init__(name, price)
        self.author = author

class electronic(product):
    def __init__(self, name, price,warranty):
        super().__init__(name, price)
        self.warranty = warranty

class order:
    def __init__(self,name,cart,payment_method):
        self.name = name
        self.cart = cart
        self.payment_method = payment_method
    def calculate_total(self):
        return sum(item.get_price() for item in self.cart)
    def order_process(self):
        total = self.calculate_total()
        print(f"order for {self.name} with total ${total}")
        self.payment_method.pay(total)
        print("order processed successfully")
        
book = Book("The Lord of the Rings", 25, "J.R.R. Tolkien")
laptop = ElectronicDevice("Dell XPS 15", 1500, "2 years")

current_user = "hari"
shopping_cart = [book, laptop]

credit_card_payment = credit()
upi_payment = upi()

order1 = order(current_user,shopping_cart,credit_card_payment)
order1.order_process()
order2 = order(current_user,shopping_cart,upi_payment)
order2.order_process()

from abc import ABC, abstractmethod

# Pillar 1: Abstraction (The Transaction "Contract")
# ----------------------------------------------------
class Transaction(ABC):
    """ABSTRACT BASE CLASS: Defines the contract for all transactions."""
    @abstractmethod
    def execute(self, account, amount):
        pass

class WithdrawTransaction(Transaction):
    """A concrete class that inherits from the abstract one."""
    def execute(self, account, amount):
        return account.withdraw(amount)

class DepositTransaction(Transaction):
    """Another concrete class for a different transaction type."""
    def execute(self, account, amount):
        return account.deposit(amount)

# Pillar 2: Inheritance (Account Hierarchy) & Pillar 3: Encapsulation
# ----------------------------------------------------------------------
class Account:
    """PARENT CLASS: A general bank account."""
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance  # ENCAPSULATION: Balance is private

    def get_balance(self):
        """A 'getter' to safely view the balance."""
        print(f"Current balance for {self.account_number}: ${self.__balance}")
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}.")
            return True
        else:
            print("Deposit amount must be positive.")
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}.")
            return True
        else:
            print("Invalid withdrawal amount or insufficient funds.")
            return False

class SavingsAccount(Account):
    """CHILD CLASS: Inherits from Account and adds new features."""
    def __init__(self, account_number, owner, balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._Account__balance * self.interest_rate # Accessing private var correctly
        print(f"Applying {self.interest_rate*100}% interest...")
        self.deposit(interest)


# Pillar 4: Classes/Objects and Pillar 5: Polymorphism
# --------------------------------------------------------
class ATM:
    """This class brings everything together to perform operations."""
    def execute_transaction(self, account, transaction, amount):
        """POLYMORPHISM in action!"""
        print(f"\n--- ATM executing a {transaction.__class__.__name__} ---")
        # This one line works with ANY object that follows the Transaction contract.
        transaction.execute(account, amount)
        account.get_balance()


# --- Let's run the ATM simulation! ---

# 1. Create a specific type of account (Object)
my_savings_account = SavingsAccount("SA-12345", "Jane Doe", 1000)
my_savings_account.get_balance()

# 2. Create transaction types (Objects)
deposit = DepositTransaction()
withdraw = WithdrawTransaction()

# 3. Create an ATM object
local_atm = ATM()

# 4. Use the ATM to perform different transactions on the same account
local_atm.execute_transaction(my_savings_account, deposit, 500)
local_atm.execute_transaction(my_savings_account, withdraw, 200)
local_atm.execute_transaction(my_savings_account, withdraw, 2000) # This one should fail

# 5. Use a specialized method from the child class
print("\n--- Applying interest ---")
my_savings_account.apply_interest()



from abc import ABC, abstractmethod

# Pillar 1: Abstraction & Pillar 2: Inheritance
# -----------------------------------------------
class LibraryItem(ABC):
    """ABSTRACT BASE CLASS: The contract for any item in the library."""
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self._is_checked_out = False  # ENCAPSULATION: Protected status

    @abstractmethod
    def display(self):
        """An abstract method that subclasses must implement."""
        pass

    def check_out(self):
        self._is_checked_out = True

    def return_item(self):
        self._is_checked_out = False

class Book(LibraryItem):
    """CHILD CLASS: Inherits from LibraryItem."""
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display(self):
        status = "Checked Out" if self._is_checked_out else "Available"
        print(f"Book: '{self.title}' by {self.author} (ID: {self.item_id}) - Status: {status}")

class DVD(LibraryItem):
    """CHILD CLASS: Inherits from LibraryItem."""
    def __init__(self, title, item_id, director):
        super().__init__(title, item_id)
        self.director = director

    def display(self):
        status = "Checked Out" if self._is_checked_out else "Available"
        print(f"DVD: '{self.title}' directed by {self.director} (ID: {self.item_id}) - Status: {status}")

# Pillar 3: Encapsulation
# -------------------------
class Member:
    """Manages member information and their borrowed items."""
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self._borrowed_items = []  # ENCAPSULATION: Private list of borrowed items

    def borrow_item(self, item):
        self._borrowed_items.append(item)
        print(f"Member '{self.name}' borrowed '{item.title}'.")

    def return_item(self, item):
        self._borrowed_items.remove(item)
        print(f"Member '{self.name}' returned '{item.title}'.")

    def list_borrowed(self):
        print(f"\nItems borrowed by {self.name}:")
        if not self._borrowed_items:
            print("  None")
        for item in self._borrowed_items:
            print(f"  - {item.title}")

# Pillar 4: Classes/Objects & Pillar 5: Polymorphism
# ----------------------------------------------------
class Library:
    """The main class that orchestrates the system."""
    def __init__(self):
        self._catalog = {}
        self._members = {}

    def add_item(self, item):
        self._catalog[item.item_id] = item
        print(f"Added '{item.title}' to the catalog.")

    def register_member(self, member):
        self._members[member.member_id] = member
        print(f"Registered member '{member.name}'.")

    def lend_item(self, item_id, member_id):
        item = self._catalog.get(item_id)
        member = self._members.get(member_id)

        if item and member and not item._is_checked_out:
            item.check_out()
            member.borrow_item(item)
        else:
            print(f"Error: Cannot lend item {item_id}.")

    def display_catalog(self):
        """POLYMORPHISM in action!"""
        print("\n--- Library Catalog ---")
        # This loop calls the .display() method on each item.
        # It works seamlessly for both Book and DVD objects.
        for item_id in self._catalog:
            self._catalog[item_id].display()
        print("---------------------\n")


# --- Let's run the library simulation! ---

# 1. Create a Library
my_library = Library()

# 2. Add different types of items (Books and DVDs) to the catalog
book1 = Book("The Hobbit", "B001", "J.R.R. Tolkien")
dvd1 = DVD("The Matrix", "D001", "Wachowskis")
my_library.add_item(book1)
my_library.add_item(dvd1)

# 3. Register members
member1 = Member("Alice", "M01")
my_library.register_member(member1)

# 4. Display the catalog (shows polymorphism)
my_library.display_catalog()

# 5. Perform transactions
my_library.lend_item("B001", "M01") # Alice borrows The Hobbit
member1.list_borrowed()

# 6. Display the catalog again to see the updated status
my_library.display_catalog()