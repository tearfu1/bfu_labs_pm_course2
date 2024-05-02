import functools

def rabin_karp(text, st):
    if len(st) > len(text):
        return -1 
    BASE = 33
    text_hash = functools.reduce(lambda h, c: h * BASE + ord(c), text[:len(st)], 0)
    st_hash = functools.reduce(lambda h, c: h * BASE + ord(c), st, 0)
    power_st = BASE**max(len(st) - 1, 0) 
    for i in range(len(st), len(text)):
        if text_hash == st_hash and text[i - len(st):i] == st:
            return i - len(st) 
        text_hash -= ord(text[i - len(st)]) * power_st
        text_hash = text_hash * BASE + ord(text[i])
    if text_hash == st_hash and text[-len(st):] == st:
        return len(text) - len(st)
    return -1 

text = "ABASABAGHSDJLKBVILASJ"
st = "BAS"
print(rabin_karp(text, st))