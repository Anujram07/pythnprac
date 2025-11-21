eye,mouth,body = map(int,input().split()) 
minimum=min(eye,mouth,body)
count=int(minimum)
eye=eye-minimum
mouth=mouth-minimum
body=body-minimum
if(body>(eye//2)):
    count=count+(eye//2)
else:
    count=count+body
print(count)