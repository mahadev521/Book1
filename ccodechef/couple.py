from sys import stdin,stdout
rl=lambda : stdin.readline()
wl=lambda s: stdout.write(str(s)+'\n')
for _ in range(int(rl())):
    n=rl()
    bo=sorted([int(x) for x in rl().split()])
    gl=sorted([int(x) for x in rl().split()],reverse=True)
    wl(max(i+j for i,j in zip(bo,gl)))
    # wl(max(max(bo)+min(gl),max(gl)+min(bo)))