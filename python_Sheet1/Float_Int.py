N = float(input())
M=int(N)
if(N==M):
    print("int",M)
else:
    print("float",M,f"{(N-M):.3f}")

# if "." in N:
#     npart,decpart = N.split(".")
#     print("float",int(npart),"0."+decpart)
# else:
#     print("int",int((N)))

