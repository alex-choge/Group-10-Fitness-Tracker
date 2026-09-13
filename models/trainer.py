from .user import User

class Trainer(User):
    def __init__(self, name, email_or_spec, password_hash="1234", specialization=None):
        if specialization is None:
            actual_spec = email_or_spec
            email = f"{name.lower()}@gmail.com"
        else:
            actual_spec = specialization
            email = email_or_spec

        super().__init__(name, email, password_hash, age=25, weight=70, height=175)
        
        self.specialization = actual_spec 
        self.clients = []

    def add_client(self, client_name):
        self.clients.append(client_name)
        print(f"{client_name} added to {self.username}")

    def show_clients(self):
        print(f"Trainer {self.username} has clients: {self.clients}")
        return self.clients

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "specialization": self.specialization,
            "clients": self.clients
        }
