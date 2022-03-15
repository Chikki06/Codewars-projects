import string

def is_pangram(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
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
