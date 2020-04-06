"""The first solution is taken from leetcode and has time complexity of O(NK)"""

# import collections
#
#
# def groupAnagrams(strs):
#     ans = collections.defaultdict(list)
#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord('a')] += 1
#         ans[tuple(count)].append(s)
#     return ans.values()

"""This has a complexity of O(NKlogK)"""
def groupAnagrams(strs):
    newstrs = []
    dicwords = dict()
    finalstrs = []
    for i in strs:
        newstrs.append(''.join(sorted(i)))
    for i in range(len(strs)):
        if newstrs[i] in dicwords:
            dicwords[newstrs[i]].append(strs[i])
        else:
            dicwords[newstrs[i]] = [strs[i]]
    for key,value in dicwords.items():
        finalstrs.append(value)

    print(finalstrs)


if __name__ == '__main__':
    groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])