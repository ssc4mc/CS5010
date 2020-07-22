#Mod5 Live Session: BookLover
#Summer Chambers
#ssc4mc

class BookLover:
    
    def __init__(self, name, email, favGenre, numBooks=0, bookList=None):
        self.name = name
        self.email = email
        self.favGenre = favGenre
        self.numBooks = numBooks
        self.bookList = bookList or []
        
        
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Favorite Genre: {self.favGenre}, Number of Books: {self.numBooks}, Book List: {self.bookList}"
    
    
    def addBook(self, bookName, rating):
        for book_tuple in self.bookList:
            if bookName in book_tuple:
                return False
        self.bookList.append((bookName, rating))
        self.numBooks += 1
        return True
        
        
    def hasRead(self, bookName):
        for book_tuple in self.bookList:
            if bookName in book_tuple:
                return True
        return False
        
    
    def numBooksRead(self):
        return self.numBooks
    
    
    def favBooks(self):
        goodList = list(filter(lambda x: x[1] > 3, self.bookList))
        return goodList
        

booklover1 = BookLover("Joanne", "jojo@gmail.com", "Fantasy")

print(booklover1)
    
booklover1.addBook("Harry Potter", 5)

print(booklover1.hasRead("Harry Potter"))

booklover1.addBook("War and Peace", 3)
print(booklover1.bookList)

booklover1.addBook("War and Peace2", 3)
print(booklover1.bookList)

print(booklover1.numBooksRead())

print(booklover1.favBooks())