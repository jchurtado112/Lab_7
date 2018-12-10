#Jesus Hurtado, Lab 7 Option A, CS 2302 Data Structures, Fall 2018
#Implement the dynamic-programming algorithm edit distance and test your results


# Method to edit matrix and get number of changes needed to convert one word to another one 
def edit_list(s1,s2):   
    l1 = len(s1)
    l2 = len(s2)
    matrix = []   # Creates an empty matrix
    
    for i in range(l2+1):   # Creates a 2D Matrix to perform "edit distance" algorithm and get number of changes
        matrix.append([0]*(l1+1))
        
    for j in range(l1+1):   # Horizontal first row is filled with numbers starting from 0-->length of string   
        matrix[0][j]=j
    for k in range(l2+1):   # Vertical first column is filled with numbers starting from 0-->length of string
        matrix[k][0]=k
    
    # Here 2D matrix will be filled by comparing first word with the second one
    for row in range(1,l2+1):
        for column in range(1,l1+1):
         #If condition is True, then assign value from previous column from previous row equal to current location
            if s2[row-1] == s1[column-1]: 
                matrix[row][column] = matrix[row-1][column-1]
         # Assign the minimum out of (previous-row and previous column, current row and previous column
         # , previous row and current column) + 1 to current location if the previous "if statement" is False
            else:
                matrix[row][column]=1+min(matrix[row-1][column],matrix[row][column-1],matrix[row-1][column-1])
    
    for line in range(len(s2)+1):   # Prints 2D Matrix
        print(matrix[line])
    
    print()
    # Prints as the result, the number of changes needed to convert word #1 to word #2
    print("Changes needed to convert '{}' word to '{}': {}".format(s1,s2,matrix[len(s2)-1][len(s1)-1]))
        
def read_file(file):  # Retrieve words from a file and store them into an array
    arr=[]
    f = open(file)
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','')
        arr.append(line)
    return arr
        
    
          
def main(): # Main method
    print()
    print("Reading file #1 with words that will be compared........")
    words = read_file("file_1.txt")   # Calls method to retrieve contents from 1st file
    print(words) # Prints array storing the words from 1st file
    print()
    string1 = words[0]
    string2 = words[1]
    edit_list(string1, string2)  #Calls method to get number of changes needed to convert word #1 to word #2
    
    print()
    
    print("Reading file #2 with words that will be compared........")
    words = read_file("file_2.txt")  # Calls method to retrieve contents from 2nd file
    print(words) # Prints array storing the words from 2nd file
    print()
    string1 = words[0]
    string2 = words[1]
    edit_list(string1, string2) # Calls method to get number of changes needed to convert word #1 to word #2
                    
                    
main()