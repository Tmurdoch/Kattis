

num_testcase = int(input())

#greedy algorithm: place the restaurant at the highest delivery location and sum everything
#notice that each number is a street CROSSING not a street, signifigance -> weighted graph
#all pairs shortest path



def compute_distance_from(source, dest):
	#source and destinations are indexes
	#cost = x + y * # of deliveries
	#x_distance
	#y_distance
	x_distance = abs(source[0] - dest[0])
	y_distance = abs(source[1] - dest[1])
	return (x_distance + y_distance) * deliveries[dest[0]][dest[1]]

deliveries = []
for i in range(num_testcase):
	cost = 0
	
	size_x, size_y = input().split()
	size_x = int(size_x)
	size_y = int(size_y)

	for j in range(size_y):
		#each list will be of size_x size
		deliveries_each_strt = input().split()
		deliveries_each_strt = [int(x) for x in deliveries_each_strt]
		deliveries.append(deliveries_each_strt)
		#print(deliveries_each_strt)

	temp_cost = cost
	for source_x in range(len(deliveries)-1):
		for source_y in range(len(deliveries[source_x])-1):
			for row in range(size_y):
				for col in range(size_x):
					temp_cost += compute_distance_from((source_x, source_y), (row, col))
			if temp_cost < cost:
				cost = temp_cost

	print(cost, "blocks")






