import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author_1 = Author("Susan", "Hill")
author_repository.save(author_1)
author_2 = Author("Andrew", "Kaufman")
author_repository.save(author_2)
author_3 = Author("Shirley", "Jackson")
author_repository.save(author_3)

book_1 = Book("The Woman in Black", author_1, "Fiction, Horror, Thriller")
book_repository.save(book_1)
book_2 = Book("All My Friends Are Superheroes", author_2, "Fiction, Comedy")
book_repository.save(book_2)
book_3 = Book("The Haunting of Hill House", author_3, "Fiction, Horror")
book_repository.save(book_3)
book_repository.select_all()

pdb.set_trace()
