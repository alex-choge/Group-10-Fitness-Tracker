import hashlib

class User:

    def __init__(
        self,
        username,
        email,
        password,
        age,
        weight,
        height,
        role="user",
        password_is_hashed=False
    ):
        self.username = username
        self.email = email

  
        if password_is_hashed:
            self.__password = password
        else:
            self.__password = self.hash_password(password)

        self.age = age
        self.weight = weight
        self.height = height
        self.role = role

        self.workouts = []
        self.goals = []
        self.trainer = None

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.__password == self.hash_password(password)

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = self.hash_password(new_password)

    def add_workout(self, workout):
        self.workouts.append(workout)
        print("Workout added!")

    def remove_workout(self, workout):
        if workout in self.workouts:
            self.workouts.remove(workout)
            print("Workout removed!")

    def add_goal(self, goal):
        self.goals.append(goal)
        print("Goal added!")

    def view_workouts(self):
        print(f"My workouts for {self.username}:")
        for w in self.workouts:
            print(f"- {w}")

    def view_goals(self):
        print(f"My goals for {self.username}:")
        for g in self.goals:
            print(f"- {g.title}: {g.description} [{g.status}]")

    def update_weight(self, new_weight):
        self.weight = new_weight
        print(f"New weight is {new_weight}")

    def set_trainer(self, trainer_name):
        self.trainer = trainer_name
        print(f"My trainer is {trainer_name}")

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password_hash": self.__password,
            "age": self.age,
            "weight": self.weight,
            "height": self.height,
            "role": self.role,
            "workouts": self.workouts,
            "goals": [g.to_dict() for g in self.goals]
        }

