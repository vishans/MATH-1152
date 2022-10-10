'''Recursive step-by-step gcd algorithm'''

def gcd(a,b, __maxFormatLim = None):
    a,b = max(a,b), min(a,b)
    
    if b == 0:
        return a

    if not __maxFormatLim:
        __maxFormatLim = len(str(a))

    q = a//b 
    r = a % b
    
    print(f'{a:<{__maxFormatLim}d} = {b:>{__maxFormatLim}d} *  {q}  + {r}')
    return gcd(b,r, __maxFormatLim)

if __name__ == '__main__':
    print(gcd(1701,3768))