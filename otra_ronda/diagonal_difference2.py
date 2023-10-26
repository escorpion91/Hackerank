def diagonalDifference(arr):
    suma_diagonal_l2r = 0
    suma_diagonal_r2l = 0

    for i in range(len(arr)):
        suma_diagonal_l2r += arr[i][i]
        suma_diagonal_r2l += arr[i][(len(arr)-1) - i]

    return abs(suma_diagonal_r2l - suma_diagonal_l2r)
