#!/usr/bin/python
# This program is to assist in tabbing out songs

import argparse

def chord_parse(chords):
    chords = chords.split(',')
    return chords

parser = argparse.ArgumentParser(description='Tab out songs')
parser.add_argument('-b', '--banner', help='Banner you want to display, like song title')
parser.add_argument('Chords', help='Chords you want tabbed out, seperated by commas', type=chord_parse)
args = parser.parse_args()

def A(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '2'
    string4 = string4 + '2'
    string5 = string5 + '0'
    string6 = string6 + '-'
    return string1, string2, string3, string4, string5, string6

def Asharp(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '2'
    string4 = string4 + '3'
    string5 = string5 + '1'
    string6 = string6 + '-'
    return string1, string2, string3, string4, string5, string6

def B(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '4'
    string4 = string4 + '4'
    string5 = string5 + '2'
    string6 = string6 + '-'
    return string1, string2, string3, string4, string5, string6

def C(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '5'
    string4 = string4 + '5'
    string5 = string5 + '3'
    string6 = string6 + '-'
    return string1, string2, string3, string4, string5, string6

def Csharp(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '6'
    string4 = string4 + '6'
    string5 = string5 + '4'
    string6 = string6 + '-'
    return string1, string2, string3, string4, string5, string6

def D(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '7'
    string4 = string4 + '7'
    string5 = string5 + '5'
    string6 = string6 + '-'
    return string1, string2, string3, string4, string5, string6

def Dsharp(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '8'
    string4 = string4 + '8'
    string5 = string5 + '6'
    string6 = string6 + '-'
    return string1, string2, string3, string4, string5, string6

def E(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '-'
    string4 = string4 + '2'
    string5 = string5 + '2'
    string6 = string6 + '0'
    return string1, string2, string3, string4, string5, string6

def F(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '-'
    string4 = string4 + '3'
    string5 = string5 + '3'
    string6 = string6 + '1'
    return string1, string2, string3, string4, string5, string6

def Fsharp(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '-'
    string4 = string4 + '4'
    string5 = string5 + '4'
    string6 = string6 + '2'
    return string1, string2, string3, string4, string5, string6

def G(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '-'
    string4 = string4 + '5'
    string5 = string5 + '5'
    string6 = string6 + '3'
    return string1, string2, string3, string4, string5, string6

def Gsharp(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '-'
    string4 = string4 + '6'
    string5 = string5 + '6'
    string6 = string6 + '4'
    return string1, string2, string3, string4, string5, string6

def blank(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '-'
    string4 = string4 + '-'
    string5 = string5 + '-'
    string6 = string6 + '-'
    return string1, string2, string3, string4, string5, string6

def end(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '|\n'
    string2 = string2 + '|\n'
    string3 = string3 + '|\n'
    string4 = string4 + '|\n'
    string5 = string5 + '|\n'
    string6 = string6 + '|\n'
    return string1, string2, string3, string4, string5, string6

def main(args):
    banner = args.banner
    chords = args.Chords
    arglist = list()
    string1 = 'e|'
    string2 = 'B|'
    string3 = 'G|'
    string4 = 'D|'
    string5 = 'A|'
    string6 = 'E|'
    for chord in chords:
        if chord == ' ':
          string1, string2, string3, string4, string5, string6 = blank(string1, string2, string3, string4, string5, string6)
        if chord == 'a':
          string1, string2, string3, string4, string5, string6 = A(string1, string2, string3, string4, string5, string6)
        if chord == 'a#':
          string1, string2, string3, string4, string5, string6 = Asharp(string1, string2, string3, string4, string5, string6)
        if chord == 'b':
          string1, string2, string3, string4, string5, string6 = B(string1, string2, string3, string4, string5, string6)
        if chord == 'c':
          string1, string2, string3, string4, string5, string6 = C(string1, string2, string3, string4, string5, string6)
        if chord == 'c#':
          string1, string2, string3, string4, string5, string6 = Csharp(string1, string2, string3, string4, string5, string6)
        if chord == 'd':
          string1, string2, string3, string4, string5, string6 = D(string1, string2, string3, string4, string5, string6)
        if chord == 'd#':
          string1, string2, string3, string4, string5, string6 = Dsharp(string1, string2, string3, string4, string5, string6)
        if chord == 'e':
          string1, string2, string3, string4, string5, string6 = E(string1, string2, string3, string4, string5, string6)
        if chord == 'f':
          string1, string2, string3, string4, string5, string6 = F(string1, string2, string3, string4, string5, string6)
        if chord == 'f#':
          string1, string2, string3, string4, string5, string6 = Fsharp(string1, string2, string3, string4, string5, string6)
        if chord == 'g':
          string1, string2, string3, string4, string5, string6 = G(string1, string2, string3, string4, string5, string6)
        if chord == 'g#':
          string1, string2, string3, string4, string5, string6 = Gsharp(string1, string2, string3, string4, string5, string6)

    string1, string2, string3, string4, string5, string6 = end(string1, string2, string3, string4, string5, string6)
    if banner:
        print banner
    print string1 + string2 + string3 + string4 + string5 + string6
main(args)
