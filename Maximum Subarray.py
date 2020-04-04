""" This code will not work if all the elements of the array are negative """
# def maxSubArray(nums):
#     maxSoFar = 0
#     maxEnd = 0
#     for i in nums:
#         maxEnd += i
#         if maxEnd < 0:
#             maxEnd = 0
#         elif maxSoFar < maxEnd:
#             maxSoFar = maxEnd
#
#     return maxSoFar

""" This code will work if all the elements of the array are negative """
def maxSubArray(nums):
    currentmax = nums[0]
    totalmax = nums[0]
    for i in range(1, len(nums)):
        currentmax = max(nums[i], currentmax + nums[i])
        totalmax = max(currentmax, totalmax)

    return totalmax

if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))