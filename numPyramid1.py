#Python Number Pattern Program
#       1  
#       2 2  
#       3 3 3  
#       4 4 4 4  
#       5 5 5 5 5


def Num_pattern(rows):
	for row in range(1,rows+1):
		for num in range(1,row+1):
			print(row, end=" ")
		print()
			
Num_pattern(5)