# n = int(input())
# arr = input().split()

# print(arr)

""" Way 1 """

# for i in range(len(arr)):
# 	arr[i] = int(arr[i])

# print(arr)

""" Way 2 """

# int_arr = [int(i) for i in arr]

# print(int_arr)

""" Way 3 """

# def convert_int(n):
# 	return int(n)

# int_arr = list(map(convert_int, arr))
# print(int_arr)


""" input array in one line """
arr_input = list(map(int, input().split()))
print(arr_input)