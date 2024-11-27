# numbers = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61, 70]
# odds = []

# for num in numbers:
# 	if num % 2 == 1 and num % 5 == 0:
# 		odds.append(num)

# # print(odds)

# odds_num = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
# # print(odds_num)


players = ["Messi", "Lautaro", "Alvarez"]
ages = [38, 29, 24]

# for player in players:
# 	print("Player:", player)
# 	for age in ages:
# 		print("Age:", age)


player_age_combination = [(player, age) for player in players for age in ages]
print(player_age_combination)



# -------- quizes ----------

# def display_person(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")


# display_person(Name="Amir Khan", Age="45")

# numbers =[7,6,5,3,3,2,1]
# print(numbers[-4])

# numbers =[7,8,5,4,3,2,4]
# print(numbers[::-1])