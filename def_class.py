class User:

    def __init__(self, user_id, user_name,):
        self.id = user_id
        self.name = user_name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower +=1
        self.following +=1


user_1 = User("123", "Karan", "105")
user_2 = User("345", "Shanu", "35")

user_1.follow(user_2)

print("User id of this person is: ", user_1.id)
print("User's name is: ", user_1.name)
print("Followers of the user's are : ", user_1.follower)
print("User's following are : ", user_1.following)
print("User id of this person is: ", user_2.id)
print("User's name is: ", user_2.name)
print("Followers of the user's are : ", user_2.follower)
print("User's following are : ", user_2.following)

