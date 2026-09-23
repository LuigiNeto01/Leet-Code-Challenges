from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        # Map file content -> list of full file paths
        content_to_paths = defaultdict(list)

        for entry in paths:
            parts = entry.split()
            directory = parts[0]

            # Each remaining token is a "filename(content)" entry
            for file_token in parts[1:]:
                open_pos = file_token.index('(')
                file_name = file_token[:open_pos]
                content = file_token[open_pos + 1:-1]  # strip closing ')'

                full_path = directory + '/' + file_name
                content_to_paths[content].append(full_path)

        # Only keep contents that appear in at least two files
        return [
            paths
            for paths in content_to_paths.values()
            if len(paths) >= 2
        ]