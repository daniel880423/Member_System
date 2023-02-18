s="a-bC-dEf-ghIj"
lst=list(s)
lst2=[]
for i in range(len(lst)):
    if lst[i]=="-":
        lst2.append(i)
ans=""
s=s.replace("-","")
s=s[::-1]

n = 0
while n < len(s):
    if n in lst2:
        ans+="-"
        ans+=s[n]
        n += 1
    else:
        ans+=s[n]
    n += 1       
print(ans)
    
    








     


    