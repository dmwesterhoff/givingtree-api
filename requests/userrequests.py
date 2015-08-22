from models import User

class UserRequests:

    def user_with_id(self, user_id):
        return User.get(User.id == user_id)

    def user_with_email(self, email):
        return User.get(User.email == 'dmwesterhoff@gmail.com')
