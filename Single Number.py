def singleNumber(nums):
    dic = dict()
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    for j in dic:
        if dic[j] == 1:
            return j

if __name__ == '__main__':
    print(singleNumber([4,1,2,1,2]))
