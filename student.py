from user import User


class Student(User):
    def __init__(self, name, email, phone, location, age, roll, id, current_class) -> None:
        self.roll = roll
        self.age = age
        self.current_class = current_class
        self.id = id
        super().__init__(name, email, phone, location)
