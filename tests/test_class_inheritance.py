from code.class_inheritance import Teacher

x = Teacher('Amy', 'Harrot', 1979)

assert x.get_name() == 'Amy Harrot', 'Name should be "Amy Harrot"'

assert x.get_year() == 1989, 'Year should be 1989'