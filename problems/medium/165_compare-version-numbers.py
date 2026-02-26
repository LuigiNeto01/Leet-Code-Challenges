class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split versions into list of revision strings
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')

        # Use max length so we can compare all revisions, padding with 0 when missing
        max_len = max(len(v1_parts), len(v2_parts))

        for i in range(max_len):
            # Convert each revision to int, missing revisions treated as 0
            rev1 = int(v1_parts[i]) if i < len(v1_parts) else 0
            rev2 = int(v2_parts[i]) if i < len(v2_parts) else 0

            # Compare current revisions
            if rev1 < rev2:
                return -1
            if rev1 > rev2:
                return 1

        # All revisions equal after normalization
        return 0