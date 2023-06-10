# Number Pyramid Pattern 4
# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1




def invertedNumPyramid2(rows):
	for row in  reversed(range(1,rows+1)):		
		for num in range(0,row+1):
			print(num,end=" ")
		print()
		
invertedNumPyramid2(5)