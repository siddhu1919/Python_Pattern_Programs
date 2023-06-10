# Number Pyramid Pattern 3
# Inverted Number Pyramid Pattern
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

def invertedNumPyramid(rows):
	temp = 0
	for row in  reversed(range(1,rows+1)):
		temp+=1 
		for num in range(1,row+1):
			print(temp,end=" ")
		print()
		
invertedNumPyramid(5)