a, b = input().split()

# print(a[::-1])
# print(b[::-1])
a_int = int(a)
b_int = int(b)


lucky_nums = []
while a_int <= b_int:
	a_str = str(a_int)
	if a_str.find('4') == 1 or a_str.find('7') == 1:
		lucky_nums.append(a_str)

	a_int += 1


print(lucky_nums)

# Input: Two numbers A and B
A, B = map(int, input().split())


def is_lucky(number):
    return all(char in '47' for char in str(number))


lucky_numbers = [number for number in range(A, B + 1) if is_lucky(number)]


if lucky_numbers:
    print(" ".join(map(str, lucky_numbers)))
else:
    print(-1)
