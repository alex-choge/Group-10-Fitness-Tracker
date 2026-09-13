from utils.auth import AuthManager
from utils.decorator import login_required, admin_required
from utils.storage import load_json, save_json
from models.goal import Goal

class FitnessTracker:
    def __init__(self):
        self.auth = AuthManager()
        self.current_user = None

    def start(self):
        while True:
            print("\nFITNESS TRACKER")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

    def register(self):
        print("\n--- Register ---")
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        try:
            age = int(input("Enter your age: ").strip())
            weight = float(input("Enter your weight: ").strip())
            height = float(input("Enter your height: ").strip())
            role = input("Role (user/trainer/admin) [user]: ").strip().lower() or "user"
            user = self.auth.register(name, email, password, age, weight, height, role)
            print(f"Account created for {user.username}!")
            self.current_user = user
            if user.role == "admin":
                self.admin_menu()
            else:
                self.user_menu()
        except ValueError as error:
            print(f"Error: {error}")

    def login(self):
        print("\n--- Login ---")
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        user = self.auth.login(email, password)
        if user:
            self.current_user = user
            print(f"Welcome, {user.username}!")
            if user.role == "admin":
                self.admin_menu()
            else:
                self.user_menu()
        else:
            print("Invalid email or password.")

    @login_required
    def user_menu(self):
        while self.current_user is not None:
            print("\nUSER MENU")
            print("1. View Profile")
            print("2. Add Goal")
            print("3. View Goals")
            print("4. Update Weight")
            print("5. Set Trainer")
            print("6. Delete My Account")
            print("7. Logout")
            choice = input("Choose an option (1-7): ").strip()
            if choice == "1":
                self.view_profile()
            elif choice == "2":
                self.add_goal()
            elif choice == "3":
                self.current_user.view_goals()
            elif choice == "4":
                self.update_weight()
            elif choice == "5":
                self.set_trainer()
            elif choice == "6":
                self.delete_my_account()
            elif choice == "7":
                self.logout()
            else:
                print("Invalid choice.")

    @login_required
    def view_profile(self):
        print("\nMY PROFILE")
        print(f"Name: {self.current_user.username}")
        print(f"Email: {self.current_user.email}")
        print(f"Age: {self.current_user.age}")
        print(f"Weight: {self.current_user.weight} kg")
        print(f"Height: {self.current_user.height} cm")
        print(f"Role: {self.current_user.role}")
        print(f"Trainer: {self.current_user.trainer}")
        print(f"Goals: {len(self.current_user.goals)}")

    @login_required
    def add_goal(self):
        print("\nADD GOAL")
        title = input("Enter goal title: ").strip()
        description = input("Enter goal description: ").strip()
        if not title.strip() or not description.strip():
            print("Goal title and description cannot be empty.")
            return
        goal = Goal(title, description)
        self.current_user.add_goal(goal)
        self.save_current_user()

    @login_required
    def update_weight(self):
        print("\nUPDATE WEIGHT")
        try:
            new_weight = float(input("Enter your new weight: ").strip())
            if new_weight <= 0:
                print("Weight must be greater than 0.")
                return
            self.current_user.update_weight(new_weight)
            self.save_current_user()
        except ValueError:
            print("Please enter a valid number.")

    @login_required
    def set_trainer(self):
        print("\nSET TRAINER")
        trainer_name = input("Enter trainer name: ").strip()
        if not trainer_name:
            print("Trainer name cannot be empty.")
            return
        self.current_user.set_trainer(trainer_name)
        self.save_current_user()
        print(f"Trainer set to {trainer_name}!")

    @login_required
    def delete_my_account(self):
        confirm = input(f"Are you sure you want to delete {self.current_user.email}? (yes/no): ").strip().lower()
        if confirm!= "yes":
            print("Cancelled.")
            return
        users = load_json("data/users.json")
        users = [u for u in users if u["email"]!= self.current_user.email]
        save_json("data/users.json", users)
        print(f"Account {self.current_user.username} deleted!")
        self.current_user = None

    @admin_required
    def admin_menu(self):
        while self.current_user is not None:
            print("\nADMIN MENU")
            print("1. View Users")
            print("2. Delete User")
            print("3. Logout")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.view_users()
            elif choice == "2":
                self.delete_user_admin()
            elif choice == "3":
                self.logout()
            else:
                print("Invalid choice.")

    @admin_required
    def view_users(self):
        users = load_json("data/users.json")
        print("\nALL USERS")
        if not users:
            print("No users found.")
            return
        for user in users:
            print(f"- {user['username']} | {user['email']} | {user['role']}")

    @admin_required
    def delete_user_admin(self):
        email = input("Enter email of user to delete: ").strip()
        if email == self.current_user.email:
            print("You cannot delete yourself!")
            return
        users = load_json("data/users.json")
        original_len = len(users)
        users = [u for u in users if u["email"]!= email]
        if len(users) == original_len:
            print("User not found.")
        else:
            save_json("data/users.json", users)
            print(f"User {email} deleted!")

    @login_required
    def logout(self):
        print(f"Goodbye, {self.current_user.username}!")
        self.current_user = None

    def save_current_user(self):
        users = load_json("data/users.json")
        for index, user in enumerate(users):
            if user["email"] == self.current_user.email:
                users[index] = self.current_user.to_dict()
                break
        save_json("data/users.json", users)

if __name__ == "__main__":
    app = FitnessTracker()
    app.start()