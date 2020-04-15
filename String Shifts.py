def stringShift(s, shift):
    if len(shift) == 0:
        return s
    val = shift.pop(0)
    for i in range(val[1]):
        temp = ""
        if val[0] == 0:
            temp = s[0]
            s = s[1:] + temp
        elif val[0] == 1:
            temp = s[len(s) - 1]
            s = temp + s[:len(s)-1]
    return stringShift(s, shift)

if __name__ == '__main__':
    print(stringShift("abc", [[0,1],[1,2]]))