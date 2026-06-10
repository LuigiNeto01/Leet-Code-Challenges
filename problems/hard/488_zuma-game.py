from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove_consecutive(s):
            while True:
                new_s = ""
                i = 0
                changed = False
                while i < len(s):
                    j = i
                    while j < len(s) and s[j] == s[i]:
                        j += 1
                    if j - i < 3:
                        new_s += s[i:j]
                    else:
                        changed = True
                    i = j
                if not changed:
                    break
                s = new_s
            return s
        
        memo = {}
        
        def dfs(board_state, hand_counter):
            if not board_state:
                return 0
            
            hand_tuple = tuple(sorted(hand_counter.items()))
            key = (board_state, hand_tuple)
            if key in memo:
                return memo[key]
            
            if sum(hand_counter.values()) == 0:
                return float('inf')
            
            result = float('inf')
            
            # Try inserting each available color at each position
            for i in range(len(board_state) + 1):
                for color in hand_counter:
                    if hand_counter[color] > 0:
                        # Insert the ball at position i
                        new_board = board_state[:i] + color + board_state[i:]
                        new_board = remove_consecutive(new_board)
                        
                        # Skip if nothing changed (no point in this move)
                        if new_board == board_state:
                            continue
                        
                        new_hand = hand_counter.copy()
                        new_hand[color] -= 1
                        
                        steps = dfs(new_board, new_hand)
                        if steps != float('inf'):
                            result = min(result, steps + 1)
            
            memo[key] = result
            return result
        
        hand_counter = Counter(hand)
        result = dfs(board, hand_counter)
        
        return result if result != float('inf') else -1