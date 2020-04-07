""" The basic approach of while having space complexity O(n)"""
# def moveZeroes(nums):
#     array = []
#     count = 0
#     for i in nums:
#         if i == 0:
#             count += 1
#         else:
#             array.append(i)
#     for j in range(count):
#         array.append(0)
#     return array

""" This uses double pointer concept and has space complexity O(1)"""
def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            for j in range(i+1, len(nums)):
                if nums[j] != 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
    return nums




if __name__ == '__main__':
    print(moveZeroes([0,1,0,3,12]))
