# Question 1: Add Two Matrices
def add_matrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
sum_matrix = add_matrices(matrix1, matrix2)
print("Sum of matrices:")
for row in sum_matrix:
    print(row)

# Question 2: Multiply Two Matrices
def multiply_matrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            element = 0
            for k in range(len(mat2)):
                element += mat1[i][k] * mat2[k][j]
            row.append(element)
        result.append(row)
    return result

product_matrix = multiply_matrices(matrix1, matrix2)
print("Product of matrices:")
for row in product_matrix:
    print(row)

# Question 3: Transpose a Matrix
def transpose_matrix(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

transpose = transpose_matrix(matrix1)
print("Transposed matrix:")
for row in transpose:
    print(row)

# Question 4: Sort Words in Alphabetic Order
sentence = input("Enter a sentence: ")
words = sentence.split()
words.sort()
sorted_sentence = ' '.join(words)
print("Sentence with words sorted in alphabetic order:", sorted_sentence)

# Question 5: Remove Punctuation From a String
import string

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

text = input("Enter a string with punctuation: ")
no_punctuation_text = remove_punctuation(text)
print("String with punctuation removed:", no_punctuation_text)
