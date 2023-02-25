# finalCapstone

This project was created as part of HyperionDev Software Engineer Bootcamp.

## Capstone Project V

### Summary

This programme uses Python and SQLite.

A programme that can be used by a bookstore clerk. The programme allows the clerk to read and update a books database, called ebookstore. The programme allows the clerk to:
* add new books
* update book information
* delete books
* search the database to find a specific book.

### Using the programme

The programme will present the user with the following menu:
1. Enter book
2. Update book
3. Delete book
4. Search books
5. Exit

These inputs will manipulate the ebookstore table, which has the following structure:

| **id** | **Title**                                | **Author**      | **Qty** |
|--------|------------------------------------------|-----------------|---------|
| 3001   | A Tale of Two Cities                     | Charles Dickens | 30      |
| 3002   | Harry Potter and the Philosopher's Stone | J. K. Rowling   | 40      |


#### Enter book
Programme will ask the user for the Title, Author and Quantity of the new book to be entered into the database. The fields are added to the database and the id automattically incremented.

#### Update book
The programme will allow the user to update the quantity of a chosen book with id. The updated book entry will then be displayed with the new quantity.

#### Delete book
The programme will allow the user to delete a book from the database, chosen by id. The chosen book entry will be displayed and the user is asked to confirm deletion.

#### Search book
The programme will allow the user to search the Titles in the ebookstore table with a simple, case-sensitive searchword. e.g. Entering 'Harry' will find Harry Potter and the Philosopher's Stone.

#### Exit
Exits the programme.

### Installation
Download the file and open with your preferreed IDE.
