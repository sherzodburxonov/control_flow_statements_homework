def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<0:
        a="Freezing"
    if 1<temp<10:
        a="very_cold"
    if 11<temp<21:
        a="cold"
    if 21<temp<30:
        a="Normal"
    if 31<temp<40:
        a="Hot"
    if 40<temp:
        a="Very_Hot"
    return a
temp=int(input())
print(main(temp))    