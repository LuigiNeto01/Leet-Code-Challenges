class WordFilter:
    def __init__(self, words: list[str]):
        # Precompute a mapping from every (prefix, suffix) pair to the largest
        # word index that matches both. Each word has length <= 7, so this is cheap.
        self.mapping = {}

        for idx, word in enumerate(words):
            L = len(word)
            # Generate all non-empty prefixes and suffixes of this word.
            for i in range(1, L + 1):
                prefix = word[:i]
                for j in range(1, L + 1):
                    suffix = word[-j:]
                    # Later indices overwrite earlier ones, so no extra max() is needed.
                    self.mapping[(prefix, suffix)] = idx

    def f(self, pref: str, suff: str) -> int:
        # O(1) lookup for the required prefix/suffix pair.
        return self.mapping.get((pref, suff), -1)