
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return self.first_name + ' ' + self.last_name


class Teacher(Person):
    def __init__(self, first_name, last_name, year):
        Person.__init__(self, first_name, last_name)
        self.year = year

    def get_year(self):
        return self.year
