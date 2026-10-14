class Solution:
    def maskPII(self, s: str) -> str:
        # Check if input is an email (contains '@')
        if '@' in s:
            return self._mask_email(s)
        else:
            return self._mask_phone(s)
    
    def _mask_email(self, s: str) -> str:
        """Mask an email address following the rules."""
        # Convert everything to lowercase
        s_lower = s.lower()
        
        # Split into name and domain at '@'
        at_index = s_lower.index('@')
        name = s_lower[:at_index]
        domain = s_lower[at_index:]  # includes '@' and everything after
        
        # First character of name + "*****" + last character of name + domain
        # Even if name has only 2 chars, still insert 5 asterisks in middle
        masked = name[0] + "*****" + name[-1] + domain
        return masked
    
    def _mask_phone(self, s: str) -> str:
        """Mask a phone number following the rules."""
        # Extract all digits from the string
        digits = [ch for ch in s if ch.isdigit()]
        num_digits = len(digits)
        
        # Last 4 digits are the local number ending
        last_four = ''.join(digits[-4:])
        
        # Determine country code length
        if s.startswith('+'):
            # Count consecutive digits immediately after the '+'
            count = 0
            for ch in s[1:]:
                if ch.isdigit():
                    count += 1
                else:
                    break
            # If there are more than 10 digits, standard rule applies
            if num_digits > 10:
                country_len = num_digits - 10
            else:
                # Total digits is 10, but leading '+' indicates a country code
                country_len = count
        else:
            # No plus sign: country code exists only if digits exceed 10
            country_len = num_digits - 10 if num_digits > 10 else 0
        
        # Build the masked number based on country code length
        if country_len == 0:
            return f"***-***-{last_four}"
        elif country_len == 1:
            return f"+*-***-***-{last_four}"
        elif country_len == 2:
            return f"+**-***-***-{last_four}"
        else:  # 3 digits (any larger values are clamped)
            return f"+***-***-***-{last_four}"