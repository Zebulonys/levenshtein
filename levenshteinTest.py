# -*- coding: utf-8 -*-
__authors__ = "Stéphane Gabillon"

from levenshtein import levenshtein

print("***** Begin ******\n")

print("Levenshtein distance should work on empty strings")
assert(levenshtein(   "",    "") == 0 )
assert(levenshtein(  "a",    "") == 1 )
assert(levenshtein(   "",   "a") == 1 )
assert(levenshtein("abc",    "") == 3 )
assert(levenshtein(   "", "abc") == 3 )
print("Tests passed")
  

print("Levenshtein distance should work on equal strings") 
assert(levenshtein(   "",    "") == 0 )
assert(levenshtein(  "a",   "a") == 0 )
assert(levenshtein("abc", "abc") == 0 )
print("Tests passed")
  

print("Levensthein distance should work where only inserts are needed") 
assert(levenshtein(   "",   "a") == 1 )
assert(levenshtein(  "a",  "ab") == 1 )
assert(levenshtein(  "b",  "ab") == 1 )
assert(levenshtein( "ac", "abc") == 1 )
assert(levenshtein("abcdefg", "xabxcdxxefxgx") == 6 )
print("Tests passed")
  

print("Levenshtein distance should work where only deletes are needed") 
assert(levenshtein(  "a",    "") == 1 )
assert(levenshtein( "ab",   "a") == 1 )
assert(levenshtein( "ab",   "b") == 1 )
assert(levenshtein("abc",  "ac") == 1 )
assert(levenshtein("xabxcdxxefxgx", "abcdefg") == 6 )
print("Tests passed")


print("Levenshtein distance should work where only substitutions are needed") 
assert(levenshtein(  "a",   "b") == 1 )
assert(levenshtein( "ab",  "ac") == 1 )
assert(levenshtein( "ac",  "bc") == 1 )
assert(levenshtein("abc", "axc") == 1 )
print("Tests passed")


print("Levensthein distance should work where many operations are needed")
assert(levenshtein("example", "samples") == 3 )
assert(levenshtein("sturgeon", "urgently") == 6 )
assert(levenshtein("levenshtein", "frankenstein") == 6 )
assert(levenshtein("distance", "difference") == 5 )
print("Tests passed\n")

print("***** End ******")

