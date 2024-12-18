class School:
	def __init__(self, name, address):
		self.name = name
		self.address = address
		self.teachers = {}	# {"english": teacher object}
		self.classrooms = {}	# {"ten": student object}


	def add_classroom(self, classroom):
		self.classrooms[classroom.class_name] = classroom


	def add_teacher(self, subject, teacher):
		self.teachers[subject] = teacher


	def student_admission(self, student):
		admitted_class = student.classroom.class_name
		self.classrooms[admitted_class].add_student(student)


	@staticmethod
	def calculate_grade(marks):
		if marks >= 80 and marks < 100:
			return "A+"
		elif marks >= 70 and marks < 80:
			return "A"
		elif marks >= 60 and marks < 70:
			return "A-"
		elif marks >= 50 and marks < 60:
			return "B"
		elif marks >= 40 and marks < 50:
			return "C"
		elif marks >= 33 and marks < 40:
			return "D"
		else:
			return "F"


	@staticmethod
	def grade_to_value(grade):
		grade_map = {
			"A+": 5.00,
			"A": 4.00,
			"A-": 3.50,
			"B": 3.00,
			"C": 2.00,
			"D": 1.00,
			"F": 0.00
		}

		return grade_map[grade]


	@staticmethod
	def value_to_grade(value):
		if value >= 4.50 and value < 5.00:
			return "A+"
		elif value >= 3.50 and value < 4.50:
			return "A"
		elif value >= 3.00 and value < 3.50:
			return "A-"
		elif value >= 2.50 and value < 3.00:
			return "B"
		elif value >= 2.00 and value < 2.50:
			return "C"
		elif value >= 1.00 and value < 2.00:
			return "D"
		else:
			return "F"


	def __repr__(self):
		# all calssrooms
		print("ALL CLASSROOMS : ")
		for key in self.classrooms.keys():
			print(key)

		print("\n")

		# all students
		print("ALL STUDENTS : ")
		result = ""
		for key, value in self.classrooms.items():
			result += f"----{key.upper()} classroom students\n"

			for student in value.students:
				result += f"{student.name}\n"
		
		print(result, "\n")

		
		# all subjects
		print("ALL SUBJECTS : ")
		subject = ""
		for key, value in self.classrooms.items():
			subject += f"----{key.upper()} classroom's subjects\n"

			for sub in value.subjects:
				subject += f"{sub.subject_name}\n"

		print(subject, "\n")
		

		# all teachers - HOMEWORK ----> 
		print("ALL TEACHERS : ")
		print(len(self.teachers))

		# all student results
		print("ALL STUDENT'S RESULT : ")
		for key, value in self.classrooms.items():
			for student in value.students:
				for k, v in student.subject_marks.items():
					print(student.name, k, v, student.subject_grade[k])
				print(student.calculate_final_grade(), "\n")
		

		return ""
