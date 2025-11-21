a,b = input().split()
a = int(a)
b = int(b)

if(a+b>0 and (a==b+1 or b==a+1 or a==b)) :
    print("YES")
else:
    print("NO")