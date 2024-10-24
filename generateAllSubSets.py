arr=[1,2,3,4]

def genAllSubset(arr):
    result = []

    def recurse(newArr,tempResult,length):
        if(len(tempResult)==length):
            result.append(tempResult)
            return 
        while len(newArr)>0:
            current = newArr[0]
            tempArr= newArr[:0]+newArr[1:]
            newArr=tempArr
            # print(tempResult)
            recurse(tempArr,tempResult+[current],length)
            # recurse(tempArr,tempResult,length)
            
    
    for i in range(0,len(arr)+1):
        # print(result)
        recurse(arr,[],i)
    
    return result

print(genAllSubset(arr))
# arr2=[1]
# arr2=arr2[:0]+arr2[1:]
# print(arr2)