class Student:

	def __init__(self, name, class_name, id):
		self.name = name
		self.class_name = class_name
		self.id = id


	def __repr__(self):
		return f"{self.name} and {self.class_name}"


class Teacher:

	def __init__(self, name, subject, id):
		self.name = name
		self.subject = subject 


	def __repr__(self):
		return f"{self.name} and {self.subject}"


class School:

	def __init__(self, name):
		self.name = name 
		self.teachers = []
		self.students = []

	def add_teacher(self, name, subject):
		id = len(self.teachers) + 1001
		teacher = Teacher(name, subject, id)
		self.teachers.append(teacher)


	def enroll(self, name, class_name, fee):
		if fee < 6500:
			return f"Fee not enough"
		else:
			id = len(self.students) + 1
			student = Student(name, class_name, id)
			self.students.append(student)

			return f"your enrollment done and extra {fee - 6500}"


	def __repr__(self):
		print(f"Welcome to {self.name}")
		print()
		print("------------- Our Teachers --------------")
		for teacher in self.teachers:
			print(teacher)

		print()
		print("------------- Our Students ---------------")
		for student in self.students:
			print(student)

		print()
		return f"Join here and enjoy"




# mia = Student("malkova", "doggy Style", 1001)
# print(mia)

phitron = School("phitron")
phitron.add_teacher("Van Disel", "C")
phitron.add_teacher("Tom Cruise", "C++")
phitron.add_teacher("Hamesworth", "DS")
phitron.add_teacher("Dulson", "Algorithm")
phitron.add_teacher("Gosling", "DS")
phitron.add_teacher("Lopez", "Algorithm")

phitron.enroll("De Arms", "DS", 7500)
phitron.enroll("lawrence", "C", 7500)
phitron.enroll("Herd", "Algorithm", 3500)
phitron.enroll("Jolly", "C++", 10000)
phitron.enroll("Gadot", "Algorithm", 9500)
phitron.enroll("Sweany", "C++", 8000)
phitron.enroll("Anna", "DS", 10500)

print(phitron)