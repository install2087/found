a1=input('جملت؟')
a2=input('کاراکتر هایی که میخوای پیدا کنی بگو و راحت باش مثلا اگه دنبال i و n هستی بنویس i n من برات میگم هر کاراکتر چند بار امده؟ ')
a=tuple(a2)
b={}
for p in a1:
    if p in a:
        b.setdefault(p,0)
        b[p]+=1
for b,v in b.items():
    print(b,'=',v)
print('اپدیت ۳')

print('@install2087/inastall2087.xyz')
