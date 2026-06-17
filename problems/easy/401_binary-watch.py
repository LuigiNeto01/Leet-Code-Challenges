from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        # Iterate through all possible hour and minute combinations
        for h in range(12):  # Hours: 0-11
            for m in range(60):  # Minutes: 0-59
                # Count the number of 1s in binary representation of hour and minute
                # bin(x).count('1') counts the number of set bits
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    # Format: hour without leading zero, minute with leading zero if needed
                    result.append(f"{h}:{m:02d}")
        
        return result