def gcd(a,b):
    a=max(a,b)  
    b=min(a,b)

    if b==0:
        return a
    else:

        c=a
        a=b
        b=c%b

        return gcd(a,b)

print( gcd(942,66))