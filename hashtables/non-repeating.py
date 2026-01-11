def first_non_repeating_char(string):
    # Dictionary to store the frequency of each character
    char_counts = {}
    
    # First pass: Count occurrences of each character
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # Second pass: Find the first character with a count of 1
    for char in string:
        if char_counts[char] == 1:
            return char
            
    # Return None if no non-repeating character exists
    return None


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""