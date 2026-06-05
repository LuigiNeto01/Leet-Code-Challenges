from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Use a Trie (prefix tree) to store binary representations of numbers
        # This allows efficient bit-by-bit comparison to find max XOR
        
        class TrieNode:
            def __init__(self):
                self.children = {}  # Maps bit (0 or 1) to child node
        
        # Build the trie with all numbers
        root = TrieNode()
        for num in nums:
            node = root
            # Process each bit from MSB to LSB (31 bits for 32-bit integers)
            for i in range(31, -1, -1):
                bit = (num >> i) & 1  # Extract the i-th bit
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        max_xor = 0
        
        # For each number, try to find the number that gives max XOR
        for num in nums:
            node = root
            current_xor = 0
            
            # For each bit position, try to go opposite direction
            # (to maximize XOR, we want different bits)
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                # Try to take the opposite bit to maximize XOR
                toggled_bit = 1 - bit
                
                if toggled_bit in node.children:
                    # We can take the opposite bit - XOR will be 1 at this position
                    current_xor |= (1 << i)  # Set the i-th bit in result
                    node = node.children[toggled_bit]
                else:
                    # Must take the same bit - XOR will be 0 at this position
                    node = node.children[bit]
            
            max_xor = max(max_xor, current_xor)
        
        return max_xor