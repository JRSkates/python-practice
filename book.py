class Book:
  def __init__(self, title, author, availablity):
    self.title = title
    self.author = author
    self.availablity = availablity

  def check_availablity(self):
    return self.availablity > 0
  
  def borrow_book(self):
    if self.check_availablity():
      self.availablity -= 1
      return True
    else:
      return False
    
  def return_book(self):
    self.availablity += 1
