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

