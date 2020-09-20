def gcd(a,b):
    a=max(a,b)  
    b=min(a,b)

    if b==0:       #base case
        return a  
    else:

        c=a        #temporary variable
        a=b
        b=c%b

        return gcd(a,b)

print( gcd(200,66)) #example