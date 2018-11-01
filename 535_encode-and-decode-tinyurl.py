#coding=utf-8

import string
import random
import math
full_tiny = {}
tiny_full = {}
letters = string.ascii_letters + string.digits

class Codec:
    def encode(self, longUrl):
        def six_addr():
            ans = ''
            for i in range(6):
                tmp = letters[random.randint(0, 10000)%62]
                ans = ans+tmp
            return ans
        if longUrl in full_tiny:
            return "http://tinyurl.com/" + full_tiny[longUrl]
        else:
            suffix = six_addr()
            full_tiny[longUrl]=suffix
            tiny_full[suffix] = longUrl
            return "http://tinyurl.com/" + suffix

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in tiny_full:
            return tiny_full[shortUrl]
        else:
            return None

# Your Codec object will be instantiated and called as such:
codec = Codec()
url = 'http://www.baidu.com'
print codec.encode(url)
print codec.decode(codec.encode(url))

