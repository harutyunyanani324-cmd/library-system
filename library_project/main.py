from src.models.items import Book, DVD
from src.user.user import User
from src.services.library import Library


my_lib = Library()

book1 = Book("Python Basics", "B01", "Guido van Rossum", 300)
dvd1 = DVD("Inception", "D01", 148, "Sci-Fi")

my_lib.add_item(book1)
my_lib.add_item(dvd1)


erik = User("Erik")
erik.borrow_item(book1)
erik.list_borrowed_items()
erik.return_item(book1)


print("\nLibrary Status:")
print(my_lib)
my_lib.display_all_items()

print("\nSUCCESS: The library system is running correctly!")
