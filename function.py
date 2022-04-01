from random import random
from random import uniform
from random import randint


def create_identical_matrix(matrix):
    matrix1 = []
    for k in range(len(matrix)):
        line = []
        for m in range(len(matrix[k])):
            line.append(matrix[k][m])
        matrix1.append(line)
    return matrix1


def create_unit_vector(n):
    vector = []
    for k in range(n):
        vector.append(1)
    return vector


def delete_line(matrix, line):
    matrix1 = create_identical_matrix(matrix)
    matrix1.pop(line - 1)
    return matrix1


def delete_column(matrix, column):
    matrix1 = create_identical_matrix(matrix)
    for k in range(len(matrix)):
        matrix1[k].pop(column - 1)
    return matrix1


def transposition(matrix):
    matrix1 = []
    for k in range(len(matrix)):
        line = []
        for m in range(len(matrix[k])):
            line.append(matrix[m][k])
        matrix1.append(line)
    return matrix1


def determinant(matrix):
    det = 0
    if len(matrix) == 1:
        det = matrix[0][0]
    else:
        for k in range(1, len(matrix) + 1):
            index = 1 + k
            if index % 2 == 0:
                sign = 1
            else:
                sign = -1
            tmp_matrix = delete_line(delete_column(matrix, k), 1)
            det += (matrix[0][k - 1] * (sign * determinant(tmp_matrix)))
    return det


def inverse(matrix):
    matrix1 = []
    for k in range(len(matrix)):
        line = []
        for m in range(len(matrix[k])):
            index = m + k + 2
            if index % 2 == 0:
                sign = 1
            else:
                sign = -1
            line.append(sign * determinant(delete_line(delete_column(transposition(matrix), m + 1), k + 1)))
        matrix1.append(line)
    for k in range(len(matrix)):
        for m in range(len(matrix)):
            matrix1[k][m] /= determinant(matrix)
    return matrix1


def acting(matrix, vector):
    vector1 = []
    tp = 0
    for k in range(len(matrix)):
        for m in range(len(matrix[0])):
            tp += matrix[k][m] * vector[m]
        vector1.append(tp)
        tp = 0
    return vector1


def scalar_product(vector1, vector2):
    product = 0
    for k in range(len(vector1)):
        product += (vector1[k] * vector2[k])
    return product


def write_vector(vector):
    st = ''
    for k in range(len(vector)):
        st += (str(vector[k]) + ' ')
    st += "\n"
    return st


def write_matrix(matrix):
    st = ''
    for k in range(len(matrix)):
        for m in range(len(matrix[0])):
            st += (str(matrix[k][m]) + ' ')
        st += "\n"
    return st


f = open("info.txt", "w")

print("Enter the number of points:")
points = int(input())
print("Enter the dimension:")
dim = int(input())
x_vector = []
x_exp = []
y_vector = []
V_matrix = []
c_vector = []
line = []
for i in range(points):
    for j in range(dim):
        line.append(random())
    x_vector.append(line)
    line = []
x_str = write_matrix(x_vector)

for i in range(dim):
    x_exp.append(random())
exp_str = write_vector(x_exp)

for i in range(dim):
    for j in range(dim):
        line.append(random())
    V_matrix.append(line)
    line = []
V_str = write_matrix(V_matrix)

for i in range(dim):
    c_vector.append(random())
c_str = write_vector(c_vector)

for i in range(points):
    y_vector.append(scalar_product(acting(V_matrix, x_vector[i]), x_vector[i]) + scalar_product(c_vector, x_vector[i]))
y_str = write_vector(y_vector)

y = scalar_product(acting(V_matrix, x_exp), x_exp) + scalar_product(c_vector, x_exp)

f.write("Points:\n")
f.write(x_str + '\n')
f.write("Experimental point:\n")
f.write(exp_str + '\n')
f.write("Matrix V:\n")
f.write(V_str + '\n')
f.write("Vector C:\n")
f.write(c_str + '\n')
f.write("Vector of values:\n")
f.write(y_str + '\n')
f.write("Experimental value:\n")
f.write(str(y) + '\n')

f.close()

ff = open("data.txt", "w")
ff.write(str(points) + " " + str(dim) + "\n")
ff.write(x_str + '\n')
ff.write(y_str + '\n')
ff.write(exp_str + '\n')
ff.close()