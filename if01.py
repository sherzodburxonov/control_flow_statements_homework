def main(a):
    """
    If the number is positive, increase it to 1,otherwise leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    if a>0:
        x=1
    if a<0:
        x=0
    return x
a=int(input("a="))
print(main(a))
