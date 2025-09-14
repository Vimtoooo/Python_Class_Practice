class Bank:

    bank_name: str = "Python Bank"

    def __init__(self, name: str, age: int):
        self._name = name
        self._age: int = age
        self._balance: float = 0

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def age(self) -> int:
        return self._age

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def deposit(self):
        while True:
            try:
                value: float = float(input("Enter a value to deposit:\n"))

                if not value:
                    choice2: str = input("Are you sure about not making any transactions?\n")

                    if 'y' in choice2.lower():
                        break

                elif value > 0:
                    self._balance += value
                    print("Transaction complete.")
                
                else:
                    raise ValueError
            
            except TypeError as a:
                print(f"Error: {a}")
            
            except ValueError:
                print(f"Error: {ValueError}")

            except Exception as e:
                print(f"Error: {e}")

            finally:
                choice: str = input("Would you like to deposit more cash?\n")
                
                if 'n' in choice.lower():
                    break
    
    # @name.setter
    # @age.setter
    # def change_data(self):
    #     print("Please select a data to alter:")
    #     while True:
    #         choice: str = input("1 - Change your Name\n2 - Change your age\n")
    #         if n

# my_account = Bank("Vito", 18)
# my_account.deposit




class User:
    def __init__(self, password):
        # TODO: Store the password as a private attribute using double underscore (__)
        #       This makes it harder to access from outside the class
        self.__password = password
    
    def check_password(self, input_password):
        # TODO: Return True if input_password matches the stored private password
        #       Return False otherwise
        if input_password == self.__password:
            return True
        else:
            return False
    
    def change_password(self, old_password, new_password):
        # TODO: Check if old_password is correct using the check_password method
        # TODO: If old_password is correct, update the private password to new_password and return True
        # TODO: If old_password is incorrect, return False without changing the password
        if self.check_password(old_password):
            self.__password = new_password
            return True
        else:
            return False



# TODO: Import the User class from the user module

# TODO: Get test case from input
# test_case = input()

# if test_case == "constructor_test":
#     # TODO: Create a User object with initial password "secure123"
#     user = User("secure123")
#     print("User created successfully")
#     print("Initial password set")

# elif test_case == "correct_password_test":
#     # TODO: Create a User object with initial password "secure123"
#     user = User("secure123")
#     # TODO: Test the check_password method with correct password
#     #       Print "Password check successful!" if it returns True
#     #       Print "Password check failed!" if it returns False
#     result = user.check_password("secure123")
#     if result:
#         print("Password check successful!")
#     else:
#         print("Password check failed!")

# elif test_case == "incorrect_password_test":
#     # TODO: Create a User object with initial password "secure123"
#     user = User("secure123")
#     # TODO: Test the check_password method with incorrect password "wrong"
#     #       Print "Incorrect password rejected!" if it returns False
#     #       Print "Security issue: incorrect password accepted!" if it returns True
#     result = user.check_password("wrong")
#     if not result:
#         print("Incorrect password rejected!")
#     else:
#         print("Security issue: incorrect password accepted!")

# elif test_case == "change_password_test":
#     # TODO: Create a User object with initial password "secure123"
#     user = User("secure123")
#     # TODO: Test changing password from "secure123" to "newpass456"
#     #       Print "Password changed successfully!" if it returns True
#     #       Print "Password change failed!" if it returns False
#     result = user.change_password("secure123", "newpass456")
#     if result:
#         print("Password changed successfully!")
#     else:
#         print("Password change failed!")
    
#     # TODO: Verify the new password works by checking "newpass456"
#     #       Print "New password works!" if it returns True
#     #       Print "New password doesn't work!" if it returns False
#     if user.check_password("newpass456"):
#         print("New password works!")
#     else:
#         print("New password doesn't work!")

# elif test_case == "change_password_wrong_old_test":
#     # TODO: Create a User object with initial password "secure123"
#     user = User("secure123")
#     # TODO: Try changing password with incorrect old password
#     #       Print "Security working: incorrect old password rejected!" if it returns False
#     #       Print "Security issue: password changed with wrong old password!" if it returns True
#     result = user.change_password("wrong", "hackerpw")
#     if not result:
#         print("Security working: incorrect old password rejected!")
#     else:
#         print("Security issue: password changed with wrong old password!")

# elif test_case == "comprehensive_test":
#     # TODO: Create a User object with initial password "secure123"
#     user = User("secure123")
#     print("User created with initial password")
    
#     # TODO: Test the check_password method with correct password
#     if user.check_password("secure123"):
#         print("Initial password verification successful")
    
#     # TODO: Test the check_password method with incorrect password
#     if not user.check_password("wrongpass"):
#         print("Incorrect password properly rejected")
    
#     # TODO: Test changing password from "secure123" to "newpass456"
#     if user.change_password("secure123", "newpass456"):
#         print("Password successfully changed")
    
#     # TODO: Verify old password no longer works
#     if not user.check_password("secure123"):
#         print("Old password no longer works")
    
#     # TODO: Verify the new password works
#     if user.check_password("newpass456"):
#         print("New password works correctly")
    
#     # TODO: Try changing password with incorrect old password
#     if not user.change_password("wrongold", "hackerpw"):
#         print("Security maintained: wrong old password rejected")
    
#     # TODO: Verify password is still secure after failed change attempt
#     if user.check_password("newpass456"):
#         print("Password remains secure after failed change attempt")

