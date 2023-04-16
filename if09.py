def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    first=a//10
    second=a%10
    b=second*10+first
    if a>=b:
        c="True"
    if a<b:
        c="false"
    return c
a=int(input("a="))
print(main(a))