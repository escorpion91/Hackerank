def diagonalDifference(arr):
    # left to right = arr[o][o] + arr[1][1] + arr[2][2]
    # right to left = arr[o][2] + arr[1][1] + arr[2][0]
    sum_diag_left_right = 0
    sum_diag_right_left = 0
    for i in range(len(arr)):
        sum_diag_left_right += arr[i][i]
        sum_diag_right_left += arr[i][(len(arr)-1) - i]
    return abs(sum_diag_left_right - sum_diag_right_left)


matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9],
]


matrix2 = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12],
]


result = diagonalDifference(matrix)
result2 = diagonalDifference(matrix2)

print(result)
print(result2)
