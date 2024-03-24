#Initialize two data structures to keep track of books and members both represented as lists.
books = []
members = []

# The system features two functions (You must create these functions): add_book and add_member.
# The add_book function takes three parameters (book_id, title, author, status) and appends a new book 
# dictionary to the books list.

"""Suppose you use the system to add a book titled "Python Programming" written by Jacob Zuma with a 
book_id of 2024001, and a member named Anelisa Maleka with a member_id of 1. How would these 
additions reflect in the books and members lists, and what would the output look like if you printed 
both lists immediately after these additions?
Hint: call the functions and write a print statement for them"""
def add_book(book_id, title, author, status):
   add_book.append({
       "book_id ": 2024001,
        "title ": "Python Programming ",
        "author ": "Jacob Zuma",
        "status ": []
       
   })
   print("Books records ", add_book)
