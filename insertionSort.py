numArr=[2,8,5,6,7,4,1,3,6,5,0,14]

def insertionSort(arr):
    length=len(arr)
    for i in range(1,length-1):
        for j in range(i+1,0,-1):
            if arr[j]<arr[j-1]:
                temp = arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=temp
            else:
                break

insertionSort(numArr)
print(numArr)