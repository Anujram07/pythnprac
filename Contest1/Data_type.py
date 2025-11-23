n,k,a=map(int,input().split())
result=(n*k)/a
check=int(result)
r1=int(-2147483648)
r2=int(2147483647)
if(result==check):
    if(r1<=result<=r2):
        print("int")
    else:
        print("long long")
else:
    print("double")