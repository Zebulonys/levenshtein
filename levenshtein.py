# -*- coding: utf-8 -*-
__authors__ = "Stéphane Gabillon"

def levenshtein(firstWord, secondWord):
    if firstWord == "":
        return len(secondWord)
    if secondWord == "":
        return len(firstWord)
    if firstWord[-1] == secondWord[-1]:
        cost = 0
    else:
        cost = 1
       
    levenshteinDistance = min([levenshtein(firstWord[:-1], secondWord) + 1,
                               levenshtein(firstWord, secondWord[:-1]) + 1, 
                               levenshtein(firstWord[:-1], secondWord[:-1]) + cost])

    return levenshteinDistance