num = 999

def isPalindrome(number):
    temp = str(number)
    temp = temp[::-1]
    #print(number)
    if(int(temp) == number):
        return True
    else:
        return False

max = 0
for num1 in range(num,-1,-1):
    if(num1 < 800):
        break
    for num2 in range(num1,-1,-1):
        if(num2 < 800):
            break
        temp = num1 * num2
        if max > temp :
            break
        #print(temp)
        if isPalindrome(temp) :
            if max < temp :
                max = temp
    
print(max)