# else:
#     print("Unknown test case")

class BankAccount:
    # TODO: Define class variable for interest rate (2% = 0.02)
    interest_rate = 0.02
    
    def __init__(self, owner_name: str, initial_balance: float):
        """Initialize a new bank account.
        
        Args:
            owner_name (str): Name of the account owner
            initial_balance (float): Starting balance for the account
        
        TODO:
        - Store owner_name as private attribute (__owner_name)
        - Validate that initial_balance is not negative
        - If negative, raise ValueError with message "Initial balance cannot be negative"
        - Store initial_balance as private attribute (__balance)
        """
        self.__owner_name = owner_name
        if initial_balance < 0:
            print("Initial balance cannot be negative")
        else:
            self.__balance = initial_balance
    
    @property
    def owner_name(self) -> str:
        """Get the account owner's name.
        
        TODO: Return the private __owner_name attribute
        """
        return self.__owner_name
    
    @property
    def balance(self) -> float:
        """Get the current account balance.
        
        TODO: Return the private __balance attribute
        """
        return self.__balance
    
    @balance.setter
    def balance(self, value: float) -> bool:
        """Set the account balance with validation.
        
        Args:
            value (float): New balance value
        
        TODO:
        - Check if value is negative
        - If negative, print exactly: "Balance cannot be negative"
        - If negative, return without setting the balance
        - Otherwise, set __balance to the new value
        """
        if value <= 0:
            print("Balance cannot be negative")
            return False
        else:
            self.__balance = value   # For validation purposes
            return True
    
    def deposit(self, amount: float) -> bool:
        """Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            bool: True if successful, False if failed
        
        TODO:
        - Check if amount is <= 0
        - If invalid, print exactly: "Deposit amount must be positive"
        - If invalid, return False
        - Otherwise, add amount to __balance and return True
        """
        if amount > 0:
            self.__balance += amount
            return True
        else:
            print("Deposit amount must be positive")
            return False
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if successful, False if failed
        
        TODO:
        - Check if amount is <= 0
        - If invalid, print exactly: "Withdrawal amount must be positive"
        - If invalid, return False
        - Check if amount > current balance
        - If insufficient funds, print exactly: "Insufficient funds"
        - If insufficient funds, return False
        - Otherwise, subtract amount from __balance and return True
        """
        if amount > 0:
            if self.__balance < amount:
                print("Insufficient funds")
                return False
            else:
                self.__balance -= amount
                return True
        else:
            print("Withdrawal amount must be positive")
            return False
    
    def apply_interest(self) -> float:
        """Apply interest to the current balance.
        
        Returns:
            float: The interest amount that was added
        
        TODO:
        - Calculate interest: __balance * interest_rate
        - Add the interest to __balance
        - Return the interest amount
        """
        interest_amount: float = self.__balance * self.interest_rate
        self.__balance += interest_amount
        return interest_amount
    
    def display_info(self):
        """Display account information.
        
        TODO: Print the following format exactly:
        Account Owner: {owner_name}
        Balance: ${balance}
        Interest Rate: {interest_rate_as_percentage}%
        
        Example output:
        Account Owner: John Doe
        Balance: $1000.0
        Interest Rate: 2.0%
        """
        print(f"Account Owner: {self.__owner_name}\nBalance: ${self.__balance}\nInterest Rate: {self.interest_rate * 100}%")


# Test case handler
# test_case = input()

# if test_case == "account_creation":
#     # Test account creation
#     account = BankAccount("Alice", 1000)
#     print(f"Owner: {account.owner_name}")
#     print(f"Initial balance: ${account.balance}")
#     print(f"Interest rate: {BankAccount.interest_rate * 100}%")

# elif test_case == "deposit_method":
#     # Test deposit functionality
#     account = BankAccount("Bob", 500)
#     print(f"Initial balance: ${account.balance}")
    
#     # Valid deposit
#     result = account.deposit(300)
#     print(f"Deposit result: {result}")
#     print(f"New balance: ${account.balance}")
    
#     # Invalid deposit
#     result = account.deposit(-50)
#     print(f"Negative deposit result: {result}")
#     print(f"Balance after invalid deposit: ${account.balance}")

# elif test_case == "withdraw_method":
#     # Test withdraw functionality
#     account = BankAccount("Charlie", 1000)
    
#     # Valid withdrawal
#     result = account.withdraw(400)
#     print(f"Withdrawal result: {result}")
#     print(f"Balance after withdrawal: ${account.balance}")
    
#     # Invalid withdrawal (negative)
#     result = account.withdraw(-50)
#     print(f"Negative withdrawal result: {result}")
    
#     # Invalid withdrawal (exceeds balance)
#     result = account.withdraw(1000)
#     print(f"Excessive withdrawal result: {result}")
#     print(f"Final balance: ${account.balance}")

# elif test_case == "property_access":
#     # Test property access and protection
#     account = BankAccount("Dave", 800)
    
#     print(f"Owner via property: {account.owner_name}")
#     print(f"Balance via property: ${account.balance}")
    
#     # Try to set balance (should use the setter)
#     account.balance = 1200
#     print(f"Balance after valid setter: ${account.balance}")
    
#     # Try invalid balance
#     account.balance = -500
#     print(f"Balance after invalid setter: ${account.balance}")
    
#     # Try to access private attributes directly (should fail)
#     try:
#         print(account.__owner_name)
#     except AttributeError:
#         print("Cannot access private owner_name directly")

# elif test_case == "apply_interest":
#     # Test interest application
#     account = BankAccount("Eve", 2000)
    
#     # Check original balance
#     print(f"Initial balance: ${account.balance}")
    
#     # Apply interest
#     interest_earned = account.apply_interest()
#     expected_interest = 2000 * 0.02
    
#     print(f"Interest earned: ${interest_earned}")
#     print(f"New balance after interest: ${account.balance}")
#     print(f"Interest calculation correct: {interest_earned == expected_interest}")

# elif test_case == "display_info":
#     # Test display_info method format
#     account = BankAccount("Frank", 1500)
    
#     # Modify interest rate to test class variable
#     original_rate = BankAccount.interest_rate
#     BankAccount.interest_rate = 0.03
    
#     print("Display info output:")
#     account.display_info()
    
#     # Restore original rate
#     BankAccount.interest_rate = original_rate

# elif test_case == "original_test_case":
#     # Run the original test code from the challenge
#     account = BankAccount("Coddy", 1000)

#     # Perform operations
#     account.deposit(500)
#     account.withdraw(200)
#     account.apply_interest()

#     # Display account information
#     account.display_info()

#     # Test setter validation
#     account.balance = 5000
#     print(f"Balance after setter: ${account.balance}")

#     # Test withdrawal validation
#     account.withdraw(10000)
#     print(f"Final balance: ${account.balance}")


# class Person:
#     def __init__(self, salary):
#         self.__salary = salary  # private

#     def get_salary(self):
#         return self.__salary

# p = Person(5000)
# # print(p.__salary)  # AttributeError
# print(p._Person__salary)  # Accessible, but discouraged
# print(p.get_salary())

# class Person:
#     def __init__(self, name, age):
#         self._age = age  # protected
    
#     # def get_age(self):
#     #     return self._age

# class Student(Person):
#     def get_age(self):
#         return self._age  # Accessible in subclass


class BankAccount:
    def __init__(self, owner, balance, account_id):
        self.owner = owner           # Public - accessible anywhere
        self._balance = balance      # Protected - internal use
        self.__account_id = account_id  # Private - class only
    
    def deposit(self, amount):       # Public method
        self._balance += amount
    
    def _calculate_interest(self):   # Protected method
        return self._balance * 0.02
    
    def __validate_transaction(self, amount):  # Private method
        return amount > 0 and amount <= self._balance

class SavingsAccount(BankAccount):
    def show_balance(self):
        return self._balance        # Protected - accessible in subclass
    
    def show_id(self):
        # return self.__account_id  # This won't work - private attributes can only be returned within the origin class (where it was created)
        return "Cannot access private member"

# s = Student("Bob", 20)
# print(s._age) 
# print(s.get_age())

# savings = SavingsAccount("Bob", 2000, "67890")
# print(savings.show_balance())  # 2000
# print(savings.show_id())       # Cannot access private member


# Public, Protected and Private members (encapsulation)
class BankAccount:
    def __init__(self, account_holder, account_number):
        # TODO: Initialize the public attribute 'account_holder' with the provided parameter
        self.account_holder = account_holder
        # TODO: Initialize the protected attribute '_transaction_count' to 0
        self._transaction_count = 0
        # TODO: Initialize the private attribute '__balance' to 0
        # NOTE: Private attributes use double underscore prefix
        self.__balance = 0
        # TODO: Initialize the private attribute '__account_number' with the provided parameter
        self.__account_number = account_number
    
    # Public methods
    def deposit(self, amount):
        # TODO: Check if amount is greater than 0
        if amount > 0:
        # TODO: If valid, add amount to the private __balance attribute
            self.__balance += amount
        # TODO: Call the protected _update_transaction_count() method
            self._update_transaction_count()
        # TODO: Return the new balance
            return self.__balance
        # TODO: If amount is not valid, return None
        else:
            return None
    
    def get_balance(self):
        # TODO: Return the current value of the private __balance attribute
        return self.__balance
    
    # Protected method
    def _update_transaction_count(self):
        # TODO: Increment the protected _transaction_count attribute by 1
        self._transaction_count += 1


# Comprehensive test case handler
# test_case = input()

# if test_case == "basic_test":
#     # Basic functionality test
#     account = BankAccount("John Doe", "12345")
#     print(account.account_holder)  # Public attribute
#     print(account.deposit(100))    # Public method
#     print(account.get_balance())   # Public method

# elif test_case == "transaction_count":
#     # Testing protected attribute
#     account = BankAccount("Jane Smith", "67890")
#     account.deposit(50)
#     account.deposit(100)
#     account.deposit(200)
#     print(account._transaction_count)  # Protected attribute
#     print(account.get_balance())

# elif test_case == "invalid_deposit":
#     # Testing validation in deposit method
#     account = BankAccount("Bob Johnson", "54321")
#     print(account.deposit(-50))  # Should return None
#     print(account.deposit(0))    # Should return None
#     print(account.deposit(75))   # Should return 75
#     print(account.get_balance())

# elif test_case == "private_access":
#     # Testing private attribute access
#     account = BankAccount("Alice Brown", "98765")
#     try:
#         print(account.__balance)  # This will raise an AttributeError
#     except AttributeError:
#         pass
    
#     try:
#         print(account.__account_number)  # This will raise an AttributeError
#     except AttributeError:
#         pass
    
#     print("Private attributes are not directly accessible")
#     account.deposit(500)
#     print(account.get_balance())  # Access through public method

# elif test_case == "name_mangling":
#     # Demonstrating name mangling for private attributes
#     account = BankAccount("Charlie Green", "13579")
#     print(account._BankAccount__balance)        # Accessing private attribute through name mangling
#     print(account._BankAccount__account_number)  # Accessing private attribute through name mangling
#     account.deposit(300)
#     print(account._BankAccount__balance)  # Should show updated balance

# elif test_case == "multiple_accounts":
#     # Testing multiple accounts
#     account1 = BankAccount("David White", "24680")
#     account2 = BankAccount("Eva Black", "86420")
#     account3 = BankAccount("Frank Red", "97531")
    
#     account1.deposit(150)
#     account2.deposit(250)
#     account2.deposit(50)
#     account3.deposit(500)
#     account3.deposit(300)
#     account3.deposit(200)
    
#     print(f"{account1.account_holder}: {account1.get_balance()}")
#     print(f"{account2.account_holder}: {account2.get_balance()}")
#     print(f"{account3.account_holder}: {account3.get_balance()}")
    
#     print(f"Account 1 transactions: {account1._transaction_count}")
#     print(f"Account 2 transactions: {account2._transaction_count}")
#     print(f"Account 3 transactions: {account3._transaction_count}")

# elif test_case == "stress_test":
#     # Performance test with many transactions
#     account = BankAccount("Stress Tester", "11111")
#     for _ in range(1000):
#         account.deposit(1)
#     print(f"Final balance: {account.get_balance()}")
#     print(f"Transaction count: {account._transaction_count}")


class Rectangle:
    def __init__(self, width, height):
        self._width = 0
        self._height = 0
        self.width = width  # Use setter for validation
        self.height = height  # Use setter for validation
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    @property
    def dimensions(self):
        return (self.width, self.height)
    
    @dimensions.setter
    def dimensions(self, dimensions):
        self.width, self.height = dimensions
    
    @dimensions.deleter
    def dimensions(self):
        self.width = 1
        self.height = 1


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y) # This formats the output to be inside the Vector() class
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# v1 = Vector(2, 3)
# v2 = Vector(5, 8)
# # v3 = Vector(2, 3)
# # print(v1 + v2) # Output: Vector(7, 11)
# # print(v1 * 2) # Output: Vector, (4, 6)
# # print(v2 / 2) # Output: Vector(2.5, 4.0)
# # print(v1 == v3) # True
# print(v1 == v2) # False

class ACalculator:
    def add(self, *args, **kwargs): # *args will handle unlimited positional arguments (numbers)
        return sum(args) + sum(kwargs.values()) # **kwargs will handle optional keyword arguments (if the keyword arguments were purposely coded in like a=20 and b=30...)


# cal = ACalculator()
# print(cal.add(2, 3, 4, 5, 6, 7, 8, 9, 10, a=20, b=30)) # 104

# Using container magic methods!

import random

class Deck:
    def __init__(self):
        # TODO: Initialize the deck with 52 standard playing cards
        # TODO: Create a list of cards using suits ['H', 'D', 'C', 'S'] and
        # TODO: ranks ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # TODO: Store cards as strings like "2H" (2 of Hearts) or "AS" (Ace of Spades)
        # TODO: Use a list comprehension to create all combinations of rank+suit
        self.suits = ['H', 'D', 'C', 'S']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [r + s for s in self.suits for r in self.ranks]
    
    def __len__(self):
        # TODO: Return the number of cards in the deck
        # TODO: This enables the len(deck) functionality
        return len(self.deck)
    
    def __getitem__(self, index):
        # TODO: Return the card at the specified index
        # TODO: This enables indexing like deck[0] to get the first card
        return self.deck[index]
    
    def __contains__(self, card):
        # TODO: Check if the specified card is in the deck
        # TODO: This enables the 'in' operator like "AS" in deck
        return card in self.deck
    
    def __iter__(self):
        # TODO: Return an iterator for the cards
        # TODO: This enables iteration like 'for card in deck'
        # TODO: Use the built-in iter() function on your cards collection
        return iter(self.deck)
    
    def shuffle(self):
        # TODO: Randomize the order of cards in the deck
        # TODO: Use random.shuffle() on your cards collection
        random.shuffle(self.deck)


# Comprehensive test case handler
# test_case = input()

# def test_basic_functionality():
#     deck = Deck()
#     assert len(deck) == 52, f"Deck should have 52 cards, but has {len(deck)}"
    
#     first_card = deck[0]
#     assert isinstance(first_card, str), f"Card should be a string, but got {type(first_card)}"
    
#     assert "AS" in deck, "Ace of Spades should be in the deck"
#     assert "XY" not in deck, "XY is not a valid card and should not be in the deck"
    
#     cards = [card for card in deck]
#     assert len(cards) == 52, f"Iteration should yield 52 cards, but got {len(cards)}"
    
#     original_first_five = [deck[i] for i in range(5)]
#     deck.shuffle()
#     shuffled_first_five = [deck[i] for i in range(5)]
#     assert original_first_five != shuffled_first_five or len(deck) <= 5, "Shuffle should change card order"
    
#     print("Basic functionality tests passed!")

# def test_edge_cases():
#     deck = Deck()
    
#     # Test first and last card access
#     first_card = deck[0]
#     last_card = deck[51]
#     assert isinstance(first_card, str) and isinstance(last_card, str), "First and last cards should be strings"
    
#     # Test negative indexing
#     assert deck[-1] == deck[51], "Negative indexing should work correctly"
    
#     # Test out of bounds access
#     try:
#         invalid_card = deck[52]
#         print("Test failed: Should raise IndexError for out of bounds access")
#     except IndexError:
#         print("Edge case test passed: IndexError raised for out of bounds access")
    
#     print("Edge case tests passed!")

# def test_card_uniqueness():
#     deck = Deck()
#     cards = [card for card in deck]
#     unique_cards = set(cards)
    
#     assert len(unique_cards) == 52, f"All cards should be unique, but found {len(unique_cards)} unique cards"
    
#     # Verify specific cards exist
#     expected_cards = ["2H", "10S", "KD", "AC"]
#     for card in expected_cards:
#         assert card in deck, f"Expected card {card} not found in deck"
    
#     print("Card uniqueness tests passed!")

# def test_shuffle_behavior():
#     deck = Deck()
#     original_order = [card for card in deck]
    
#     # First shuffle
#     deck.shuffle()
#     first_shuffle = [card for card in deck]
#     assert len(first_shuffle) == 52, "Shuffle should preserve all 52 cards"
#     assert set(first_shuffle) == set(original_order), "Shuffle should not add or remove cards"
    
#     # Most likely the order changed (though there's a tiny probability it didn't)
#     different_order = (original_order != first_shuffle)
    
#     # Second shuffle to be extra sure
#     deck.shuffle()
#     second_shuffle = [card for card in deck]
#     different_order_2 = (first_shuffle != second_shuffle)
    
#     assert different_order or different_order_2, "Multiple shuffles should change the order"
    
#     print("Shuffle behavior tests passed!")

# def test_contains_behavior():
#     deck = Deck()
    
#     # Test all valid cards are in the deck
#     suits = ['H', 'D', 'C', 'S']
#     ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
#     for suit in suits:
#         for rank in ranks:
#             card = rank + suit
#             assert card in deck, f"Valid card {card} should be in the deck"
    
#     # Test invalid cards are not in the deck
#     invalid_cards = ["1H", "11S", "XD", "AX", "JX", ""]
#     for card in invalid_cards:
#         assert card not in deck, f"Invalid card {card} should not be in the deck"
    
#     print("Contains behavior tests passed!")

# def test_iteration_behavior():
#     deck = Deck()
    
#     # Test iteration
#     card_count = 0
#     for card in deck:
#         card_count += 1
#         assert isinstance(card, str), f"Each card should be a string, but got {type(card)}"
    
#     assert card_count == 52, f"Iteration should yield 52 cards, but got {card_count}"
    
#     # Test multiple iterations
#     first_iteration = [card for card in deck]
#     second_iteration = [card for card in deck]
#     assert first_iteration == second_iteration, "Multiple iterations should yield the same order"
    
#     print("Iteration behavior tests passed!")

# # Run the appropriate test based on input
# if test_case == "basic_functionality":
#     test_basic_functionality()
# elif test_case == "edge_cases":
#     test_edge_cases()
# elif test_case == "card_uniqueness":
#     test_card_uniqueness()
# elif test_case == "shuffle_behavior":
#     test_shuffle_behavior()
# elif test_case == "contains_behavior":
#     test_contains_behavior()
# elif test_case == "iteration_behavior":
#     test_iteration_behavior()
# else:
#     # Default test - run the original test suite
#     def test_deck():
#         try:
#             # Test initialization and length
#             deck = Deck()
#             assert len(deck) == 52, f"Deck should have 52 cards, but has {len(deck)}"
            
#             # Test getitem
#             first_card = deck[0]
#             assert isinstance(first_card, str), f"Card should be a string, but got {type(first_card)}"
            
#             # Test contains
#             assert "AS" in deck, "Ace of Spades should be in the deck"
#             assert "XY" not in deck, "XY is not a valid card and should not be in the deck"
            
#             # Test iteration
#             cards = [card for card in deck]
#             assert len(cards) == 52, f"Iteration should yield 52 cards, but got {len(cards)}"
#             assert len(set(cards)) == 52, "All cards in the deck should be unique"
            
#             # Test shuffle (basic check that order changes)
#             original_first_five = [deck[i] for i in range(5)]
#             deck.shuffle()
#             shuffled_first_five = [deck[i] for i in range(5)]
#             assert original_first_five != shuffled_first_five or len(deck) <= 5, "Shuffle should change card order"
            
#             # Check that shuffle doesn't lose cards
#             assert len(deck) == 52, f"Deck should still have 52 cards after shuffle, but has {len(deck)}"
            
#             print("All tests passed!")
#         except AssertionError as e:
#             print(f"Test failed: {e}")

#     test_deck()
#     print("Tests completed")

# Using both inheritance and composition!

class Media:
    def __init__(self, title, creator, year):
        # TODO: Initialize the Media class with title, creator, and year parameters
        # TODO: Store these parameters as instance attributes
        self.title = title
        self.creator = creator
        self.year = year
    
    def display_info(self):
        # TODO: Define a base display_info method that will be overridden by child classes
        # NOTE: This method should be implemented by child classes
        pass

class Book(Media):
    # TODO: No need to implement __init__ as it will use the parent class constructor
    
    def display_info(self):
        # TODO: Override the display_info method to return a formatted string
        # TODO: Format should be: "Book: {title} by {creator} ({year})"
        # Example: "Book: The Hobbit by J.R.R. Tolkien (1937)"
        return f"Book: {self.title} by {self.creator} ({self.year})"

class Movie(Media):
    # TODO: No need to implement __init__ as it will use the parent class constructor
    
    def display_info(self):
        # TODO: Override the display_info method to return a formatted string
        # TODO: Format should be: "Movie: {title} directed by {creator} ({year})"
        # Example: "Movie: The Matrix directed by Wachowski Sisters (1999)"
        return f"Movie: {self.title} directed by {self.creator} ({self.year})"
    
class MusicAlbum(Media):
    # TODO: No need to implement __init__ as it will use the parent class constructor
    
    def display_info(self):
        # TODO: Override the display_info method to return a formatted string
        # TODO: Format should be: "Music Album: {title} by {creator} ({year})"
        # Example: "Music Album: Abbey Road by The Beatles (1969)"
        return f"Music Album: {self.title} by {self.creator} ({self.year})"

class MediaItem:
    def __init__(self, title, creator, year):
        # TODO: Initialize the MediaItem class with title, creator, and year parameters
        # TODO: Store these parameters as instance attributes
        # NOTE: This class will be used for composition approach
        self.title = title
        self.creator = creator
        self.year = year

class BookComposition:
    def __init__(self, title, author, year):
        # TODO: Create a MediaItem instance and store it as self.media
        # TODO: Pass title, author, and year to the MediaItem constructor
        self.media = MediaItem(title, author, year)
    
    def display_info(self):
        # TODO: Return a formatted string using the media object's attributes
        # TODO: Format should be: "Book: {title} by {creator} ({year})"
        # Example: "Book: Dune by Frank Herbert (1965)"
        return f"Book: {self.title} by {self.creator} ({self.year})"
    
class MovieComposition:
    def __init__(self, title, director, year):
        # TODO: Create a MediaItem instance and store it as self.media
        # TODO: Pass title, director, and year to the MediaItem constructor
        self.media = MediaItem(title, director, year)
    
    def display_info(self):
        # TODO: Return a formatted string using the media object's attributes
        # TODO: Format should be: "Movie: {title} directed by {creator} ({year})"
        # Example: "Movie: Inception directed by Christopher Nolan (2010)"
        return f"Movie: {self.title} directed by {self.creator} ({self.year})"

class MusicAlbumComposition:
    def __init__(self, title, artist, year):
        # TODO: Create a MediaItem instance and store it as self.media
        # TODO: Pass title, artist, and year to the MediaItem constructor
        self.media = MediaItem(title, artist, year)
    
    def display_info(self):
        # TODO: Return a formatted string using the media object's attributes
        # TODO: Format should be: "Music Album: {title} by {creator} ({year})"
        # Example: "Music Album: Thriller by Michael Jackson (1982)"
        return f"Music Album: {self.title} by {self.creator} ({self.year})"

# Comprehensive test case handler
# test_case = input()

# def test_inheritance_basic():
#     book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
#     movie = Movie("The Matrix", "Wachowski Sisters", 1999)
#     album = MusicAlbum("Abbey Road", "The Beatles", 1969)
    
#     assert book.display_info() == "Book: The Hobbit by J.R.R. Tolkien (1937)"
#     assert movie.display_info() == "Movie: The Matrix directed by Wachowski Sisters (1999)"
#     assert album.display_info() == "Music Album: Abbey Road by The Beatles (1969)"

# def test_composition_basic():
#     book_comp = BookComposition("Dune", "Frank Herbert", 1965)
#     movie_comp = MovieComposition("Inception", "Christopher Nolan", 2010)
#     album_comp = MusicAlbumComposition("Thriller", "Michael Jackson", 1982)
    
#     assert book_comp.display_info() == "Book: Dune by Frank Herbert (1965)"
#     assert movie_comp.display_info() == "Movie: Inception directed by Christopher Nolan (2010)"
#     assert album_comp.display_info() == "Music Album: Thriller by Michael Jackson (1982)"

# def test_inheritance_relationships():
#     book = Book("Test Book", "Test Author", 2000)
#     movie = Movie("Test Movie", "Test Director", 2001)
#     album = MusicAlbum("Test Album", "Test Artist", 2002)
    
#     assert isinstance(book, Book)
#     assert isinstance(book, Media)
#     assert isinstance(movie, Movie)
#     assert isinstance(movie, Media)
#     assert isinstance(album, MusicAlbum)
#     assert isinstance(album, Media)

# def test_attribute_access():
#     # Test inheritance approach
#     book = Book("Test Book", "Test Author", 2000)
#     assert book.title == "Test Book"
#     assert book.creator == "Test Author"
#     assert book.year == 2000
    
#     # Test composition approach
#     book_comp = BookComposition("Test Book", "Test Author", 2000)
#     assert book_comp.media.title == "Test Book"
#     assert book_comp.media.creator == "Test Author"
#     assert book_comp.media.year == 2000

# def test_polymorphism():
#     media_list = [
#         Book("Book1", "Author1", 2001),
#         Movie("Movie1", "Director1", 2002),
#         MusicAlbum("Album1", "Artist1", 2003)
#     ]
    
#     assert media_list[0].display_info() == "Book: Book1 by Author1 (2001)"
#     assert media_list[1].display_info() == "Movie: Movie1 directed by Director1 (2002)"
#     assert media_list[2].display_info() == "Music Album: Album1 by Artist1 (2003)"

# def test_edge_cases():
#     # Empty strings
#     book = Book("", "", 0)
#     assert book.display_info() == "Book:  by  (0)"
    
#     # Special characters - fixed the syntax error here
#     movie = Movie("Test\"Movie", "Test\\nDirector", -1)
#     assert movie.display_info() == "Movie: Test\"Movie directed by Test\\nDirector (-1)"
    
#     # Extreme years
#     album = MusicAlbum("Test Album", "Test Artist", 9999)
#     assert album.display_info() == "Music Album: Test Album by Test Artist (9999)"

# def test_stress():
#     # Create many media objects
#     books = [Book(f"Book{i}", f"Author{i}", 2000+i) for i in range(100)]
#     movies = [Movie(f"Movie{i}", f"Director{i}", 2000+i) for i in range(100)]
#     albums = [MusicAlbum(f"Album{i}", f"Artist{i}", 2000+i) for i in range(100)]
    
#     for i, book in enumerate(books):
#         assert book.display_info() == f"Book: Book{i} by Author{i} ({2000+i})"
    
#     for i, movie in enumerate(movies):
#         assert movie.display_info() == f"Movie: Movie{i} directed by Director{i} ({2000+i})"
    
#     for i, album in enumerate(albums):
#         assert album.display_info() == f"Music Album: Album{i} by Artist{i} ({2000+i})"

# # Run the appropriate test based on input
# if test_case == "default_test" or test_case == "":
#     test_inheritance_basic()
#     test_composition_basic()
#     print("All tests passed!")
# elif test_case == "inheritance_test":
#     test_inheritance_basic()
#     test_inheritance_relationships()
#     print("Inheritance tests passed!")
# elif test_case == "composition_test":
#     test_composition_basic()
#     print("Composition tests passed!")
# elif test_case == "polymorphism_test":
#     test_polymorphism()
#     print("Polymorphism tests passed!")
# elif test_case == "attribute_test":
#     test_attribute_access()
#     print("Attribute tests passed!")
# elif test_case == "edge_cases":
#     test_edge_cases()
#     print("Edge case tests passed!")
# elif test_case == "stress_test":
#     test_stress()
#     print("Stress tests passed!")

class PrintableMixin:
    def print_details(self):
        # TODO: Implement the print_details method that returns product details
        # TODO: Return a formatted string with product name and price
        # TODO: Use f-string format: "Product: {self.name}, Price: ${self.price}"
        return f"Product: {self.name}, Price: ${self.price}"

class DiscountMixin:
    def apply_discount(self, percent):
        # TODO: Implement the apply_discount method that calculates a discounted price
        # TODO: Calculate the discounted price using the formula: price - (price * percent / 100)
        # TODO: This method should access self.price attribute from the class that uses this mixin
        # TODO: Return the calculated discounted price
        discount_price = self.price - (self.price * percent / 100)
        return discount_price

class ShippableMixin:
    def set_weight(self, weight):
        # TODO: Implement the set_weight method that stores the weight as an attribute
        # TODO: Set self.weight = weight
        self.weight = weight
    
    def calculate_shipping(self):
        # TODO: Implement the calculate_shipping method that calculates shipping cost
        # TODO: Calculate shipping cost using the formula: weight * 0.5 ($0.50 per pound)
        # TODO: This method should access self.weight attribute set by set_weight method
        # TODO: Return the calculated shipping cost
        shipping_cost = self.weight * 0.5
        return shipping_cost

class Product(PrintableMixin, DiscountMixin):
    # TODO: Make this class inherit from PrintableMixin and DiscountMixin
    # TODO: Modify the class definition to: class Product(PrintableMixin, DiscountMixin):
    
    def __init__(self, name, price):
        # TODO: Initialize the product with name and price attributes
        # TODO: Set self.name = name
        # TODO: Set self.price = price
        self.name = name
        self.price = price

class PhysicalProduct(Product, ShippableMixin):
    # TODO: Make this class inherit from Product and ShippableMixin
    # TODO: Modify the class definition to: class PhysicalProduct(Product, ShippableMixin):
    # TODO: No need to override any methods as it inherits all needed functionality
    pass

class DigitalProduct(Product):
    # TODO: Make this class inherit from Product
    # TODO: Modify the class definition to: class DigitalProduct(Product):
    
    def apply_discount(self, percent):
        # TODO: Override the apply_discount method with a special fixed 10% discount
        # TODO: Return self.price * 0.9 (10% off, regardless of the percent parameter)
        # TODO: This special discount ignores the percent parameter and always applies 10%
        discount_price = self.price * 0.9
        return discount_price


def test_basic_functionality():
    # Test basic functionality of all classes
    p = Product("Laptop", 1000)
    assert p.print_details() == "Product: Laptop, Price: $1000", f"Print details failed: {p.print_details()}"
    assert p.apply_discount(10) == 900, f"Discount calculation failed: {p.apply_discount(10)}"
    
    physical = PhysicalProduct("Desk", 500)
    physical.set_weight(30)
    assert physical.calculate_shipping() == 15, f"Shipping calculation failed: {physical.calculate_shipping()}"
    
    digital = DigitalProduct("Software", 200)
    assert digital.apply_discount(10) == 180, f"Digital discount failed: {digital.apply_discount(10)}"
    print("Basic functionality test passed!")

def test_edge_cases():
    # Test edge cases like zero and negative values
    p = Product("Free Item", 0)
    assert p.apply_discount(10) == 0, f"Zero price discount failed: {p.apply_discount(10)}"
    
    p_neg = Product("Negative Item", -100)
    assert p_neg.apply_discount(10) == -90, f"Negative price discount failed: {p_neg.apply_discount(10)}"
    
    physical = PhysicalProduct("Empty Box", 10)
    physical.set_weight(0)
    assert physical.calculate_shipping() == 0, f"Zero weight shipping failed: {physical.calculate_shipping()}"
    
    physical_neg = PhysicalProduct("Anti-Gravity Item", 10)
    physical_neg.set_weight(-5)
    assert physical_neg.calculate_shipping() == -2.5, f"Negative weight shipping failed: {physical_neg.calculate_shipping()}"
    print("Edge cases test passed!")

def test_large_values():
    # Test with very large values
    p = Product("Expensive Item", 1000000)
    assert p.apply_discount(10) == 900000, f"Large value discount failed: {p.apply_discount(10)}"
    
    physical = PhysicalProduct("Heavy Item", 500)
    physical.set_weight(1000)
    assert physical.calculate_shipping() == 500, f"Large weight shipping failed: {physical.calculate_shipping()}"
    print("Large values test passed!")

def test_inheritance():
    # Test inheritance relationships
    p = Product("Test", 100)
    physical = PhysicalProduct("Test", 100)
    digital = DigitalProduct("Test", 100)
    
    assert isinstance(p, PrintableMixin), "Product should inherit from PrintableMixin"
    assert isinstance(p, DiscountMixin), "Product should inherit from DiscountMixin"
    
    assert isinstance(physical, Product), "PhysicalProduct should inherit from Product"
    assert isinstance(physical, ShippableMixin), "PhysicalProduct should inherit from ShippableMixin"
    assert isinstance(physical, PrintableMixin), "PhysicalProduct should inherit from PrintableMixin through Product"
    assert isinstance(physical, DiscountMixin), "PhysicalProduct should inherit from DiscountMixin through Product"
    
    assert isinstance(digital, Product), "DigitalProduct should inherit from Product"
    assert isinstance(digital, PrintableMixin), "DigitalProduct should inherit from PrintableMixin through Product"
    assert isinstance(digital, DiscountMixin), "DigitalProduct should inherit from DiscountMixin through Product"
    print("Inheritance test passed!")

def test_method_overriding():
    # Test method overriding behavior
    p = Product("Regular Product", 100)
    digital = DigitalProduct("Digital Product", 100)
    
    # Same price, same discount percentage, different results
    assert p.apply_discount(20) == 80, f"Regular discount calculation failed: {p.apply_discount(20)}"
    assert digital.apply_discount(20) == 90, f"Digital fixed discount failed: {digital.apply_discount(20)}"
    
    # Digital product should always apply 10% discount regardless of parameter
    assert digital.apply_discount(0) == 90, "Digital product should apply 10% discount even with 0%"
    assert digital.apply_discount(50) == 90, "Digital product should apply 10% discount even with 50%"
    print("Method overriding test passed!")

def test_polymorphism():
    # Test polymorphic behavior with a list of different product types
    products = [
        Product("Regular", 100),
        PhysicalProduct("Physical", 100),
        DigitalProduct("Digital", 100)
    ]
    
    # Set weight for the physical product
    products[1].set_weight(10)
    
    # Expected results for apply_discount(20)
    expected_discounts = [80, 80, 90]
    
    for i, product in enumerate(products):
        # All should have print_details method
        assert "Product:" in product.print_details(), f"Polymorphic print_details failed for {type(product)}"
        
        # All should have apply_discount method but with different implementations
        assert product.apply_discount(20) == expected_discounts[i], f"Polymorphic apply_discount failed for {type(product)}"
    print("Polymorphism test passed!")

def test_attribute_access():
    # Test attribute access patterns
    p = Product("Test Product", 100)
    assert p.name == "Test Product", "Name attribute not properly set in Product"
    assert p.price == 100, "Price attribute not properly set in Product"
    
    physical = PhysicalProduct("Physical Product", 200)
    assert physical.name == "Physical Product", "Name attribute not properly set in PhysicalProduct"
    assert physical.price == 200, "Price attribute not properly set in PhysicalProduct"
    
    # Weight attribute should not exist before set_weight is called
    try:
        weight = physical.weight
        assert False, "Weight attribute should not exist before set_weight is called"
    except AttributeError:
        pass
    
    physical.set_weight(15)
    assert physical.weight == 15, "Weight attribute not properly set in PhysicalProduct"
    
    digital = DigitalProduct("Digital Product", 300)
    assert digital.name == "Digital Product", "Name attribute not properly set in DigitalProduct"
    assert digital.price == 300, "Price attribute not properly set in DigitalProduct"
    print("Attribute access test passed!")

# Main test runner
test_case = input()

if test_case == "basic_test":
    test_basic_functionality()
elif test_case == "edge_cases":
    test_edge_cases()
elif test_case == "large_values":
    test_large_values()
elif test_case == "inheritance":
    test_inheritance()
elif test_case == "method_overriding":
    test_method_overriding()
elif test_case == "polymorphism":
    test_polymorphism()
elif test_case == "attribute_access":
    test_attribute_access()