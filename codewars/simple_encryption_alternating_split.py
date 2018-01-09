"""
For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)
For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.
"""


def decrypt(text, n):
    if text in (None, ''): return text

    h = len(text) // 2
    for i in range(n):
        o, p = text[:h], text[h:]
        text = ''.join([p[j:j+1] + o[j:j+1] for j in range(h+1)])
    return text


def encrypt(text, n):
    if text in (None, ''): return text

    for _ in range(n):
        text = text[1::2] + text[::2]
    return text
