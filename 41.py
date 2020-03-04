x1 = 2
x2 = 10
y1 = 3
y2 = 16

s1 = 1
s2 = 2

left_operand = [
                [x1, y1],
                [x2, y2]
                ]
right_operands = [s1, s2]

def get_determinant():
    product_of_leading_diagonal = left_operand[0][0] * left_operand[1][1]
    product_of_other_diagonal = left_operand[0][1] * left_operand[1][0]
    determinant = product_of_leading_diagonal - product_of_other_diagonal
    return determinant

def inverse(det):
    if det == 0:          #singlar matrix
        inverse_matrix = [
                [x1, y1],
                [x2, y2]
        ]
    else:
        reciprocal_of_det = 1/det
        inverse_matrix = [
            [left_operand[1][1]*reciprocal_of_det, -left_operand[0][1]*reciprocal_of_det],
            [-left_operand[1][0] * reciprocal_of_det, left_operand[0][0]*reciprocal_of_det]
        ]
    return inverse_matrix

def premultiply_by_inverse(matrix_inverse):
    value_of_x = matrix_inverse[0][0] * right_operands[0] + matrix_inverse[0][1] * right_operands[1]
    value_of_y = matrix_inverse[1][0] * right_operands[0] + matrix_inverse[1][1] * right_operands[1]
    return [value_of_x, value_of_y]

def calculate_matrix():
    the_det = get_determinant()
    inverse_mat = inverse(the_det)
    solutions = premultiply_by_inverse(inverse_mat)
    print(f'X = {solutions[0]}')
    print(f'Y = {solutions[1]}')

calculate_matrix()