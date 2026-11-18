from __future__ import annotations
from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # Map each required skill to a bit index (0-based)
        skill_to_bit = {skill: i for i, skill in enumerate(req_skills)}
        n = len(req_skills)          # number of required skills (<=16)
        m = len(people)              # number of people (<=60)
        
        # Precompute bitmask for each person: which required skills they cover
        person_masks = [0] * m
        for i, skills in enumerate(people):
            mask = 0
            for s in skills:
                if s in skill_to_bit:
                    mask |= 1 << skill_to_bit[s]
            person_masks[i] = mask
        
        total_masks = 1 << n
        INF = float('inf')
        
        # dp[mask] = smallest team size to achieve 'mask' of required skills
        dp = [INF] * total_masks
        dp[0] = 0
        
        # prev[mask] = (previous_mask, person_index) for reconstruction
        prev = [(-1, -1)] * total_masks
        
        # Standard DP over masks: for each mask, try adding each person
        for mask in range(total_masks):
            if dp[mask] == INF:
                continue
            # Current team size
            cur_size = dp[mask]
            for i, p_mask in enumerate(person_masks):
                new_mask = mask | p_mask
                # If adding person i improves the team size for new_mask
                if cur_size + 1 < dp[new_mask]:
                    dp[new_mask] = cur_size + 1
                    prev[new_mask] = (mask, i)
        
        # Reconstruct the team by backtracking from full mask
        full_mask = (1 << n) - 1
        team = []
        mask = full_mask
        while mask != 0:
            prev_mask, person_idx = prev[mask]
            team.append(person_idx)
            mask = prev_mask
        # We added people in reverse order (since we backtracked), reverse to original order
        team.reverse()
        return team