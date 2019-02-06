# Running on Python 3
# Made by: Russell Wong 
# Purpose: Quick refresher to help get back into any type of python programming  
import csv

def Csv_To_2dArray(filename):

	Data_Matrix = []
	
	# Opens the file and reads it
	with open(filename, 'r') as Csv_File:

		# Set the delimiter
		Data_Reader = csv.reader(Csv_File, delimiter = " ")

		# Takes each line in the csv file and makes it into an array
		# The array is then added to our Data_Matrix
		# Data_Matrix is a 2d array, with the following parameters [Row][Column]
		for row in Data_Reader:
			Data_Matrix.append(row)

	# Returns our Data_Matrix so we can use it	
	return(Data_Matrix)

# ~~~~~~~~~~ Printing functions ~~~~~~~~~~

# Whole array
def P_array(Array):
	print(Array)

# Specific element 
def P_element(i, Array):
	print(Array[i])

# Specific range of element
def P_range(i,k, Array):
	print(Array[i:k])

# ~~~~~~~~~~ Select Row ~~~~~~~~~~  
def Select_array(Matrix, Row):
	Selected = []
	Selected = Matrix[Row]
	return(Selected)

# ~~~~~~~~~~ Methods ~~~~~~~~~~
# - Append: Adds element to end of array.
#			i.e. array.append('val')
# - Extend: Adds array to another
#			i.e. a.extend(y) will add all elements of y to a
# - Insert: Inserts element into specific positon
#			i.e. insert(index_to_insert_behind, element)

# ~~~~~~~~~~ Sorting ~~~~~~~~~~
# - sort(): Sorts in Ascending order
# - can pass it (reverse=True) To sort in Descending Order
# - Can pass it key (key=fxn) To sort based on key 


def main():
	print("Now Executing...\n")
	File_Name = "txt_test.txt"

	# Prints out our Matrix
	Matrix = Csv_To_2dArray(File_Name)
	print("Matrix: \n")
	P_array(Matrix)
	print("\n")

	# Let's Select 1 of the arrays to work with
	arr_index = 1
	Selected = Select_array(Matrix, arr_index)
	print("Selected array: Index->" + str(arr_index) + "\n")
	P_array(Selected)
	print("\n")

	# Sorting array 
	Selected.sort()
	print("Sorting: ")
	P_array(Selected)
	print("\n")

	# Reversing sorted array
	print("Reversing Sorting: ")
	Selected.sort(reverse=True)
	P_array(Selected)
	print("\n")

	# Adding two items in matrix
	print("Adding (0,0) and (2,1): ")
	print(Matrix[0][0] + "+" + Matrix[2][1] + "=" + str(int(Matrix[0][0]) + int(Matrix[2][1])))
	print("\n")

	print("Executing Complete.\n")

main()