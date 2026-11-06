class MagicDictionary:
    def __init__(self):
        self.words = []
        self.word_set = set()

    def buildDict(self, dictionary: list[str]) -> None:
        self.words = dictionary[:]
        self.word_set = set(dictionary)

    def search(self, searchWord: str) -> bool:
        if searchWord in self.word_set:
            return False

        for word in self.words:
            if len(word) != len(searchWord):
                continue

            diff = 0
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    diff += 1
                    if diff > 1:
                        break

            if diff == 1:
                return True

        return False