#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line utility that accepts a word file and prints a dictionary of
anagrams for that file.

Module provides a function find_anagrams which can be used to do the same
for an arbitrary list of strings.
"""

import sys

# Your name here, and any other people/sources who helped.
# Give credit where credit is due.
__author__ = "Cedric Mulvihill"


def alphabetize(string):
    """Returns alphabetized version of the string"""
    return "".join(sorted(string.lower()))


def find_anagrams(words):
    """
    Returns a dictionary with keys that are alphabetized words and values
    that are all words that, when alphabetized, match the key.
    Example:
    {'dgo': ['dog'], 'act': ['cat', 'act']}
    """
    anagrams = {}
    for word in words:
        item = alphabetize(word)
        if item in anagrams:
            anagrams[item].append(word)
        else:
            anagrams[item] = [word]
    return anagrams


def main(args):
    # run find_anagrams() on first argument filename
    if len(args) < 1:
        print("Please specify a word file!")
        sys.exit(1)

    with open(args[0], 'r') as f:
        words = f.read().split()
    anagram_dict = {
        "".join(sorted(word.lower())): [
            w for w in words
            if "".join(sorted(w.lower())) == "".join(sorted(word.lower()))]
        for word in words}
    for k, v in anagram_dict.items():
        print("{} : {}".format(k, v))


if __name__ == "__main__":
    main(sys.argv[1:])
