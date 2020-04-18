def productExceptSelf(nums):
    prefix = [0]*len(nums)
    suffix = [0]*len(nums)
    prefix[0] = 1
    suffix[len(nums)-1] = 1
    result = []

    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] * nums[i-1]

    for j in range(len(nums)-2, -1, -1):
        suffix[j] = suffix[j+1] * nums[j+1]

    for k in range(len(nums)):
        result.append(prefix[k] * suffix[k])

    return result
if __name__ == '__main__':
    print(productExceptSelf([1,2,3,4]))