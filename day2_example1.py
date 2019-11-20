"""
how to manage try except finally raise
"""

a = 10
b = 19

try:
    a / b  # in case there is exception
except Exception as e:
    print(e)
    print("Some exception Occured")
finally:
    print("This will still execute...")