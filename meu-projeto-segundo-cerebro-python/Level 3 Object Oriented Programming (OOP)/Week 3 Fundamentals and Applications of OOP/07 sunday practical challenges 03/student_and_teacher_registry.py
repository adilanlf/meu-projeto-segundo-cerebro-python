# Student and Teacher Registry – OOP, Inheritance, Encapsulation

# Base class for all people
class Person:
    def __init__(self, name, age):         # Constructor method
        self._name = name                  # Private attribute: name
        self._age = age                    # Private attribute: age

    @property
    def name(self):                        # Getter for name
        return self._name

    @property
    def age(self):                         # Getter for age
        return self._age

# Subclass for students
class Student(Person):
    def __init__(self, name, age, grade):  # Constructor for Student
        super().__init__(name, age)        # Call the parent constructor
        self.grade = grade                 # Public attribute: grade

# Subclass for teachers
class Teacher(Person):
    def __init__(self, name, age, subject):  # Constructor for Teacher
        super().__init__(name, age)          # Call the parent constructor
        self.subject = subject               # Public attribute: subject

# Create a student and a teacher
s1 = Student("Anna", 20, "10th Grade")       # Instance of Student
t1 = Teacher("Mr. Smith", 40, "Math")        # Instance of Teacher

# Print their information
print(f"Student: {s1.name}, Age: {s1.age}, Grade: {s1.grade}")
print(f"Teacher: {t1.name}, Age: {t1.age}, Subject: {t1.subject}")

# Output:
# Student: Anna, Age: 20, Grade: 10th Grade
# Teacher: Mr. Smith, Age: 40, Subject: Math