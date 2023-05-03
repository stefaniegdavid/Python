#Create the user class and add a couple of methods
# first_name, last_name, email, age
# is_rewards_member - default value of False, gold_card_points = 0
# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        
        self.is_rewards_member=False
        self.gold_card_points=0

    # print(my_user.first_name)
    # print(my_user.last_name)
    # print(my_user.email)
    # print(my_user.age)
    # print(my_user.is_rewards_member)
    # print(my_user.gold_card_points)

    def display_info(self):
        print("============================")
        print(f"First name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("==============================")

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        # return self

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount

my_user = User("Stefanie", "David", "Stefaniedavid@gmail.com", 29)
my_user.display_info()

user2 = User("David", "Dishoyan", "daviddish@yahoo.com", 27)
user3 = User("Andrew", "Dishoyan" "a.dishoyan@gmail.com", 21)

my_user.spend_points(50)
user2.enroll().spend_points(80)

my_user.display_info()
user2.display_info()
user3.display_info()

#=====CHAINING METHODS=====
my_user.display_info().enroll().spend_points(100).display_info()



