from random import randint


class Exam:

	def __init__(self, student_name):
		self.student_name = student_name
		self.marks = 0


	def attend_to_exam(self, exam_name):
		print("Thanks for attending to the exam")


	def get_marks(self):
		self.marks = randint(70, 100)



# print(randint(1, 10))
sakib = Exam("Math")
print(sakib.get_marks())