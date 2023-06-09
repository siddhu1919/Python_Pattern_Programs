#Python Pattern Program: Left Pyramid

def leftPyramid(rows):
	for i in range(0,rows):
		for j in range(0 ,i+1):
			print(" * ",end = " ")
		print("\n")
		
		
leftPyramid(4)