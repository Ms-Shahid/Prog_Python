#Learning and implementing the concepts of oops


"""
The pillars of OOPs

1->Abstraction:Take the details of program(data) which are essential to us, by ommiting the non-essential details
2->Encapsulation: Here we bind the data associated with object and methods associated with it.
3->Inheritance:Where we use common characterics from the another class, which has been already derived.
4->Ploymorphism:Objects with different forms behaves differently.

"""

#Creating a book store using oops
class Book:

    #This are the properties of the Class BOOK
    
    #Methods of the Book are the fuctions inside the class Book
    def __init__(self,title,author,pubDate, price):
        self.title = title
        self.author = author
        self.pubDate = str(pubDate)
        self.price = str(price)

        print(self.title + ' | ' + self.author + ' | ' + self.pubDate + ' | ' + self.price)
        print('*************************')


#Objects of class Book are:

book1 = Book('The robin Hood','Benjamin',1998,3.54)
book1.title,book1.author,book1.pubDate,book1.price


#Second object
book2 = Book('The Alchemist','Paulo Coelho',1988,10.19)
book2.title,book2.author,book2.pubDate,book2.price

#Third object
book3 = Book('As a Man Thinketh','James Allen',1902,5.99)
book3.title,book3.author,book3.pubDate,book3.price

