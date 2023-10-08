from user import User


class Teacher(User):
    def __init__(self, name, email, phone, location, subject, age) -> None:
        self.subject = subject
        self.age = age
        super().__init__(name, email, phone, location)
