class Customer:
    def __init__(self, name, membership_type): # instructor and initiator # self: means "this" represant whatever customer we're creating
        self.name = name
        self.membership_type = membership_type

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
    #__repr__ = __str__


customers = [Customer("Wilbert", "Gold"), Customer("Brad", "Bronze")]
print(customers[1].membership_type)
customers[1].update_membership("Gold")
print(customers[1].membership_type)
