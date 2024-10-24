class User:
    user_counter = 0

    def __init__(self, name: str, surname: str, phone: str = "", email: str = ""):
        self.id = User.user_counter
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

        User.user_counter += 1

    def __repr__(self):
        return f"(id: {self.id},name: {self.name}, surname: {self.surname})"