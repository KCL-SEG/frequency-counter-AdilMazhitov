"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies  = {}
    # Your code goes here
    list = []
    for x in items:
        list.append(str(x))
    for y in list:
        counterItem = list.count(str(y))
        frequencies .update({y : counterItem})
    return frequencies 
