import numpy as np

def get_polynom(coords):
    n = len(coords)
    x = [c[0] for c in coords]
    y = [c[1] for c in coords]
    a = np.ones((n, n))

    # calc x matrix
    for i in range(len(x)): # row
        for j in range(1, len(x)): # colon

            a[i][j] = pow(x[i],j)

    # calc y matrix
    text_to_b = ''
    for item in y:

        text_item = f'{item};'
        text_to_b += text_item

    text_to_b = text_to_b[:-1]
    b = np.matrix(text_to_b)

    # calc coeficients
    return np.linalg.solve(a, b)

if __name__ == '__main__':
    coords =  [(-1, 2), (0, 3), (3, 4), (5, 0)]
    print(get_polynom(coords))