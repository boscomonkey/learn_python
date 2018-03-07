import re

def echo(msg):
    return msg

def first_word(msg):
    arry = re.compile('\s+').split(msg)
    return arry[0]

def repeat(msg, num=2):
    buffer = ''
    counter = 0
    while counter < num:
        buffer += msg
        if counter < num-1:
            buffer += ' ' 
        counter += 1
    return buffer

def shout(msg):
    return msg.upper()

def start_of_word(msg, count):
    return msg[0:count]

def titleize(msg):
    arry = re.compile('\s+').split(msg)
    buffer = ''
    ii = 0
    num = len(arry)
    while ii < num:
        word = arry[ii]

        if is_little(word) and ii > 0:
            buffer += word
        else:
            buffer += word.capitalize()

        if ii < num-1:
            buffer += ' ' 
        ii += 1
    return buffer

def is_little(word):
    set = {
        "and",
        "over",
        "the"
        }
    return word in set
