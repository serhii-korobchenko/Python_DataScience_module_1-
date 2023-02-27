import numpy as np


def get_polynom(coords):
    matrix_number = len(coords)
    print (matrix_number)
    # a =  np.matrix([A,B, C])

    x_list = []
    y_list = []
    for item in coords:
        x_list.append(item[0])
        y_list.append(item[1])

    x = np.asarray(x_list)
    y = np.asarray(y_list)
    print(x, y)


    # Find the coefficients of the quadratic function that fits the points
    coefficients = np.polyfit(x, y, 1)

    # Print the coefficients
    print(coefficients)





    # return np.linalg.solve(a, b)


if __name__ == '__main__':

    coords =  [(1, 2), (4,6)]
    get_polynom(coords)