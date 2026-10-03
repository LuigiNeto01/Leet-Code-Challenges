from __future__ import annotations
from typing import List, Set, Tuple
import random

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        # We maintain a set of candidate words that could still be the secret.
        candidates: Set[str] = set(words)
        
        while candidates:
            # Choose the next word to guess.
            # Strategy: pick a word that minimizes the maximum group size
            # after partitioning by match count. This heuristic reduces
            # the candidate set quickly (like minimax).
            guess_word = self._choose_best_guess(candidates)
            
            # Call the API to get the number of exact matches.
            matches: int = master.guess(guess_word)
            
            # If we found the secret (6 matches), we are done.
            if matches == 6:
                return
            
            # Filter candidates: keep only words that have exactly `matches`
            # characters in common with the guessed word at the same positions.
            # Words that don't match are impossible to be the secret.
            new_candidates: Set[str] = set()
            for word in candidates:
                if self._match_count(guess_word, word) == matches:
                    new_candidates.add(word)
            candidates = new_candidates
    
    def _match_count(self, a: str, b: str) -> int:
        """Return number of positions where a and b have the same character."""
        # Both strings are length 6 as per problem constraints.
        count: int = 0
        for i in range(6):
            if a[i] == b[i]:
                count += 1
        return count
    
    def _choose_best_guess(self, candidates: Set[str]) -> str:
        """Select a word (from the full original set) that minimizes
        the worst-case size of the largest group when partitioned by
        match count. This reduces the number of guesses needed.
        If candidates are few, just pick any candidate."""
        # If the candidate pool is small, just guess one directly.
        if len(candidates) <= 2:
            return next(iter(candidates))
        
        # Evaluate all words in the original set (not just candidates)
        # because we can guess any word, even if it's not a candidate.
        # We'll use a precomputed list; but we don't have the full list
        # here, so we use candidates as a reasonable approximation.
        best_word: str = ""
        best_max_group: int = float('inf')
        
        # To speed up, we can randomly sample or just evaluate a subset,
        # but for n<=100 it's fine to check all candidates.
        for guess in candidates:
            # Count how many candidates fall into each match-count bucket (0..6)
            group_sizes: List[int] = [0] * 7
            for word in candidates:
                m = self._match_count(guess, word)
                group_sizes[m] += 1
            # The largest group after the guess (ignoring m=6 since that would be perfect)
            max_group = max(group_sizes[:6])  # exclude full match (size at m=6)
            if max_group < best_max_group:
                best_max_group = max_group
                best_word = guess
        
        return best_word