def largestSquareNumber(n: int):
    q = 1
    while n>(q*q):
        q = q+1
    q = (q-1)*(q-1)
    return q
print(largestSquareNumber(82))
# it looks like I learned how to use git today
