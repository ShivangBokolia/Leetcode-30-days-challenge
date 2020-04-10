""" The time complexity of the program is O(N) and space complexity is O(1)."""
def backspaceCompare(S, T):
    strS = ""
    strT = ""
    for i in S:
        if i == '#' and len(strS) != 0:
            strS = strS[0:len(strS) - 1]
        elif i != '#':
            strS += i
        else:
            continue
    for i in T:
        if i == '#' and len(strT) != 0:
            strT = strT[0:len(strT) - 1]
        elif i != '#':
            strT += i
        else:
            continue

    if strS == strT:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    backspaceCompare("a##c", "#a#c")

