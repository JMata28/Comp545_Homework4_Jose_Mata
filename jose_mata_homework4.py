#This is Jose Mata's submission for COMP 545 - Analysis of Algorithms, Homework 4 
#Fall 2024 - Bridgewater State University 

#To run this python file: 
#Run using the latest Python version or Python 3.12.2 64-bit
#Run from command line or from Visual Studio Code 
#The program will sort and display the numbers hardcoded into the program in the list "unsorted_numbers"
#from least to greatest, using Radix sort and count sort. 

#This project is fully completed and no features of it were left undone. 

#This function performs the counting sort. It takes an unsorted list of tuples and then returns the sorted list based on the
#second value (index 1) of the tuple.
def count_sort(unsorted_list_of_tuples):
    #Create an array with the digits
    unsorted_array_of_digits = []
    for pair in unsorted_list_of_tuples:
        unsorted_array_of_digits.append(pair[1])

    #Count how many instances of each digit are in the array
    counter_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(10):
        count = unsorted_array_of_digits.count(x)
        counter_array[x]= count
    
    #Include in the index of an array the sum of all the values of the indexes before it
    counter_array2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter_array2[0]= counter_array[0]
    for y in range(1, 10):
        counter_array2[y] = counter_array2[y-1]+counter_array[y]
    
    #Shift counter array 2 to the right by one index 
    counter_array3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter_array3[0]=0
    counter_array3[1:10] = counter_array2[0:9]
    
    #sort the digits using counter_array3
    sorted_array_of_digits = [0]*len(unsorted_array_of_digits)
    for digit in unsorted_array_of_digits:
        sorted_array_of_digits[counter_array3[digit]] = digit
        counter_array3[digit] = counter_array3[digit]+1 
    
    #organize the list of tuples based on the sorted digits
    sorted_list_of_tuples = []
    for number in sorted_array_of_digits:
        for pair in unsorted_list_of_tuples:
            if pair[1] == number:
                sorted_list_of_tuples.append(pair)
                unsorted_list_of_tuples.remove(pair)
                break
    return sorted_list_of_tuples


#Define the list with the numbers that will be sorted. These numbers are purposely unsorted in this list. 
unsorted_numbers = [85, 32, 56, 90, 7, 10, 23, 12, 99, 44]

#Turn the list of numbers to a list of strings. Since we assume that the largest numbers will have up to 
#4 digits, we add the necessary number of zeroes to the left of the number depending on its number of 
#digits (its lenght). This allows for easier handling of the digits in this program for comparison purposes.
unsorted_strings = []
for number in unsorted_numbers:
    number_as_string = str(number)
    if len(number_as_string) == 1:
        number_as_string = '000' + number_as_string
    elif len(number_as_string) == 2:
        number_as_string = '00' + number_as_string
    elif len(number_as_string) == 3:
        number_as_string = '0' + number_as_string
    unsorted_strings.append(number_as_string)

#Create a list of tuples. The first value in the tuple (index 0) has the number and the second value of the tuple (index 1)
#has the least significant digit (LSD) of the number. The purpose of the tuples is to keep the LSD associated with the 
#number that it came from. 
unsorted_list_of_tuples_lsd =[]
for number in unsorted_strings:
    unsorted_list_of_tuples_lsd.append((number, int(number[-1])))  
sorted_list_of_tuples_lsd = count_sort(unsorted_list_of_tuples_lsd) #Sort in increasing order by the LSD
print("The list of pairs of numbers sorted sorted by LSD and the number's LSD is: " + str(sorted_list_of_tuples_lsd))

#Create a list of tuples. The first value in the tuple (index 0) has the number and the second value of the tuple (index 1)
#has the second least significant digit (LSD) of the number. The purpose of the tuples is to keep the second LSD associated with the 
#number that it came from. 
unsorted_list_of_tuples_2lsd = []
for pair in sorted_list_of_tuples_lsd:
    unsorted_list_of_tuples_2lsd.append((pair[0], int(pair[0][-2])))
sorted_list_of_tuples_2lsd = count_sort(unsorted_list_of_tuples_2lsd) #Sort in increasing order by the second LSD
print("The list of pairs of numbers sorted by second LSD and the number's second LSD is: " + str(sorted_list_of_tuples_2lsd))

#Create a list of tuples. The first value in the tuple (index 0) has the number and the second value of the tuple (index 1)
#has the third least significant digit (LSD) of the number. The purpose of the tuples is to keep the third LSD associated with the 
#number that it came from. 
unsorted_list_of_tuples_3lsd = []
for pair in sorted_list_of_tuples_2lsd:
    unsorted_list_of_tuples_3lsd.append((pair[0], int(pair[0][-3])))
sorted_list_of_tuples_3lsd = count_sort(unsorted_list_of_tuples_3lsd) #Sort in increasing order by the third LSD
print("The list of pairs of numbers sorted by third LSD and the number's third LSD is:  " + str(sorted_list_of_tuples_3lsd))

#Create a list of tuples. The first value in the tuple (index 0) has the number and the second value of the tuple (index 1)
#has the fourth least significant digit (LSD) of the number. The purpose of the tuples is to keep the fourth LSD associated with the 
#number that it came from. 
unsorted_list_of_tuples_4lsd = []
for pair in sorted_list_of_tuples_3lsd:
    unsorted_list_of_tuples_4lsd.append((pair[0], int(pair[0][-4])))
sorted_list_of_tuples_4lsd = count_sort(unsorted_list_of_tuples_4lsd) #Sort in increasing order by the fourth LSD
print("The list of pairs of numbers sorted by fourth LSD and the number's fourth LSD is:  " + str(sorted_list_of_tuples_4lsd))

#Extract only the numbers from the tuples and put them into the final list of numbers already sorted by the fourth LSD.
final_sorted_list = []
for element in sorted_list_of_tuples_4lsd:
    final_sorted_list.append(int(element[0])) #the 'int' method converts the numbers from strings back to integers 
print("The final list of sorted numbers is: " + str(final_sorted_list))




