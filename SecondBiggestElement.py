arr = [4,3,5,9,10,12,3,1,20,18]

def secondBiggestElement(arr):
    biggest=-9999999
    secondBiggest=-9999999

    for value in arr:
        if(value>biggest):
            secondBiggest=biggest
            biggest=value
        elif value>secondBiggest:
            secondBiggest=value

    return secondBiggest

print(secondBiggestElement(arr))



        