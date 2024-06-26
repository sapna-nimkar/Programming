# Dunder or Magic Methods

my_list = [1,2,3]

print(len(my_list))

class Sample():
    pass

mysample = Sample()
print(mysample)   # <__main__.Sample object at 0x000002578F88A6A0>  -> gives the location of the object

class Book():

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'
    def __len__(self):
        return self.pages

    def __del__(self):
        print("the book object has been deleted")


b = Book("Python Study", "Jose Portilla", 50)
print(b)
print("***")
print(str(b))
print(len(b))
len(b)

del b

