from person import Teacher
from school import School


class Subject:
	def __init__(self, subject_name, teacher_name):
		self.subject_name = subject_name
		self.teacher_name = teacher_name
		self.max_marks = 100
		self.pass_marks = 33


	def exam(self, students):
		for student in students:
			mark = self.Teacher.evaluate_exam()
			student.student_marks[self.subject_name] = mark
			student.student_grade[self.subject_name] = self.School.calculate_grade(mark)