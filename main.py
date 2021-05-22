import sys

import pandas as pd
from z3 import *

from data_types import *

debug = False

def sat_solve(data):
    print("Input data:")
    print(data)

    s = Solver()

    # Basic clauses

    # Garments
    s.add(Not(And(shorts, pants)))          # No shorts and pants
    s.add(Not(And(shorts, jacket)))         # No shorts and jacket
    s.add(Implies(scarf, jacket))           # No scarf without jacket
    s.add(Implies(gloves, jacket))          # No gloves without jacket
    s.add(Or(Not(tie), shirt))              # No tie without shirt

    # Colors
    s.add(Not(And(yellow, white)))
    s.add(Not(And(blue, purple)))
    s.add(Not(And(blue, black)))
    s.add(Not(And(red, green)))
    s.add(Not(And(red, orange)))
    s.add(Not(And(green, pink)))
    s.add(Not(And(green, orange)))

    # Parse input-related clauses
    cond_array = []
    for pair in data.values:
        cond_array.append(And(dict_garments[pair[0]], dict_colors[pair[1]]))
    for el in dict_garments:
        if el not in data.values:
            s.add(Not(dict_garments[el]))
    s.add(Or(cond_array))

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

    if debug:
        print("\nStatistics:")
        # Traverse statistics
        for k, v in s.statistics():
            print("%s: %s" % (k, v))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s filename" % sys.argv[0])
        exit()
    data = pd.read_csv(sys.argv[1], delimiter=', ', comment='#', engine='python')
    sat_solve(data)
