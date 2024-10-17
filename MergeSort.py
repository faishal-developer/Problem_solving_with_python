numArr=[2,8,5,6,7,4,1,3,6,5]

def mergeSort(arr):
    length=len(arr)
    if length<=1:
        return arr

    arr1=[]
    arr2=[]
    for i in range(0,length):
        if(i<(length-1)/2):
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])
    
    arrS1 = mergeSort(arr1)
    len1=len(arrS1)
    arrS2 = mergeSort(arr2)
    len2=len(arrS2)

    # conquer stage started here
    resultArr=[]
    l=0
    r=0
    for i in range(0,length):
        if r>=len2:
            if l<len1:
                # print(arrS1,l)
                resultArr.append(arrS1[l])
                l=l+1
        elif l>=len1:
            if r<len2:
                resultArr.append(arrS2[r])
                r=r+1
        elif arrS1[l]<=arrS2[r]:
            resultArr.append(arrS1[l])
            l=l+1
        elif arrS1[l]>arrS2[r]:
            resultArr.append(arrS2[r])
            r=r+1
    
    return resultArr



result= mergeSort(numArr)
print("result=",result)