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
    if n <= 0 or text is None or len(text) < 1: return text

    def decrypted(t):
        h = int(len(t)/2)
        o, p = t[:h], t[h:]
        return ''.join([''.join([p[i] if i < len(p) else '', o[i] if i < len(o) else '']) for i in range(h+1)])
    return decrypt((decrypted(text)), n-1)


def encrypt(text, n):
    if n <= 0 or text is None or len(text) < 1: return text

    def encrypted(t):
        return ''.join(t[1::2]) + ''.join(t[::2])
    return encrypt((encrypted(text)), n-1)
