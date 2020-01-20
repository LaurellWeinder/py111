import numpy as np

def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    l = np.zeros(shape, dtype=np.int)
    l[0][0] = 1
    for i in range(shape[0]):
        for j in range(shape[1]):
            if (i + 1 < shape[0]) and (j + 2 < shape[1]):
                l[i + 1, j + 2] += l[i, j] * 2
            if (i + 1 < shape[0]) and (j - 2 >= 0):
                l[i + 1, j - 2] += l[i, j] * 2
            if (i + 2 < shape[0]) and (j - 1 >=0):
                l[i + 2, j - 1] += 2 * l[i, j]
            if (i + 2 < shape[0]) and (j + 1 < shape[1]):
                l[i + 2, j + 1] += 2 * l[i, j]
    return l[point[0]][point[1]]



