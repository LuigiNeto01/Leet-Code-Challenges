from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # If endGene is not in bank, mutation is impossible
        if endGene not in bank:
            return -1
        
        # Convert bank to set for O(1) lookup
        bank_set = set(bank)
        
        # BFS to find shortest path from startGene to endGene
        queue = deque([(startGene, 0)])  # (current_gene, mutations_count)
        visited = {startGene}
        genes = ['A', 'C', 'G', 'T']
        
        while queue:
            current_gene, mutations = queue.popleft()
            
            # If we reached the target, return the number of mutations
            if current_gene == endGene:
                return mutations
            
            # Try mutating each position in the gene string
            for i in range(len(current_gene)):
                # Try each possible character at position i
                for gene_char in genes:
                    # Skip if same character (no mutation)
                    if gene_char == current_gene[i]:
                        continue
                    
                    # Create mutated gene
                    mutated_gene = current_gene[:i] + gene_char + current_gene[i+1:]
                    
                    # Check if mutation is valid (in bank) and not visited
                    if mutated_gene in bank_set and mutated_gene not in visited:
                        visited.add(mutated_gene)
                        queue.append((mutated_gene, mutations + 1))
        
        # If we exhausted all possibilities without reaching endGene
        return -1