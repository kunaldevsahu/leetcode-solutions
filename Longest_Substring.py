def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()  # To store characters in the current window
    left = 0  # Left boundary of the window
    max_length = 0  # Maximum length found

    for right in range(len(s)):
        # If the character is already in the set, move the left boundary
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # Add the current character to the set
        char_set.add(s[right])
        # Update the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

s = str(input())
result = lengthOfLongestSubstring(s)
print(result)