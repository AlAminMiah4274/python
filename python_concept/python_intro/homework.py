# --------- float: -----------

# num = 45
# print(float(num))

# value = "457.36"
# print(float(value))

# num2 = "-185.3"
# print(float(num2))

# ---------- input: max ------------

# a, b, c = input().split()
# if a > b and a > c:
# 	print(a)
# elif b > c:
# 	print(b)
# else:
# 	print(c)


# --------- input: sum -----------
# a, b, c = input().split()

# a_int = int(a)
# b_int = int(b)
# c_int = int(c)

# sum = a_int + b_int + c_int

# print(sum)


# -------- print odd: --------- 

# num = 39
# while num < 68:
# 	num += 1

# 	if num % 2 == 0:
# 		continue

# 	print(num)

# -------- grade calculator: -------------

sub1, sub2, sub3, sub4, sub5 = input().split()
sub_1 = int(sub1)
sub_2 = int(sub2)
sub_3 = int(sub3)
sub_4 = int(sub4)
sub_5 = int(sub5)

avg = sub_1 + sub_2 + sub_3 + sub_4 + sub_5 / 5


if sub_1 >= 33 and sub_2 >= 33 and sub_3 >= 33 and sub_4 >= 33 and sub_5 >= 33:
	if avg >= 80:
		print("You got A+")
	elif avg >= 70 and avg <= 79:
		print("You got A")
	elif avg >= 60 and avg <= 69:
		print("You got A-")
	elif avg >= 50 and avg <= 59:
		print("You got B")
	elif avg >= 40 and avg <= 49:
		print("You got C")
	elif avg >= 33 and avg <= 39:
		print("You got D")
	else:
		print("You got F")
else:
	print("You got F")