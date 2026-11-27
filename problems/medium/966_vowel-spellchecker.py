from __future__ import annotations

class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        # Exact match set (case-sensitive)
        perfect = set(wordlist)

        # Case-insensitive map: lowercase -> first occurrence
        cap_map = {}
        for w in wordlist:
            lower = w.lower()
            if lower not in cap_map:
                cap_map[lower] = w

        # Vowel error map: devoweled key -> first occurrence
        def devowel(s: str) -> str:
            vowels = set('aeiou')
            result = []
            for ch in s.lower():
                if ch in vowels:
                    result.append('*')
                else:
                    result.append(ch)
            return ''.join(result)

        vowel_map = {}
        for w in wordlist:
            key = devowel(w)
            if key not in vowel_map:
                vowel_map[key] = w

        answer = []
        for q in queries:
            # For all-uppercase queries we prefer case-insensitive match over exact
            if q.isupper():
                lower_q = q.lower()
                if lower_q in cap_map:
                    answer.append(cap_map[lower_q])
                    continue
                devoweled_q = devowel(q)
                if devoweled_q in vowel_map:
                    answer.append(vowel_map[devoweled_q])
                    continue
                if q in perfect:
                    answer.append(q)
                    continue
                answer.append("")
            else:
                # Standard precedence: exact -> case-insensitive -> vowel
                if q in perfect:
                    answer.append(q)
                    continue
                lower_q = q.lower()
                if lower_q in cap_map:
                    answer.append(cap_map[lower_q])
                    continue
                devoweled_q = devowel(q)
                if devoweled_q in vowel_map:
                    answer.append(vowel_map[devoweled_q])
                    continue
                answer.append("")

        return answer