class Solution:
    @staticmethod
    def tenth_line() -> None:
        import sys

        try:
            with open("file.txt", "r") as f:
                for idx, line in enumerate(f, start=1):
                    if idx == 10:
                        sys.stdout.write(line)
                        return
        except FileNotFoundError:
            pass