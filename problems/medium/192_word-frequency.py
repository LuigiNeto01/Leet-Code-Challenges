# This is a bash/shell scripting problem, not a Python problem
# However, if we were to solve the word frequency counting logic in Python:

from collections import Counter

def word_frequency(filename):
    # Read all words from file
    with open(filename, 'r') as f:
        text = f.read()
    
    # Split by whitespace and count frequencies
    words = text.split()
    counter = Counter(words)
    
    # Sort by frequency (descending) then by word (for stability)
    sorted_words = sorted(counter.items(), key=lambda x: -x[1])
    
    # Print results
    for word, count in sorted_words:
        print(f"{word} {count}")

# For LeetCode shell problem, the actual solution is a bash one-liner:
# cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{print $2, $1}'