class Solution:
    def encode(self, strs: List[str]) -> str:
        # If the list is empty, return a specific unique marker
        if not strs:
            return "EMPTY_LIST"
        
        # Use a non-printable character that won't exist in standard text
        return "\x1e".join(strs)

    def decode(self, s: str) -> List[str]:
        # Check for our unique empty list marker
        if s == "EMPTY_LIST":
            return []
            
        # Splitting automatically recreates [""] or normal strings perfectly
        return s.split("\x1e")