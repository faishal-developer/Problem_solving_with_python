numArr=[2,8,5,6,7,4,1,3,6,5]

def sectionSort(arr):
    length=len(arr)

    for i in range(length-1):
        biggest=-9999999
        index=-1
        for j in range(length-i-1):
            if arr[j]>biggest:
                biggest=arr[j]
                index=j
        if index!=-1:
            temp = arr[index]
            arr[index]= arr[length-1-i]
            arr[length-1-i]=temp

sectionSort(numArr)
print(numArr)