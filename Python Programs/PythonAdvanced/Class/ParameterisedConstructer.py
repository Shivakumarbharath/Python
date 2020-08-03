class Course:
    def __init__(self, name, ratings):
        self.name = name
        self.rating = ratings

    def Average(self):  # defining the instance method
        length = len(self.rating)
        average = sum(self.rating) / length  # Sum gives the sum of all integersin the list
        print("The Aveage Ratings of ", self.name, "is ", average)


c1 = Course("Python", [5, 5, 5, 4, 5])

print(c1.name)
print(c1.rating)
c1.Average()
