arr=[1,2,3,4]

def permutation(arr):
    if len(arr)==1:
        return [arr]
    result=[]
    for i in range(len(arr)):
        current = arr[i]
        otherElements=arr[:i]+arr[i+1:]

        for perms in permutation(otherElements):
            result.append([current]+perms)
    return result

print(len(permutation(arr)))