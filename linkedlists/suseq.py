def fun(old,new=''):
    if len(old)==0:
        print(new)
        return
    fun(old[1:],new+old[0])
    fun(old[1:],new)
    
old='abcd'
fun(old)