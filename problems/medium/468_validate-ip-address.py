class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # Check if it could be IPv4 (contains '.')
        if '.' in queryIP:
            return self.validateIPv4(queryIP)
        # Check if it could be IPv6 (contains ':')
        elif ':' in queryIP:
            return self.validateIPv6(queryIP)
        else:
            return "Neither"
    
    def validateIPv4(self, ip: str) -> str:
        # Split by '.' - must have exactly 4 parts
        parts = ip.split('.')
        if len(parts) != 4:
            return "Neither"
        
        for part in parts:
            # Each part must be non-empty
            if not part:
                return "Neither"
            
            # Each part must contain only digits
            if not part.isdigit():
                return "Neither"
            
            # No leading zeros allowed (except for "0" itself)
            if len(part) > 1 and part[0] == '0':
                return "Neither"
            
            # Value must be in range [0, 255]
            num = int(part)
            if num < 0 or num > 255:
                return "Neither"
        
        return "IPv4"
    
    def validateIPv6(self, ip: str) -> str:
        # Split by ':' - must have exactly 8 parts
        parts = ip.split(':')
        if len(parts) != 8:
            return "Neither"
        
        for part in parts:
            # Each part must be non-empty and length between 1 and 4
            if not part or len(part) > 4:
                return "Neither"
            
            # Each character must be a valid hexadecimal digit
            for char in part:
                if not (char.isdigit() or char in 'abcdefABCDEF'):
                    return "Neither"
        
        return "IPv6"