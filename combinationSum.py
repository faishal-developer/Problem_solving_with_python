arr =[0,1,1,2,3,4,5]

def combinationSum(arr,target):
    result = []
    arr.sort()

    def recurse(i,li,sum):
        if(sum==target):
            if li not in result:
                result.append([x for x in li])
        if(sum>target) or i>=len(arr):
            return
        
        recurse(i+1,li+[arr[i]],sum+arr[i])
        recurse(i+1,li,sum)

    recurse(0,[],0)
    return result

print(combinationSum(arr,5))
        
    
