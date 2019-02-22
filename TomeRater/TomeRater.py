#defining User class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email= email
        self.books = {}
        
#Get email
    def get_email(self):
        return self.email
    
#Update/change email
    def change_email(self, new_email):
        self.email= new_email
        return"{name}'s email has changed to {new_email}".format(name= self.name,new_email = new_email)
       

#represent
    def __repr__(self):
        return "User: {name}, email: {email}, books read:{books}".format(name = self.name, email= self.email, books = len(self.books))

#check for equals
    def __eq__(self, other_user):
              if self.name == other_user.name and self.email == other_user.email:
                  return "Same user"

              
#adds items to Read Book dictionary
    def read_book (self, book, rating = None):
        self.books[book] = rating
    
#Gets Average Ratings from a user's read books dictionary
    def get_average_rating (self):
        sum_ratings=0
        average_rating = 0
        for rating in self.books.values():
            if rating != None:
                sum_ratings += rating
        average_rating = sum_ratings / len(self.books)
        return average_rating
            
         
#defining Book class
class Book():
    def __init__ (self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

        
    def get_title (self):
        return self.title

    
    def get_isbn (self):
        return self.isbn

    
    def set_isbn (self, new_isbn):
        if new_isbn == self.isbn:
            return "This ISBN is already registered"
        elif new_isbn != self.isbn:
            self.isbn = new_isbn
            return "{title}'s ISBN has been updated to {new_isbn}".format(title=self.title, new_isbn=self.isbn)
        else:
            return "ISBN can only be numbers"

            
    def add_rating (self, rating):
        if rating in range(0,6):
            self.ratings.append(rating)
        else:
            return "Invalid Rating"
       
            
    def __eq__ (self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return "Same Book"
        else:
            pass

    def get_average_rating (self):
        ratings_sum = 0
        ratings_average = 0
        for ratings in self.ratings:
            ratings_sum += ratings
        ratings_average = ratings_sum/len(self.ratings)
        return ratings_average
    
    def __hash__ (self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title

        
#defining Fiction, Book subclass
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    def get_author (self):
        return self.author
    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

#defining Non-fiction, Book subclass
class Non_Fiction(Book):
    def __init__ (self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    def get_subject (self):
        return self.subject
    def get_level (self):
        return self.level
    def __repr__ (self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

#defining TomeRater
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

        
    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction (title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            user = self.users[email]
            user.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book]=1
            else:
                self.books[book] += 1

        else:
            print ("No user with email {email}".format(email= email))
        

    def add_user (self, name, email, user_books = None):
        valid_domains = ['.com', '.org', '.edu'] #checks for valid mail endings
        count = 0
        for domain in valid_domains:
            if domain in email:
                count += 1
        if count != 1: #if not valid domain or repeated
            print ("not a valid email address")
        else:
            if "@" not in email:
                print("not a valid email address")
            elif email in self.users:
                print("This address is already registered")
            else:
                new_user = User(name, email)
                self.users[email] = new_user
                if user_books != None:
                    for book in user_books:
                        self.add_book_to_user(book, email)
        
        
    def print_catalog(self):
        for keys in self.books.keys():
            print (keys)

    def print_users(self):
        for user in self.users.values():
            print (user)

    def most_read_book(self):
        most_read = ""
        read_times = 0
        for books, times in self.books.items():
            if times > read_times:
                read_times = times
                most_read = books
        return most_read


    def highest_rated_book (self):
        highest_rating = 0
        highest_rated = ""
        for book in self.books.keys():
            book_ratings = book.get_average_rating()
            if book_ratings > highest_rating:
                highest_rating = book_ratings
                highest_rated = book
        return highest_rated

    def most_positive_user(self):
        current_high_average = 0
        current_high_user = None
        for user in self.users.values():
            average = user.get_average_rating()
            if average > current_high_average:
                current_high_average = average
                current_high_user = user
        return current_high_user
        

    
        
        
            
            
        
