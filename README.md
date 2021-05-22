# SATsolver
Assignment 6 code and report for group 5

## Dependencies

`pip install z3-solver pandas flask flask_cors werkzeug`

## Constraints

Colors:

Red\
Yellow\
Orange\
Green\
Blue\
Purple\
Brown\
Pink\
White\
Black

Garments:

Pants\
Shirt\
Hat\
Jacket\
Sweater\
Gloves\
Shoes\
Tie\
Scarf\
Shorts

Min colors: 3\
Max colors: 5

Garment constraints:

No shorts and pants\
No shorts and jacket\
No scarf without jacket\
No tie without shirt\
No gloves without jacket

Colors that don't go together:

Yellow-white\
Blue-purple\
Blue-black\
Red-green\
Red-orange\
Green-pink\
Green-orange

## Input format

A .txt file in the format (first line is fixed, then the pairs):
```
garment, color
shirt, black
shorts, white
jacket, blue
```