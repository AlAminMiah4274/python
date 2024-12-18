class ClassRoom:
	def __init__(self, class_name):
		self.class_name = class_name
		self.students = []	# list of student objects
		self.subjects = []	# list of subject objects


	def add_student(self, student):
		roll_no = f"{self.class_name} - {len(self.students) + 1}"	# eight - 1
		student.id = roll_no
		self.students.append(student)


	def add_subject(self, subject):
		self.subjects.append(subject)


	def take_semester_final_exam(self):
		for subject in self.subjects:
			subject.exam(self.students)

		for student in self.students:
			student.calculate_final_grade()