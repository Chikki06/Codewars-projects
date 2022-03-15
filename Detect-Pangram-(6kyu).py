#Problem Statement
#A pangram is a sentence that contains every single letter of the alphabet at least once.
#For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
#Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
#
#Code

import string

def is_pangram(s):
    s = s.lower()
    s = "".join(c for c in s if c.isalpha())
    alphabet = {}
    for char in string.ascii_lowercase:
        alphabet[char] = 0
    for letter in s:
        val = alphabet[str(letter)]
        alphabet[str(letter)] = val+1
    if min(alphabet.values()) == 0:
        return False
    else:
        return True
# A better solution:
# import string
#
# def is_pangram(s):
#     s = s.lower()
#     for char in 'abcdefghijklmnopqrstuvwxyz':
#         if char not in s:
#             return False
#     return True
