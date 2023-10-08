from student import Student
from teacher import Teacher


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
            print("Student added successfull")
        else:
            raise ValueError("Student is not valid")

    # add student function

    def add_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.teachers.append(teacher)
            print("Teacher added successfull")
        else:
            raise ValueError("Teacher is not valid")


sundoli = School("Sundoli", 1998)
somir = Teacher("Somir", 'somir@gmail.com', "4539", "Sundorli", "Math", 45)
tamal = Student("tamal", "tamal@gmail.com", "012", "bd", 23, 12, 1, 12)

sundoli.add_student(tamal)
sundoli.add_teacher(somir)
