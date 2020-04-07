def countElements(arr):
    """ The time complexity reduces if the set is included because repeated elements are not allowed in sets.
        This would not work if the elements are counted for repeated count.
        e.g. [1, 1, 2, 2] has the output 2, but if the set is used the output might be 1."""
    #setarr = set(arr)
    """ This is one way to do it, but the time complexity is O(n)"""
    count = 0
    for i in arr:
        if (i+1) in arr:
            count += 1
    return count


if __name__ == '__main__':
    print(countElements([1, 1, 2, 2]))
