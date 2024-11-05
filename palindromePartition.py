str = "addbdda"

def palindromePartition(str):
    result = []
    obj = {}
    DP = {}
    def isPalindrome(str):
        for i in range(0,len(str)):
            if(str[i]!= str[len(str)-1-i]):
                return False
        return True

    def recursion(newResult,newStr):
        if newStr=='':
            resultStr=' '.join(newResult)
            if resultStr not in obj:
                print(resultStr)
                result.append(newResult)
                obj[resultStr] = True
                return newResult
        
        tempStr=''
        for i in range(0,len(newStr)):
            tempStr+=newStr[i]
            tempResult=[]
            if isPalindrome(tempStr):
                if newStr[i+1:] in DP:
                    for value in DP[tempStr]:
                        if value!=False:
                            temp = newResult+tempStr+value
                            newresutStr= ' '.join(temp)
                            if (newresutStr not in obj) and (value != False):
                                result.append(temp)
                else:
                    tempResult = recursion(newResult+[tempStr],newStr[i+1:])
                if newStr[i+1:] not in DP:
                    DP[newStr[i+1:]]=[False if tempResult==None else tempResult]
                else:
                    # print(DP[tempStr],False if tempResult==None else tempResult)
                    # print(DP[tempStr],DP[tempStr].append(False if tempResult==None else tempResult))
                    DP[newStr[i+1:]].append(False if tempResult==None else tempResult ) 
                    # print(DP,"two")
                print(DP,"one")
        
    recursion([],str)
    return result

print(palindromePartition(str))