def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    x=0
    if a<0:
        x+=1
    if b<0:
        x+=1
    if c<0:
        x+=1
    return x
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
print(main(a,b,c))