def valid(valid_digits,inp):
    a=1
    b=1
    lis=[]
    while(a<=inp):
        x1=str(b)
        count=0
        for i in x1:
            if(i in valid_digits):
                count=count+1
        if(count==len(x1)):
            lis.append(x1)
            a+=1
        b+=1
    lis.reverse()
    return (lis[0])
valid_digits=['0','1','2','5','6','8','9']
inp=int(input())
print(valid(valid_digits,inp))
