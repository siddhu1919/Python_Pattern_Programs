# Pyramid pattern of numbers
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

def numPyramid(rows):
	for row in range(1,rows+1):
		for num in range(1,row+1):
			print(num ,end=" ")
		print() 
		
numPyramid(5)