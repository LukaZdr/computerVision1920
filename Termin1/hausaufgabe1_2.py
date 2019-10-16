#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:33:24 2019
Scrabble

"""
#Aufgabe2

werte = {"a": 1, "b": 3, "c": 4, "d": 1, "e": 1, "f": 4, "g": 2,"h": 2, "i": 1, "j": 6, "k": 4, "l": 2, "m": 3, "n": 1, "o":2, "p": 4, "q": 10, 
         "r": 1, "s": 1, "t": 1, "u": 1, "v": 6, "w": 3, "x": 8, "y": 10, "z": 3, "ä": 6, "ö": 8, "ü": 6}

def scrabble(word):
    scrabble_wert = 0
    for char in word:
         scrabble_wert += werte[char]
    return scrabble_wert
    
