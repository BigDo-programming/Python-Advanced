def palindrome(word, index):
    if index >= len(word) // 2:
        return f"{word} is a palindrome"

    word2 = word[::-1]
    if word[index] == word2[index]:

        return palindrome(word, index + 1)

    else:
        return f"{word} is not a palindrome"

print(palindrome("abcba", 0))
print(palindrome("peter", 0))





# def palindrome(text, idx):
#     if idx == len(text) // 2:
#         return f"{text} is a palindrome"
#     left = text[idx]
#     right = text[len(text) - 1 - idx]
#
#     if left != right:
#         return f"{text} is not a palindrome"
#
#     return palindrome(text, idx + 1)
