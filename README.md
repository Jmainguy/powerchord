# powerchord
A python script to generate power chord tabs based on input.
## Usage
```bash
./powerchord.py -h
usage: powerchord.py [-h] [-b BANNER] Chords

Tab out songs

positional arguments:
  Chords                Chords you want tabbed out, seperated by commas

optional arguments:
  -h, --help            show this help message and exit
  -b BANNER, --banner BANNER
                        Banner you want to display, like song title
```
## Example
```bash
./powerchord.py -b "(Dammit by Blink182)" ', ,c, ,c, ,c, ,c, ,g, ,g, ,g, ,g, ,a, ,a, ,a, ,a, ,f, ,f, ,f, ,f'
(Dammit by Blink182)
e|--------------------------------|
B|--------------------------------|
G|-5-5-5-5---------2-2-2-2--------|
D|-5-5-5-5-5-5-5-5-2-2-2-2-3-3-3-3|
A|-3-3-3-3-5-5-5-5-0-0-0-0-3-3-3-3|
E|---------3-3-3-3---------1-1-1-1|
```
