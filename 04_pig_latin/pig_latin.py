import re

def translate(msg):
    arry = re.compile('\s+').split(msg)
    buffer = ''
    for word in arry:
        if len(buffer) > 0:
            # append separator if there's an existing word
            buffer += ' '
        buffer += translate_word(word)
    return buffer

#
# internal
#

def find_longest_consonant_prefix(word, maxlen=3):
    buffer = ''
    ii = 0
    while ii < len(word):
        # special case phonemes
        phoneme = word[ii:ii+2]
        if phoneme == 'qu' or phoneme == 'Qu':
            buffer += phoneme
            ii += 2

        # normal consonants
        else:
            letter = word[ii]
            if is_vowel(letter):
                break
            else:
                buffer += letter
                ii += 1
    return buffer

def first_letter(word):
    return word[:1]

def is_capitalized(word):
    first_letter = word[0]
    return first_letter == first_letter.capitalize()

def is_vowel(letter):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return letter in vowels

def remaining_letters(word, count=1):
    return word[count:]

def translate_word(word_plus):
    match = re.compile('^([A-Za-z]+)(.*)').match(word_plus)
    word = match[1]
    punctuation = match[2]

    consonants = find_longest_consonant_prefix(word)
    clength = len(consonants)
    if clength == 0:
        return word + 'ay' + punctuation
    else:
        remainder = word[clength:]
        if is_capitalized(word):
            remainder = remainder.capitalize()
            consonants = consonants.lower()
        return remainder + consonants + 'ay' + punctuation

