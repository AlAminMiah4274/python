from person import Teacher
from school import School


class Subject:
	def __init__(self, subject_name, subject_teacher):
		self.subject_name = subject_name
		self.subject_teacher = subject_teacher
		self.max_marks = 100
		self.pass_marks = 33


	def exam(self, students):
		for student in students:
			mark = self.subject_teacher.evaluate_exam()
			student.subject_marks[self.subject_name] = mark 
			student.subject_grade[self.subject_name] = School.calculate_grade(mark)

