class School:
    def __init__(self, name, year) -> None:
        self.name = name
        self.year = year
        self.students = []
        self.teachers = []
        self.staff = []

    def __repr__(self) -> str:
        return f"{self.name} is started from {self.year}"

    # add student function

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise ValueError("Student is not valid")


class User:
    def __init__(self, name, email, phone, location) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.location = location


class Student(User):
    def __init__(self, name, email, phone, location, age, roll, id, current_class) -> None:
        self.roll = roll
        self.age = age
        self.current_class = current_class
        self.id = id
        super().__init__(name, email, phone, location)



sundoli = School("Sundoli", 1998)

tamal = Student("tamal", "tamal@gmail.com", "012", "bd", 23, 12, 1, 12)

sundoli.add_student(tamal)

    
