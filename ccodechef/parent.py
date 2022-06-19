def fun(p,n):
    p=list(p)
    try:
        for i in n: p.remove(i)
    except: return 'NO'
    return 'YES'    
from sys import stdin,stdout
rl=lambda : stdin.readline().strip('\n')
wl=lambda x: stdout.write(str(x)+'\n')
for _ in range(int(rl())):
    p=rl().replace(' ','')
    dup=''
    for _ in range(int(rl())):
        dup+=rl().strip()
    print(fun(p,dup))