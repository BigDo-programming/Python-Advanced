def palindrome(text, idx):
    if idx == len(text) // 2:
        return f"{text} is a palindrome"
    left = text[idx]
    right = text[len(text) - 1 - idx]

    if left != right:
        return f"{text} is not a palindrome"

    return palindrome(text, idx + 1)


print(palindrome("abcba", 0))
# print(palindrome("peter", 0))
