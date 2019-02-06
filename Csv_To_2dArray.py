# Running on Python 3
# Made by: Russell Wong 
# Purpose: Quick refresher to help get back into any type of python programming  
import csv

def Csv_To_2dArray(filename):

	Data_Array = []
	
	# Opens the file and reads it
	with open(filename, 'r') as Csv_File:

		# Set the delimiter
		Data_Reader = csv.reader(Csv_File, delimiter = " ")

		# Takes each line in the csv file and makes it into an array
		# The array is then added to our Data_Array 
		# Data_Array is a 2d array, with the following parameters [Row][Column]
		for row in Data_Reader:
			Data_Array.append(row)

	# Returns our Data_Array so we can use it	
	return(Data_Array)

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
def Select_array(Array, Row):
	Selected = []
	Selected = Array[Row]
	return(Selected)

# ~~~~~~~~~~ Methods ~~~~~~~~~~
# - Append: Adds element to end of list.
#			i.e. array.append('val')
# - Extend: Adds list to another
#			i.e. a.extend(y) will add all elements of y to a
# - Insert: Inserts element into specific positon
#			i.e. insert(index_to_insert_behind, element)

# ~~~~~~~~~~ Sorting ~~~~~~~~~~
# - sort(): Sorts in Ascending order
# - can pass it (reverse=True) To sort in Descending Order
# - Can pass it key (key=fxn) To sort based on key 


def main():
	print("Begin Executing...\n")
	File_Name = "txt_test.txt"

	# Prints out our Array
	arr = Csv_To_2dArray(File_Name)
	print("Our Array: \n")
	P_array(arr)
	print("\n")

	# Let's Select 1 of the arrays to work with
	arr_index = 1
	Selected = Select_array(arr, arr_index)
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
	print(arr[0][0] + "+" + arr[2][1] + "=" + str(int(arr[0][0]) + int(arr[2][1])))
	print("\n")

	print("Executing Complete.\n")

main()