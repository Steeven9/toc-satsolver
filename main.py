import pandas as pd
from z3 import *

debug = False

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
    tie = Bool('tie')
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
    s.add(Xor(shorts, pants))               # No shorts and pants
    s.add(Xor(shorts, jacket))              # No shorts and jacket
    s.add(Not(And(scarf, Not(jacket))))     # No scarf without jacket
    s.add(Not(And(tie, Not(shirt))))        # No tie without shirt
    s.add(Not(And(gloves, Not(jacket))))    # No gloves without jacket

    # Colors
    s.add(Not(And(yellow, white)))
    s.add(Not(And(blue, purple)))
    s.add(Not(And(blue, black)))
    s.add(Not(And(red, green)))
    s.add(Not(And(red, orange)))
    s.add(Not(And(green, pink)))
    s.add(Not(And(green, orange)))

    # TODO Parse input-related clauses
    s.add(Or(And(shirt, black), And(shorts, white), And(jacket, blue)))
    
    print("\nConstraints:")
    for c in s.assertions():
        print(c)

    print("\nResult: %s" % s.check())

    if s.check() == sat:
        m = s.model()
        if debug:
            print("\nFull model:")    
            for d in m.decls():
                print("%s = %s" % (d.name(), m[d]))

        print("\nActual pairs:")
        # Return actual pairs
        for pair in data.values:
            for d in m.decls():
                if pair[0] == d.name() and m[d]:
                    gar = d.name()
                    for d in m.decls():
                        if pair[1] == d.name() and m[d]:
                            print("%s %s" % (gar, d.name()))
 
    print("\nStatistics:")
    # Traverse statistics
    for k, v in s.statistics():
        print("%s: %s" % (k, v))
