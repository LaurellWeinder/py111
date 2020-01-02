import numpy as np

def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    l = np.zeros(shape)
    m, n = point
    print(l)
    for i in range(len(l)):
        for j in range(len(l), 0):

            l[i][j] += l[i - 2][j - 1] * 2 + l[i - 2][j + 1] * 2 \
                    + l[i - 1][j - 2] * 2 + l[i + 1][j - 2] * 2
            print(l[m][n])



print(calculate_paths((8, 8), (7, 7)))
