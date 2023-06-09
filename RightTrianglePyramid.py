##Python Pattern Program: Right Triangle Pyramid
row =5

for i in range(0,row ):
	for space in range(0,(row - i)):
		print(" ",end="")
	for j in range(0,i):
		print("*", end="")
	print()
	
	
	