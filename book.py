class publisher:
    def __init__ (self,name):
        self.name=name
    def display(self):
        print("publisher: ",self.name)

class book(publisher):
    def __init__(self, name,author,title):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print(" title: ",self.title, " author: ",self.author)

class python(book):
    def __init__(self, name, author, title,price,no_of_pages):
        super().__init__(name, author, title)
        self.price=price
        self.no_of_pages=no_of_pages

    def display(self):
        super().display()
        print(" price: ",self.price," number of pages: ",self.no_of_pages)
    
Book=python(name="french",author="paulo coelho",title="Alchemist",price="200",no_of_pages="300")
Book.display()