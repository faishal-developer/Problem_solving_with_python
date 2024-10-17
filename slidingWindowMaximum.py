import collections
arr=[2,8,5,6,7,4,1,8,6,5]

def slidingWindowMaximum(arr,w):
    deq=collections.deque([])
    resultArr=[]
    length = len(arr)
    for i in range(length):
        if len(deq)>0 and deq[0]<i-w+1:
            deq.popleft()
        
        while len(deq)>0 and arr[deq[-1]]<arr[i]:
            deq.pop()
        
        deq.append(i)

        if i>=w-1:
            resultArr.append(arr[deq[0]])
    return resultArr
    

print(slidingWindowMaximum(arr,3))