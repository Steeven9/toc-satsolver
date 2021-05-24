# Funky Fashion Store
A SATSolver with style! Assignment 6 code and report for group 5 (Andrea Brites Marto, Tommaso Rodolfo Masera, Stefano Taillefert, Ted).

Check out the live demo at [https://bestsatsolver.xyz](https://bestsatsolver.xyz)!


## Install dependencies

```console
pip install --no-cache-dir -r requirements.txt
```


## Run from command line

```console
python main.py input_file
```
where `input_file` is a text file with the pairs (garment, color). See `examples/` or below for format.


## Run the webserver

```console
cd app
```

```console
flask run
```

Then head to `localhost:5000` to access the interface.


## Run the webserver with Docker

```console
docker-compose up
```


## Constraints

Colors available:

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

Garments available:

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


## Input file format

A text file in the following format (first line is fixed, then the pairs):
```
garment, color
shirt, black
shorts, white
jacket, blue
```
