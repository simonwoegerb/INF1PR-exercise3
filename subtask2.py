def sequence():
    n = 0
    m = 0
    s = 0
    a = 0
    x = int(input())
    m = x # first is always smallest
    while x != -1:
        n = n+1
        s = s+x
        if m>x:
            print(x)
            m = x
        x = int(input())
    if n != 0:
        a = s/n
    else:
        m = -1
        a = -1
    return (n,s,m,a)
print(sequence())
# it looks like I learned how to use git today
