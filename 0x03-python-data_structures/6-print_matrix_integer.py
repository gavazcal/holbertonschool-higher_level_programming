#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for x_idx in range(len(matrix)):
            for y_idx in range(len(matrix[x_idx])):
                print("{:d}".format(matrix[x_idx][y_idx]), end="")
                if y_idx != len(matrix[x_idx]) - 1:
                    print(end=" ")
            print()
