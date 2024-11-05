num=1221
num2=-1221

def palindrome(num):
    if(num<0):
        return False
    
    numArr= []
    print(num)
    while num>9:
        reminder = num%10
        numArr.append(reminder)
        num=int(num/10)
    numArr.append(num)
    length=len(numArr)
    for i in range(0,length):
        if numArr[i]!=numArr[length-1-i]:
            return False
    return True
        

print(palindrome(10))


