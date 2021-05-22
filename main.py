import pandas as pd
from enums import ColorType, GarmentType
from z3 import *

if __name__ == '__main__':
    data = pd.read_csv('input.txt', delimiter=', ', engine='python')
    print("Input data:")
    print(data)

    s = Solver()
    # Garments
    pants = Bool('pants')
    shirt = Bool('shirt')
    hat = Bool('hat')
    jacket = Bool('jacket')
    sweater = Bool('sweater')
    gloves = Bool('gloves')
    shoes = Bool('shoes')
    underwear = Bool('underwear')
    scarf = Bool('scarf')
    shorts = Bool('shorts')

    # Color
    red = Bool('red')
    yellow = Bool('yellow')
    orange = Bool('orange')
    green = Bool('green')
    blue = Bool('blue')
    purple = Bool('purple')
    brown = Bool('brown')
    pink = Bool('pink')
    white = Bool('white')
    black = Bool('black')

    # Basic clauses

    # Garments
    s.add(Xor(shirt, pants))                # No shorts and pants
    s.add(Xor(shorts, jacket))              # No shorts and jacket
    s.add(Not(And(scarf, Not(jacket))))     # No scarf without jacket
    s.add(Not(And(gloves, Not(jacket))))    # No gloves without jacket
    s.add(underwear)                        # At least underwear

    # Colors
    s.add(Not(And(yellow, white)))
    s.add(Not(And(blue, purple)))
    s.add(Not(And(blue, black)))
    s.add(Not(And(red, green)))
    s.add(Not(And(red, orange)))
    s.add(Not(And(green, pink)))
    s.add(Not(And(green, orange)))

    # TODO input-related clauses
    
    print("\nConstraints:")
    for c in s.assertions():
        print(c)

    print("\nResult: %s" % s.check())

    if s.check() == sat:
        print("\nModel:")
        print(s.model())

    print("\nStatistics:")
    # Traversing statistics
    for k, v in s.statistics():
        print("%s: %s" % (k, v))
