#!/usr/bin/python
# This program is to assist in tabbing out songs

import argparse

parser = argparse.ArgumentParser(description='Tab out songs')
parser.add_argument('-t', '--tuning', help='Currently dropd and standard are allowed')
parser.add_argument('-b', '--banner', help='Banner you want to display, like song title')
parser.add_argument('Chords', help='Chords you want tabbed out')
args = parser.parse_args()

def E(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '-'
    string4 = string4 + '2'
    string5 = string5 + '2'
    string6 = string6 + '0'
    return string1, string2, string3, string4, string5, string6

def A(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '2'
    string4 = string4 + '2'
    string5 = string5 + '0'
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

def G(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '-'
    string4 = string4 + '5'
    string5 = string5 + '5'
    string6 = string6 + '3'
    return string1, string2, string3, string4, string5, string6

def F(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '-'
    string4 = string4 + '3'
    string5 = string5 + '3'
    string6 = string6 + '1'
    return string1, string2, string3, string4, string5, string6

def C(string1, string2, string3, string4, string5, string6):
    string1 = string1 + '-'
    string2 = string2 + '-'
    string3 = string3 + '5'
    string4 = string4 + '5'
    string5 = string5 + '3'
    string6 = string6 + '-'
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
    tuning = args.tuning
    banner = args.banner
    chords = args.Chords
    arglist = list()
    string1 = 'e|'
    string2 = 'B|'
    string3 = 'G|'
    string4 = 'D|'
    string5 = 'A|'
    if tuning == 'dropd':
        string6 = 'D|'
    else:
        string6 = 'E|'
    for chord in chords:
        if chord == ' ':
          string1, string2, string3, string4, string5, string6 = blank(string1, string2, string3, string4, string5, string6)
        if chord == 'a':
          string1, string2, string3, string4, string5, string6 = A(string1, string2, string3, string4, string5, string6)
        if chord == 'b':
          string1, string2, string3, string4, string5, string6 = B(string1, string2, string3, string4, string5, string6)
        if chord == 'c':
          string1, string2, string3, string4, string5, string6 = C(string1, string2, string3, string4, string5, string6)
        if chord == 'e':
          string1, string2, string3, string4, string5, string6 = E(string1, string2, string3, string4, string5, string6)
        if chord == 'f':
          string1, string2, string3, string4, string5, string6 = F(string1, string2, string3, string4, string5, string6)
        if chord == 'g':
          string1, string2, string3, string4, string5, string6 = G(string1, string2, string3, string4, string5, string6)

    string1, string2, string3, string4, string5, string6 = end(string1, string2, string3, string4, string5, string6)
    print banner
    print string1 + string2 + string3 + string4 + string5 + string6
main(args)
