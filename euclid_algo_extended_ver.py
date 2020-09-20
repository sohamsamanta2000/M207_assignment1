def ext_gcd(a,b):
    x, y= 0,1    #initial values
    x1,y1= 1,0   #initial values
    while a!=0:
        q= b//a
        r=b%a
        x2=x-x1*q
        y2=y-y1*q
        b=a
        a=r
        x=x1
        y=y1
        x1=x2
        y1=y2

    gcd=b

    return gcd, x, y

print( ext_gcd(10889992,66))   #example