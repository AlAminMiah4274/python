import random
from school import School


class Person:
	def __init__(self, name):
		self.name = name




class Teacher(Person):
	def __init__(self, name):
		super().__init__(name)


	def evaluate_exam(self):
		return random.randint(0, 100)



class Student(Person):
	def __init__(self, name, classroom):
		super().__init__(name)
		self.classroom = classroom
		self.__id = None
		self.subject_marks = {}  # {"math": 85, "ICT": 82}
		self.subject_grade = {}  # {"eng": "A+", "history": "A"}
		self.grade = None  # final grade 


	def calculate_final_grade(self):
		sum = 0
		for grade in self.subject_grade.values():
			point = School.grade_to_value(grade)	# 5.00
			sum += point

		if sum == 0:
			gpa = 0.00
			self.grade = "F"
			return f"{self.name}'s' Final grade: {self.grade} with GPA = {gpa}"
		else:
			gpa = sum / len(self.subject_grade)		# 7/3 = 3.50
			self.grade = School.value_to_grade(gpa)

			return f"{self.name}'s' Final grade: {self.grade} with GPA = {gpa}"


	# rahim.id ==
	@property
	def id(self):
		return self.__id


	# rahim.id == 12
	@id.setter
	def id(self, value):
		self.__id = value