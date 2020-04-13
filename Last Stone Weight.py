def lastStoneWeight(stones):
    if len(stones) == 0:
        return 0
    if len(stones) == 1:
        return stones[0]
    stones = sorted(stones, reverse=True)
    first = stones.pop(0)
    second = stones.pop(0)
    if first == second:
        return lastStoneWeight(stones)
    else:
        first -= second
        stones = [first] + stones
        return lastStoneWeight(stones)



if __name__ == '__main__':
    print(lastStoneWeight([2,7,4,1,8,1]))