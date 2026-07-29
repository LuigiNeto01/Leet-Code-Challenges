class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        path_lengths = {-1: 0}
        max_length = 0
        
        for line in lines:
            depth = line.count('\t')
            name = line.lstrip('\t')
            
            if depth == 0:
                current_length = len(name)
            else:
                current_length = path_lengths[depth - 1] + len(name)
            
            if '.' in name:
                max_length = max(max_length, current_length)
            else:
                path_lengths[depth] = current_length + 1
        
        return max_length