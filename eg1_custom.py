class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self): # Override would run teach version of log 
        print("I'm a teacher!")
class Customer(User):
    def __init__(self, name, membership_type): # instructor and initiator # self: means "this" represant whatever customer we're creating
        self.name = name
        self.membership_type = membership_type
    @property
    def name(self):
        print("get name")
        return self._name

    @name.setter
    def name(self, name):
        print("set name")
        self._name = name

    @name.deleter
    def name(self):
        print("delete name")
        del self._name

    def update_membership(self, new_membership):
        # invoke an API
        # update a database
        # charge the customer
        # calculate costs
        # anything
        self.membership_type = new_membership

    def __str__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    #__hash__ = None
    __repr__ = __str__


users = [Customer("Wilbert", "Gold"), Customer("John", "Silver"), Teacher()]
for user in users:
    user.log()
