file1 = input("Enter full name of first file: ")
file2 = input("Enter full name of second file: ")


def swapFileData(file1, file2):

	with open(file1) as a :
		data_a = a.read()
		
	with open(file2) as b :
		data_b = b.read()	

	with open(file1, "w") as a :
		 a.write(data_b)
		 
	with open(file2, "w") as b :
		 b.write(data_a)
	 
swapFileData(file1, file2)
print("Files successfully swapped")