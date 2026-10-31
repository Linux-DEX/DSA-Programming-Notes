from url_shortener import UrlShortener


def main():
    shortener = UrlShortener()
    first = shortener.shorten("https://example.com/cache")
    again = shortener.shorten("https://example.com/cache")
    other = shortener.shorten("https://example.com/locks")
    print(first, shortener.resolve(first))
    print(other, shortener.resolve(other))
    assert first == again
    assert first != other
    assert shortener.resolve(first) == "https://example.com/cache"
    assert shortener.resolve("missing") is None


if __name__ == "__main__":
    main()
