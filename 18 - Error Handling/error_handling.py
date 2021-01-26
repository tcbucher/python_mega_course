# Use a try and except block to handle runtime errors (exceptions)
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Zero division is illegal'

print(divide(1,0))