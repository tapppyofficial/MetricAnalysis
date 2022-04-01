def create_identical_matrix(matrix):
    matrix1 = []
    for k in range(len(matrix)):
        line = []
        for m in range(len(matrix[k])):
            line.append(matrix[k][m])
        matrix1.append(line)
    return matrix1


def create_empty_matrix(n):
    matrix1 = []
    for k in range(n):
        line = []
        for m in range(n):
            line.append(0)
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


f = open("data.txt", 'r')

list_of_points = []
values = []
exp_point = []
main_list = f.readlines()
number_of_points = int(main_list[0].split(' ')[0])
dimension = int(main_list[0].split(' ')[1])
weight_list = create_unit_vector(number_of_points)

for i in range(1, number_of_points + 1):
    tmp = main_list[i].split(' ')
    temp = []
    for j in range(dimension):
        temp.append(float(tmp[j]))
    list_of_points.append(temp)

tmp = main_list[number_of_points + 2].split(' ')
for j in range(number_of_points):
    values.append(float(tmp[j]))

tmp = main_list[number_of_points + 4].split(' ')
for j in range(dimension):
    exp_point.append(float(tmp[j]))

W_matrix = create_empty_matrix(number_of_points)

for i in range(number_of_points):
    for j in range(number_of_points):
        W_matrix[i][j] = 0
        for t in range(dimension):
            W_matrix[i][j] += (weight_list[i] * (list_of_points[i][t] - exp_point[t]) * (list_of_points[j][t] - exp_point[t]))

W_inverse = inverse(W_matrix)
act = acting(W_inverse, create_unit_vector(number_of_points))

numerator = scalar_product(act, values)
denominator = scalar_product(act, create_unit_vector(number_of_points))

y = numerator / denominator

print("This is you experimental value: ", y)

f.close()
