""" 
.csv  ----> comma separated value
.txt  ------> text file 
"""


# with open("message.txt", "w") as file:
# 	file.write("I am the best software engineer \n")


# with open("message.txt", "a") as file:
# 	file.write("I can solve any programming problem \n")


with open("message.txt", "r") as file:
	text = file.read()
	print(text)