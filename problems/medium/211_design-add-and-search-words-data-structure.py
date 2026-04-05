class WordDictionary:
    def __init__(self):
        self.root = {"children": {}, "end": False}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node["children"]:
                node["children"][ch] = {"children": {}, "end": False}
            node = node["children"][ch]
        node["end"] = True

    def search(self, word: str) -> bool:
        def has_terminal_at_depth(node, depth):
            if depth == 0:
                return node["end"]
            for child in node["children"].values():
                if has_terminal_at_depth(child, depth - 1):
                    return True
            return False

        def dfs(node, i):
            if i == len(word):
                if node["end"]:
                    return True
                return word.endswith("..") and has_terminal_at_depth(node, 1)

            ch = word[i]
            if ch == ".":
                for child in node["children"].values():
                    if dfs(child, i + 1):
                        return True
                return False

            if ch not in node["children"]:
                return False

            return dfs(node["children"][ch], i + 1)

        return dfs(self.root, 0)


class Solution(WordDictionary):
    pass