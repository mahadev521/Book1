def oddSq(n):
    if n<1: return 0
    return n*n+oddSq(n-2)
from sys import stdin,stdout
rl=lambda : stdin.readline()
wl=lambda s: stdout.write(str(s)+'\n')
for _ in range(int(rl())):
    n=int(rl())
    wl(oddSq(n))