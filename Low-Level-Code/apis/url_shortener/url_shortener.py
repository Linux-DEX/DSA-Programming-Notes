class UrlShortener:
    """
    Map a long URL to a short code and back.

    The same URL always returns the code issued the first time.
    Codes are base62 encodings of an increasing counter.

    ponytail: the counter and both maps are in memory.
    A real shortener persists them and starts the counter from stored state.
    """

    _ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self._by_code = {}
        self._by_url = {}
        self._next = 1

    def shorten(self, url):
        code = self._by_url.get(url)
        if code is not None:
            return code
        code = self._encode(self._next)
        self._next += 1
        self._by_code[code] = url
        self._by_url[url] = code
        return code

    def resolve(self, code):
        return self._by_code.get(code)

    def _encode(self, number):
        chars = []
        base = len(self._ALPHABET)
        while number:
            number, rem = divmod(number, base)
            chars.append(self._ALPHABET[rem])
        return "".join(reversed(chars))
