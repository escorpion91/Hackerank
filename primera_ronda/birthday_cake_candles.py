def birthdayCakeCandles(candles):
    m = max(candles)
    return candles.count(m)


# o tambien puedes:

# def birthdayCakeCandles(candles):
#     # Write your code here
#     m = candles[0]
#     count = 0
#     for candle in candles:
#         if candle >= m:
#             count += 1
#     return count


lista = [4, 3, 2, 1, 4, 4]
print(birthdayCakeCandles(lista))
