def get_matrix(text=''):    
    n, m = [int(i) for i in input(f'Enter size of{text} matrix:').split()]
    matrix = []
    print(f'Enter{text} matrix:')
    for i in range(n):
        row = [float(i) for i in input().split()]
        matrix.append([])
        for j in range(m):
            matrix[i].append(row[j])
    return matrix

def print_matrix(matrix):
    print('The result is:')
    for i in range(len(matrix)):
        
        print(' '.join(["{:.3f}".format(num) for num in matrix[i]]))
        
def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    output = []
    for i in range(n):
        output.append([])
        for j in range(m):
            output[i].append(matrix[j][i])
    return output
    
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]                    
    else:
        output = 0
        for i in range(len(matrix)):
            sign = 1
            if i % 2 == 1:
                sign = -1
            output += sign *  matrix[i][0] * determinant(minor(matrix, i, 0)) 
        return output

def minor(matrix, n, m):
    minor = [] 
    skip = 0
    for i in range( len(matrix)):
        if i != n:
            minor.append([])
            for j in range(len(matrix[0])):
                if j != m:
                    minor[i - skip].append(matrix[i][j])
        else:
            skip = 1
    return minor
    
def multiply_by_const(matrix, const):
    output = []
    for i in range(len(matrix)):
        output.append([num * const for num in matrix[i]])
    return output
    
choice = ''

while choice != '0':
    print('''
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    choice = input('Your choice:')
    # Add matrices
    if choice == '1':
        matrix1 = get_matrix(' first')
        matrix2 = get_matrix(' second')
        n1 = len(matrix1)
        m1 = len(matrix1[0])
        n2 = len(matrix2)
        m2 = len(matrix2[0])
        if n2 != n1 or m2 != m1:
            print('ERROR')
        else:
            output = []
            print('The result is:')
            
            for i in range(n1):
                output.append([])
                for j in range(m1):
                    output[i].append(matrix1[i][j] + matrix2[i][j])         
            print_matrix(output)

    # Multiply matrix by a constant
    elif choice == '2':
        matrix = get_matrix()
        scalar = int(input())
        print('The result is:')
        matrix = multiply_by_const(matrix, scalar)
        print_matrix(matrix)

    # Multiply matrices   
    elif choice == '3':
        matrix1 = get_matrix(' first')
        matrix2 = get_matrix(' second')
        n1 = len(matrix1)
        m1 = len(matrix1[0])
        n2 = len(matrix2)
        m2 = len(matrix2[0])
        if m1 != n2:
            print('ERROR')
        else:
            output = []
            for row1 in range(n1):
                output.append([])
                for col2 in range(m2):
                    total = 0
                    for row2 in range(n2):
                        total += matrix1[row1][row2] * matrix2[row2][col2] 
                    output[row1].append(total)      
            print_matrix(output)
    
    # Transpose matrix     
    elif choice == '4':
        print('''
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
        diagonal_chioce = input('Your choice:')
        
        # Main diagonal
        if diagonal_chioce == '1':
            matrix = get_matrix()
            matrix = transpose(matrix)
            print_matrix(matrix)
                    
        # Side diagonal   
        elif diagonal_chioce == '2':
            matrix = get_matrix()
            matrix = matrix[::-1]
            matrix = [row[::-1] for row in matrix]
            matrix = transpose(matrix)
            print_matrix(matrix)
            
        # Vertical line
        elif diagonal_chioce == '3':
            matrix = get_matrix()
            matrix = [row[::-1] for row in matrix]
            print_matrix(matrix)
            
        # Horizontal line
        elif diagonal_chioce == '4':
            matrix = get_matrix()
            matrix = matrix[::-1]
            print_matrix(matrix)
    
    # Calculate a determinant
    elif choice == '5':
        matrix = get_matrix() 
        n = len(matrix)
        m = len(matrix[0])
        if n != m:
            print('Error')
        else:
            print(determinant(matrix))
            
    # Inverse matrix
    elif choice == '6':
        matrix = get_matrix() 
        n = len(matrix)
        m = len(matrix[0])
        output = None
        if n != m:
            print('Error')
        else:
            det = determinant(matrix)
            if det == 0:
                print("This matrix doesn't have an inverse.")
            else:
                cofactor = []
                for i in range(n):
                    cofactor.append([])
                    for j in range(m):
                        sign = 1
                        if (i + j) % 2 == 1:
                            sign = -1
                        num = sign * determinant(minor(matrix, i, j))   
                        cofactor[i].append(num)
                        
                output = multiply_by_const(transpose(cofactor), 1 / det)
                print_matrix(output)
                