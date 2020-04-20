def checkValidString(s):
    stack = []
    star = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == '*':
            star.append(i)
        elif s[i] == ')':
            if len(stack) != 0:
                stack.pop(len(stack)-1)
            elif len(star) != 0:
                star.pop(len(star)-1)
            else:
                return False

    while len(stack) != 0:
        if len(star) == 0:
            return False

        if stack[len(stack)-1] < star[len(star)-1]:
            stack.pop(len(stack)-1)
            star.pop(len(star)-1)
        else:
            break

    return len(stack) == 0



    print(stack)

    # for i in s:
    #     if i == '(':
    #         stack.append(i)
    #     elif i == ')':
    #         if len(stack) != 0:
    #             stack.pop(len(stack)-1)
    #         else:
    #             return False
    # elif i == '*':
    #     if len(stack) != 0:
    #         stack.pop(len(stack)-1)
    #     else:
    #         stack.append(')')


if __name__ == '__main__':
    print(checkValidString("(*"))
