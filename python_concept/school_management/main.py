from school import School
from person import Student, Teacher
from subject import Subject
from class_room import ClassRoom

school = School("ABC", "Dhaka")

eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")


school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)


# adding students:

rahim = Student("rahim", eight)
karim = Student("karim", nine)
fahim = Student("fahim", ten)
hamim = Student("hamim", ten)
borkot = Student("borkot", eight)


# student admission:
school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)
school.student_admission(borkot)


# adding teacher:

abul = Teacher("Abul")
babul = Teacher("Babul")
shafiq = Teacher("Shafiq")
rafiq = Teacher("rafiq")
salam = Teacher("Salam")


# adding subjects:
bangla = Subject("bangla", abul)
english = Subject("english", babul)
ict = Subject("ICT", shafiq)
math = Subject("math", rafiq)
history = Subject("history", salam)

eight.add_subject(bangla)
eight.add_subject(ict)
eight.add_subject(math)
nine.add_subject(english)
nine.add_subject(math)
nine.add_subject(ict)
nine.add_subject(history)
ten.add_subject(math)
ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(ict)


eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()


print(school)