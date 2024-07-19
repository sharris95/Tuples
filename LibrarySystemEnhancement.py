#Library System Enhancement

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")] # List of tuples
def add_book(library, book):
    if book not in library:
        library.append(book)
    else:
        print(f"The book '{book[0]}' by {book[1]} is already in the library.")

# Example usage:
new_book = ("Fahrenheit 451", "Ray Bradbury")
add_book(library, new_book)
print(library)