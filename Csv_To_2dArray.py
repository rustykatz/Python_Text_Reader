# Running on Python 3
# Made by: Russell Wong 

import csv

def Csv_To_2dArray(filename):

	Data_Array = []
	
	# Opens the file and reads it
	with open(filename, 'r') as Csv_File:

		# Here we set the delimiter, this is the character that separates
		# the data entries 
		Data_Reader = csv.reader(Csv_File, delimiter = " ")


		# Takes each line in the csv file and makes it into an array
		# The array is then added to our Data_Array 
		# Data_Array is a 2d array, with the following parameters [Row][Column]
		for row in Data_Reader:
			Data_Array.append(row)


	# Returns our Data_Array so we can use it	
	return(Data_Array)


# Simple function that takes our Array and prints it out 
def Print_Array(Array):
	print(Array)

# Simple Function that chooses which array to focus on from our 
# Data_Array.
def Select_Array(Data_Array, Array_Wanted):
	Selected = []
	Selected = Data_Array[Array_Wanted]
	return(Selected)


def Add_Back_Array(Array, Item):
	Added_Back = Array + [Item]
	return(Added_Back)

#def Add_Front_array(Data_Array):



def main():
	print("Begin Executing...\n")
	File_Name = "txt_test.txt"

	# Prints out our Data Array
	print("Printing our Data Array: ")
	Data_Array = Csv_To_2dArray(File_Name)
	Print_Array(Data_Array)
	print("\n")

	# Let's Select 1 of the arrays to work with
	print("Printing Selected Array: ")
	Array_Wanted = 1
	print("Selected array: " + str(Array_Wanted) + "\n")
	Selected = Select_Array(Data_Array, Array_Wanted)
	Print_Array(Selected)
	print("\n")


	# Let's try adding something to the back of our Array

	# 1) Adding a whole array to our Data_Array
	print("Adding An Array to Data_Array: \n")
	New_Arr = [45,50,55,60]
	Added_Back = Add_Back_Array(Data_Array, New_Arr)
	Print_Array(Added_Back)
	print("\n")

	# 2) Adding an item to an end of a selected Array
	# print("Adding item to end of Data_Array: \n")
	# new_item = 67
	# print("item is: " + str(new_item))
	# print("Array selected is: " + str(Selected))
	# Item_Added_Back = Add_Back_Array(Selected, new_item)
	# Print_Array(Item_Added_Back)
	# print("\n")


	# Let's try adding somethignto the Front of our Array










	print("Executing Complete.\n")
main()