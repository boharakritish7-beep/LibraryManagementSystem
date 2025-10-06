from book import EBook, PrintedBook
from book_manager import BookManager
from payment import CreditCardPayment, PayPalPayment, LibrarySystem

# Create book objects
ebook = EBook("Python Basics", "John Smith", 10)
printed = PrintedBook("OOP Concepts", "Jane Doe", 20)

# Demonstrate polymorphism
print(f"EBook Late Fee for 4 days: ${ebook.calculateLateFee(4)}")
print(f"PrintedBook Late Fee for 4 days: ${printed.calculateLateFee(4)}")

# Manage books
manager = BookManager()
manager.add_book(ebook)
manager.add_book(printed)
manager.list_books()

# Payment system demo
system = LibrarySystem(CreditCardPayment())
system.make_payment(50)
