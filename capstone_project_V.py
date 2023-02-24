'''SE T48 - Capstone Project V
Compulsory Task 
Create a program that can be used by a bookstore clerk. The program should allow the clerk to:
- add new books to the database
- update book information
- delete books from the database
- search the database to find a specific book
'''

#=====Importing libraries===========
import sqlite3

#=====Creating database===========
'''Create a database called ebookstore and a table called books.'''

# Creates or opens a file called ebookstore_db with SQLite3 DB
db = sqlite3.connect('ebookstore_db')
# Get a cursor object
cursor = db.cursor() 
# Checks if the table 'python_programming' exists and if not creates it
cursor.execute('''
    CREATE TABLE IF NOT EXISTS
                        books(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Title TEXT,
                            Author TEXT,
                            Qty INTEGER
                            )''')
# Commit the change
db.commit()


# Creating list of books
book_list = [
    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J. K. Rowling", 40),
    (3003, "The Lion, the Witch, and the Wardrobe", "C. S. Lewis", 25),
    (3004, "The Lord of the Rings", "J. R. R. Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Caroll", 12)
]

#====Define Functions====

def insert_book_list(books_list):
    '''Insert several books from a list into books table'''
    try:
        cursor.executemany(''' INSERT INTO books VALUES(?,?,?,?)''', (books_list))
        db.commit()
    # Catch the exception
    except Exception as e:
        # Roll back and change if somethihg goes wrong
        db.rollback()
        print(f'Books not inserted into table due to error:\n{e}')
    else:
        print(f"{len(books_list)} books added to books table!")

def insert_book(title, author, qty):
    '''Insert single book into books table'''
    try:
        # Inserts new book into database and auto increments id
        cursor.execute('''INSERT INTO books(Title, Author, Qty) VALUES(?,?,?)''', (title, author, qty))
        db.commit()
    # Catch the exception
    except Exception as e:
        # Roll back and change if somethihg goes wrong
        db.rollback()
        print(f'Book not inserted into table due to error:\n{e}')
    else:
        print(f"New book '{title}' added to books table!")

def fetch_book(id):
    '''Check if book in table. Will be NONE if not found'''
    cursor.execute('''SELECT * FROM books WHERE id = ?''', (id,))
    book = cursor.fetchone()
    return book

def display_book(id):
    '''Display a book from books table with id'''
    cursor.execute('''SELECT * FROM books WHERE id = ?''', (id,))
    book = cursor.fetchone()
    id, title, author, qty = book[0], book[1], book[2], book[3]
    #Format for printing book
    print('-'*100)
    print ("{:<10} {:<50} {:<30} {:<10}".format('ID','TITLE','AUTHOR','QTY'))
    print ("{:<10} {:<50} {:<30} {:<10}".format(id, title, author, qty))
    print('-'*100)

def update_books(qty_val, id):
    '''Update the quantity of a book with id'''
    try:
        cursor.execute('''UPDATE books SET Qty = ? WHERE id = ?''', (qty_val, id))
        db.commit()
        # Catch the exception
    except Exception as e:
        # Roll back and change if somethihg goes wrong
        db.rollback()
        print(f'Book not updated due to error:\n{e}')
    else:
        print(f"Book with id '{id}' has been updated!")

def search_books(search_str):
    '''Search book titles in book table'''
    cursor.execute('''SELECT * FROM books WHERE Title LIKE ? ''', (f'%{search_str}%',))
    results_table = cursor.fetchall()
    #Format for to display results
    print('SEARCH RESULTS')
    print('-'*100)
    print ("{:<10} {:<50} {:<30} {:<10}".format('ID','TITLE','AUTHOR','QTY'))
    for row in results_table:
        id, title, author, qty = row[0], row[1], row[2], row[3]
        print ("{:<10} {:<50} {:<30} {:<10}".format(id, title, author, qty))
    print('-'*100)

def delete_books(id):
    '''Deletes a book from books table with id'''
    try:
        cursor.execute('''DELETE FROM books WHERE id = ? ''', (id,))
        db.commit()
    except Exception as e:
        # Roll back and change if somethihg goes wrong
        db.rollback()
        print(f'Book not deleted due to error:\n{e}')
    else:
        print(f'Book with id {id} deleted!')

def print_table():
    '''Display books table'''
    cursor.execute('''SELECT * FROM books''')
    table = cursor.fetchall()
    #Format for books table
    print('BOOKS TABLE')
    print('-'*100)
    print ("{:<10} {:<50} {:<30} {:<10}".format('ID','TITLE','AUTHOR','QTY'))
    for row in table:
        id, title, author, qty = row[0], row[1], row[2], row[3]
        print ("{:<10} {:<50} {:<30} {:<10}".format(id, title, author, qty))
    print('-'*100)


#====Call Functions====

insert_book_list(book_list)

#====Menu section====

while True:
    menu_choice = input('''
---------------------------------
Choose an option from the menu:
    ----
    1. Enter book
    2. Update book
    3. Delete book
    4. Search books
    5. Display books
    0. Exit
    ----
Enter your choice: ''')
    if menu_choice == '1':
        '''Enters new book in books table'''
        title = input("Enter book title: ")
        if not title:
            print('You need to enter book title.')
        else:
            author = input("Enter book author: ")
            if not author:
                print('You need to enter book author.')
            else:
                try:
                    qty = int(input("Enter book quantity: "))
                except ValueError:
                    print("Whoops! You need to enter an integer.")
                else:
                    insert_book(title, author, qty)

    elif menu_choice == '2':
        '''Update chosen book Qty with id'''
        try:
            id = int(input("Enter book id: "))
        except ValueError:
            print("Whoops! You need to enter an integer.")
        else:
            try:
                chosen_book = fetch_book(id)
            except Exception as e:
                print(f'Oh no! There was an error:\n{e}')
            else:
                if chosen_book is not None:
                    print(f'You have chosen:')
                    display_book(id)
                    try:
                        new_qty = int(input('Enter new qty: '))
                    except ValueError:
                        print("Whoops! You need to enter an integer.")
                    else:
                        try:
                            update_books(new_qty, id)
                        except Exception as e:
                            print(f'Book was not updated due to error:\n{e}')
                        else:
                            display_book(id)
                else:
                    print(f'Sorry, no book found with id {id}')

    elif menu_choice == '3':
        '''Delete book from table'''
        try:
            id = int(input("Enter book id: "))
        except ValueError:
            print("Whoops! You need to enter an integer.")
        else:
            try:
                chosen_book = fetch_book(id)
            except Exception as e:
                print(f'Oh no! There was an error:\n{e}')
            else:
                if chosen_book is not None:
                    print(f'You have chosen:')
                    display_book(id)
                    # Ask user to confirm deletion
                    confirm_delete = input('Are you sure you want to delete? (y/n): ').lower()
                    if confirm_delete == 'y': # If use inputs 'y'
                        delete_books(id)
                    else: # Any other input
                        print(f'Book id {id} not deleted.')
                else:
                    print(f'Sorry, no book found with id {id}')

    elif menu_choice == '4':
        '''Search books table'''
        search_str = input('Enter book title to search (case sensitive): ')
        search_books(search_str)

    elif menu_choice == '5':
        '''Display all books in table'''
        print_table()

    elif menu_choice == '0':
        # Exit
        print('Goodbye!')
        exit()

    else:
        print("You have made a wrong choice. Please try again.")

    # Commit the change
    db.commit()

db.close()