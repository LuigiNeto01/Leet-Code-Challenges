class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0  # Track minimum frequency for eviction
        self.key_to_val = {}  # key -> value mapping
        self.key_to_freq = {}  # key -> frequency mapping
        self.freq_to_keys = {}  # frequency -> OrderedDict of keys (for LRU within same frequency)
        
    def _update_freq(self, key: int) -> None:
        # Update frequency of a key and move it to appropriate frequency bucket
        freq = self.key_to_freq[key]
        
        # Remove key from current frequency bucket
        del self.freq_to_keys[freq][key]
        
        # If current frequency bucket is empty and it's the min_freq, increment min_freq
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
            
        # Increment frequency
        new_freq = freq + 1
        self.key_to_freq[key] = new_freq
        
        # Add key to new frequency bucket (most recently used, so at end)
        if new_freq not in self.freq_to_keys:
            self.freq_to_keys[new_freq] = {}
        self.freq_to_keys[new_freq][key] = None  # Using dict as OrderedDict
        
    def get(self, key: int) -> int:
        # Return -1 if key doesn't exist
        if key not in self.key_to_val:
            return -1
        
        # Update frequency since key was accessed
        self._update_freq(key)
        
        return self.key_to_val[key]
    
    def put(self, key: int, value: int) -> None:
        # Edge case: capacity 0
        if self.capacity <= 0:
            return
        
        # If key exists, update value and frequency
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update_freq(key)
            return
        
        # If cache is full, evict LFU (and LRU among LFU)
        if len(self.key_to_val) >= self.capacity:
            # Get the least recently used key from min_freq bucket
            # In Python 3.7+, dict maintains insertion order, first key is LRU
            lru_key = next(iter(self.freq_to_keys[self.min_freq]))
            
            # Remove from all data structures
            del self.freq_to_keys[self.min_freq][lru_key]
            del self.key_to_val[lru_key]
            del self.key_to_freq[lru_key]
        
        # Insert new key with frequency 1
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.min_freq = 1  # New key always has frequency 1
        
        # Add to frequency bucket
        if 1 not in self.freq_to_keys:
            self.freq_to_keys[1] = {}
        self.freq_to_keys[1][key] = None