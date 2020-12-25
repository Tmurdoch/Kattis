

n = int(input())
m = int(input())

each_room = m // n
left_over = m - (each_room * n)

for i in range(n):
	if left_over == 0:
		print("*"*each_room)
	else:
		print("*"*(each_room+1))
		left_over -= 1
