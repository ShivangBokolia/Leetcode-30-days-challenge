def isHappy(n):
    totalsquare = 0
    while n > 0:
        digit = n % 10
        n = int(n / 10)
        totalsquare += digit ** 2
        
    if totalsquare == 1 or totalsquare == 7:
        return True
    
    if totalsquare < 10:
        return False
    
    return isHappy(totalsquare)

if __name__ == '__main__':
    val = isHappy(19)
    if val is True:
        print("Happy Number")
    else:
        print("Sad Number")

