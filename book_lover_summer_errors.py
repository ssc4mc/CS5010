#Mod5 Live Session: BookLover Testing
#Summer Chambers
#ssc4mc

class BookLover:
    
    def __init__(self, name, email, favGenre, numBooks=0, bookList=None):
        self.name = email #error
        self.email = name #error
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
        return None #error
        
        
    def hasRead(self, bookName):
        for book_tuple in self.bookList:
            if bookName not in book_tuple: #error
                return True
        return False
        
    
    def numBooksRead(self):
        return self.favGenre #error
    
    
    def favBooks(self):
        goodList = list(filter(lambda x: x[1] > 4, self.bookList)) #error
        return goodList 
