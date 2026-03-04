class Matrix:
    def __init__(self, value): 
        self.value = value
        self.rows, self.columns = rows_columns(self.value)
        
    
    def __mul__(self,other):
        if not(isinstance(other, Matrix)):
            raise ValueError('Other value being multipled must be a matrix')
        else: 
            return Matrix(multiply(self.value, other.value))
    
    def __str__(self):
        return print_matrix(self.value)
        

    @property
    def value(self):
        return self.__value
    

    @value.setter
    def value(self, new_value):
        if isinstance(new_value,str):
            new_value = matrix_converter(new_value)

        if not(valid(new_value)):
            raise ValueError("Given nested list is not a matrix")
        else:
            self.__value = new_value
    
    
def main():
    # input a matrix
    user_input_1 = input("> ")
    matrix1 = Matrix(user_input_1)
    print(matrix1)


# function to convert a matrix as a string into a list 
def matrix_converter(input: str) -> list:
    # removes the blank spaces around the inputed string 
    input = input.strip(" ")
    # removes the "[[" and "]]" at the start of the input
    input = input.strip("[")
    input = input.strip("]")

    # splits the string based on wether the user has used ][ or ],[ to seperate each row 
    if '],[' in input:
        input = input.split('],[')
    elif '][' in input:
        input = input.split('][')
    else:
        raise ValueError("Incorrect format, input can not be converted into a nested list")
    
    matrix = []

    # goes through each element in input with is a string of 'num_1,num_2, ...'
    # splits it into a list, converts each element into an int and adds it as a sublist to the matrix

    for row in input: 
        # list operator used to convert each element x from row.split(',') into an int
        row = [int(x) for x in row.split(',')]
        matrix.append(row)

    return matrix


# function to validate if a nested list is a valid matrix 
def valid(input: list) -> bool:
    # check if the given input is a list of a list 
    if not(isinstance(input,list)):
        return False
    # we can check if the number of element in each row is equal 
    # num of elements in the first row 
    num_elements = len(input[0])
    
    # goes through each row 
    for row in input:
        # if the number of elements in that row is not equal to the number of elements 
        # in the first row then return false 
        if len(row) != num_elements:
            return False 
    
    return True


# function to return the number of rows and columns of a given matrix 
def rows_columns(input: list) -> tuple[int,int]:

    if not(valid(input)):
        raise ValueError("the given matrix is not valid, can not calculate the number of rows a columns")
    
    rows = 0
    for _ in input:
        rows += 1
    
    columns = 0
    for _ in input[0]:
        columns += 1

    return rows,columns


# function that checks weather two matrices can be multipled or not 
def can_multiply(input_1: list, input_2: list) -> bool:

    _, column_1 = rows_columns(input_1)
    rows_2, _ = rows_columns(input_2)

    # the the number of columns in the first matrix is equal to the number or rows in the second, 
    # both matrices can be multipled with one another 
    if column_1 != rows_2:
        return False 
    else:
        return True 

def multiply(input_1: list[list[int]], input_2: list[list[int]]) -> list:

    if not(can_multiply(input_1,input_2)):
        raise ValueError("Error the two given matrices can not be multiplied")

    rows_a = len(input_1)
    cols_a = len(input_1[0])
    cols_b = len(input_2[0])

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += int(input_1[i][k]) * int(input_2[k][j])
    
    return result
                

# outputs the matrix as a block
def print_matrix(input: list) -> str:

    output = ''
    num_rows = len(input)
    i = 0
    for row in input:
        i += 1
        for element in row:
            output += str(element) + ' '
        if i < num_rows:
            output += "\n"
    
    return(output)




if __name__ == "__main__":
    main()