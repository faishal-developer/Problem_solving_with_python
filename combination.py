def combination(n,k):
    result=[]

    def recur(i,li):
        if len(li)==k:
            result.append(li)
            return
        
        if(i>n):
            return
         
        recur(i+1,li+[i])
        recur(i+1,li)
    
    recur(1,[])
    return result

print(combination(4,3))