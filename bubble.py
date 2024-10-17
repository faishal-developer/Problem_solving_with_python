numArr=[2,8,5,6,7,4,1,3,6,5]

def bubbleSort(arr):
    length=len(arr)

    for i in range(length-1):
        for j in range(length-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp


bubbleSort(numArr)
print(numArr)

