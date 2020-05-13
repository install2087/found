a1=input('جملت؟')
a2=input('تعداد چه کاراکتریو رو میخوای حالا؟ ')
a=list(a2)
b={}
b[a2]=0
for p in a1:
    if p in a:
        b[p]+=1
for b,v in b.items():
    print(b,'=',v)

print('@install2087/inastall2087.xyz')
