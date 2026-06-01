# This is a bash/shell scripting problem, not a Python problem
# The problem asks for a bash one-liner to filter valid phone numbers from a text file
# 
# Valid formats:
# - (xxx) xxx-xxxx
# - xxx-xxx-xxxx
# where x is a digit
#
# Since this is meant to be solved with bash/grep/awk/sed, here's the bash solution:
# grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
#
# Or using egrep:
# grep -E '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt
#
# However, since this template expects Python code, here's a Python equivalent
# that would process the file if it were a Python problem:

import re
import sys

def validate_phone_numbers():
    # Pattern matches either (xxx) xxx-xxxx or xxx-xxx-xxxx
    # ^                  - start of line
    # (                  - start group
    #   \([0-9]{3}\)     - match (xxx) with literal parens
    #   [ ]              - match exactly one space
    #   |                - OR
    #   [0-9]{3}-        - match xxx-
    # )                  - end group
    # [0-9]{3}-[0-9]{4}  - match xxx-xxxx
    # $                  - end of line
    pattern = r'^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'
    
    try:
        with open('file.txt', 'r') as f:
            for line in f:
                line = line.rstrip('\n')  # Remove newline, keep other content as-is
                if re.match(pattern, line):
                    print(line)
    except FileNotFoundError:
        pass

# For LeetCode shell problems, this Python code won't be tested
# The actual solution is the bash command above