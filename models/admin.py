from .user import User

class Admin(User):

    def __init__(self, name, email, password_hash):

        super().__init__(
            name,
            email,
            password_hash,
            age=0,
            weight=0,
            height=0,
            role="admin"
        )

    def view_users(self, users):
        for u in users:
            print(u.username, "-", u.email)

    def delete_user(self, users, email):
        for u in users:
            if u.email == email:
                users.remove(u)
                print("Deleted:", email)
                return

        print("Not found")