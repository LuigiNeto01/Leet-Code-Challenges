import string
import random

class Solution:
    """Encode and decode URLs using a random 6-character key."""
    
    def __init__(self):
        self.base_url = "http://tinyurl.com/"
        self.short_to_long = {}
        self.long_to_short = {}
        self.alphabet = string.ascii_letters + string.digits
        self.key_len = 6

    def encode(self, longUrl: str) -> str:
        if longUrl in self.long_to_short:
            return self.base_url + self.long_to_short[longUrl]
        while True:
            key = ''.join(random.choice(self.alphabet) for _ in range(self.key_len))
            if key not in self.short_to_long:
                break
        self.short_to_long[key] = longUrl
        self.long_to_short[longUrl] = key
        return self.base_url + key

    def decode(self, shortUrl: str) -> str:
        key = shortUrl[len(self.base_url):]
        return self.short_to_long[key]