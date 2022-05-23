class Staff(object):
    def __init__(self, firstname, lastname, location, role):
        # record attributes of the current stuff
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.role = role

    def information(self):
        # print information of the staff
        print(f'Full name: {self.firstname} {self.lastname} Location: {self.location} Role: {self.role}')


# example of using the class
first = 'Caitriana'
last = 'Nicholson'
loc = 'International Campus'
Role = 'faculty'
staff1 = Staff(first, last, loc, Role)
staff1.information()
