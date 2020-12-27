

num_testcase = int(input())

#greedy algorithm: place the restaurant at the highest delivery location and sum everything
#notice that each number is a street CROSSING not a street, signifigance?

for i in range(num_testcase):
	cost = 0
	
	size_x, size_y = input().split()
	size_x = int(size_x)
	size_y = int(size_y)
	for j in range(size_y):
		#each list will be of size_x size
		deliveries_each_strt = input().split()
		deliveries_each_strt = [int(x) for x in deliveries_each_strt]
		#print(deliveries_each_strt) 

	print(cost, "blocks")
