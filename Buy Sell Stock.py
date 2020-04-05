"""This solution is slightly complex and taken from geeksforgeeks"""
# def maxProfit(prices):
#     if len(prices) == 1:
#         return 0
#
#     i = 0
#     maxprofit = 0
#     while i < (len(prices) - 1):
#         while i < (len(prices) - 1) and prices[i+1] <= prices[i]:
#             i += 1
#
#         if i == len(prices)-1:
#             break
#
#         buy = i
#         i += 1
#
#         while i < len(prices) and prices[i] >= prices[i-1]:
#             i += 1
#
#         sell = i - 1
#         maxprofit += (prices[sell] - prices[buy])
#
#     return maxprofit

"""This is a very simple code and works perfectly."""
def maxProfit(prices):
    maxprofit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            maxprofit += (prices[i] - prices[i-1])
    return maxprofit




if __name__ == '__main__':
    print(maxProfit([1,2,3,4,5]))