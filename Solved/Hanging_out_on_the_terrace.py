

fire_safety_limit, num_events = input().split()

fire_safety_limit = int(fire_safety_limit)
num_events = int(num_events)

cur_in = 0
count = 0

for i in range(num_events):
	new_enter, entering = input().split()
	entering = int(entering)
	if new_enter[0] == 'e':

		if entering + cur_in > fire_safety_limit:
			count += 1
		else:
			cur_in += entering
	else:
		cur_in -= entering

print(count)
