# ------------------------------------------------------------------------------------------------ #
#                                      Creating Classes in OOP                                     #
# ------------------------------------------------------------------------------------------------ #


### Creating a class
class User:
    def __init__(self, user_id, username):
        self.id = user_id  # setting user_id parameter to the ide of the object
        self.username = username
        self.followers = 0  # creating a follower attribute (with a default value)
        self.following = 0

    #! methods always have a 'self' param (identifies which object called it)
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Harper")  # creating an object (instance) of the User class
user_2 = User("002", "Penny")  # creating an object (instance) of the User class
print(user_2.username)  # Output: Harper

user_1.follow(user_2)  # calling the follow() method of user_1

print(f"{user_1.username}'s followers {user_1.followers}")
print(f"{user_1.username} is following {user_1.following}")
print(f"{user_2.username}'s followers {user_2.followers}")
print(f"{user_2.username} is following {user_2.following}")
