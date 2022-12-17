import numpy as np


Rx = np.array([
    [1, 0, 0],
    [0, 0, -1],
    [0, 1, 0]
], dtype='int')

Ry = np.array([
    [0, 0, 1],
    [0, 1, 0],
    [-1, 0, 0]
], dtype='int')


rotations = [
    np.identity(3, dtype='int'),
    Rx,
    Ry,
    Rx @ Rx,
    Rx @ Ry,
    Ry @ Rx,
    Ry @ Ry,
    Rx @ Rx @ Rx,
    Rx @ Rx @ Ry,
    Rx @ Ry @ Rx,
    Rx @ Ry @ Ry,
    Ry @ Rx @ Rx,
    Ry @ Ry @ Rx,
    Ry @ Ry @ Ry,
    Rx @ Rx @ Rx @ Ry,
    Rx @ Rx @ Ry @ Rx,
    Rx @ Rx @ Ry @ Ry,
    Rx @ Ry @ Rx @ Rx,
    Rx @ Ry @ Ry @ Ry,
    Ry @ Rx @ Rx @ Rx,
    Ry @ Ry @ Ry @ Rx,
    Rx @ Rx @ Rx @ Ry @ Rx,
    Rx @ Ry @ Rx @ Rx @ Rx,
    Rx @ Ry @ Ry @ Ry @ Rx
]
