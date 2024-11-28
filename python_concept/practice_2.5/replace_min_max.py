n = int(input())

nums = []
for i in range(n):
	x = int(input())

	nums.append(x)


max_value = max(nums)
min_value = min(nums)


for key, value in enumerate(nums):
	if value == max_value:
		nums[key] = min_value

	if value == min_value:
		nums[key] = max_value

print(nums)