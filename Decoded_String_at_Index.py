class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_length = 0
        
        # Calculate the total length of the decoded string
        for c in s:
            if c.isdigit():
                # If the character is a digit, adjust the total length
                # by multiplying it with the numeric value.
                total_length *= int(c)
            else:
                # If the character is an alphabet character, simply increment
                # the total length by 1 to account for the character itself.
                total_length += 1
        
        # Traverse the string in reverse to find the character at position k
        for c in reversed(s):
            k %= total_length  # Reduce k based on the current total length
            
            if k == 0 and c.isalpha():
                # If k becomes 0, and the current character is an alphabet character,
                # it means we've reached the desired position k, so return this character.
                return c
            
            if c.isdigit():
                # If the character is a digit, adjust the total length by dividing it
                # by the numeric value. This effectively "undo" the repetition of characters.
                total_length //= int(c)
            else:
                # If the character is an alphabet character, decrement the total length
                # by 1 to account for this character.
                total_length -= 1
        
        return ""  # This line should not be reached, but added for completeness