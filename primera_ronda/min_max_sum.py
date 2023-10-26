def miniMaxSum(arr):
    new_arr = sorted(arr)
    total = sum(new_arr)

    max_sum = total - new_arr[0]
    min_sum = total - new_arr[-1]

    print(f"{min_sum} {max_sum}")


array = [1, 2, 3, 4, 5]


# def miniMaxSum(arr):
#     arr = sorted(arr)

#     max_sum = sum(arr[1:])
#     min_sum = sum(arr[:4])
#     print(f"{min_sum} {max_sum}")


miniMaxSum(array)
