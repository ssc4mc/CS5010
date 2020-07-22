#Testing BookLover
#Summer Chambers
#ssc4mc

import unittest
from mod5_live_booklover import *

class BookLoverTestCase(unittest.TestCase):
    
    
    #tests for our __init__ method
    def test_bookLover_init1(self):
        booklover_a = BookLover("Lana", "lananana@aol.com", "Mystery")
        self.assertEqual(booklover_a.email, "lananana@aol.com")
        
    def test_bookLover_init2(self):
        booklover_a = BookLover("Lana", "lananana@aol.com", "Mystery")
        self.assertEqual(booklover_a.numBooks, 0)
        

#tests for our addBook method
    def test_addBook_false(self):
        booklover_a = BookLover("Lana", "lananana@aol.com", "Mystery", 1, [("Sherlock Holmes", 5)])
        booklover_a.addBook("book", 4)
        self.assertEqual(booklover_a.addBook("Sherlock Holmes", 5), False)

    def test_addBook_true(self):
        booklover_a = BookLover("Lana", "lananana@aol.com", "Mystery", 1, [("Sherlock Holmes", 5)])
        self.assertTrue(booklover_a.addBook("Merlin", 3))
        
    
    #tests for our hasRead method
    def test_hasRead_false(self):
        booklover_a = BookLover("Lana", "lananana@aol.com", "Mystery", 1, [("Sherlock Holmes", 5)])
        self.assertFalse(booklover_a.hasRead("Merlin"))
    
    def test_hasRead_true(self):
         booklover_a = BookLover("Lana", "lananana@aol.com", "Mystery", 1, [("Sherlock Holmes", 5)])
         self.assertTrue(booklover_a.hasRead("Sherlock Holmes"))
        
        
    #test for our numBooksRead method
    def test_numBooksRead_works(self):
         booklover_a = BookLover("Lana", "lananana@aol.com", "Mystery", 8)
         self.assertEqual(booklover_a.numBooksRead(), 8)
         
         
    #test for our favBooks method
    def test_favBooks1(self):
        booklover_a = BookLover("Lana", "lananana@aol.com", "Mystery", 3, [("Sherlock Holmes", 5), ("Merlin", 3), ("Harry Potter", 4)])
        self.assertEqual(booklover_a.favBooks(), [("Sherlock Holmes", 5), ("Harry Potter", 4)])
        
    def test_favBooks2(self):
        booklover_a = BookLover("Lana", "lananana@aol.com", "Mystery", 3, [("Sherlock Holmes", 3), ("Merlin", 2), ("Harry Potter", 1)])
        self.assertEqual(booklover_a.favBooks(), [])
        


#make it run if main
if __name__ == "__main__":
    unittest.main()   
