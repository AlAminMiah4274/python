import pyautogui

n = int(input())

hash_char = 1
space = n - 1

for i in range(n):
	for i in range(hash_char):
		# print("#", end = "")
		pyautogui.write("#")

	for i in range(space):
		# print(" ", end = "")
		pyautogui.write(" ")

	# print()
	pyautogui.press("enter")
	hash_char += 1
	space -= 1


