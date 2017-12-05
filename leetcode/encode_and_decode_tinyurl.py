"""
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it
returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode
algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded
to the original URL.
"""


class Codec:
    def __init__(self):
        self.url_pairs = {}
        self.short_to_long = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]

        rand = self.gen_random_url(6)
        while rand in self.short_to_long:
            rand = self.gen_random_url(6)

        self.long_to_short[longUrl] = rand
        self.short_to_long[rand] = longUrl
        return rand

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.short_to_long.get(shortUrl, None)


    @staticmethod
    def gen_random_url(length):
        import string
        import random
        base = 'http://tinyurl.com/'
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return base + ''.join(random.SystemRandom().choice(chars) for _ in range(length))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))