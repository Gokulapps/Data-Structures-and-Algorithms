def identifyPalindrome(word, word_length, left, right, longestPalindrome, palindromeLen):
    while left > 0 and right < word_length and word[left] == word[right]:
        if (right-left)+1 > palindromeLen:
           longestPalindrome = word[left:right+1] 
           palindromeLen = (right - left) + 1
        left -= 1
        right += 1
    return longestPalindrome, palindromeLen

def palindromicString(word): 
    word_length = len(word)
    longestPalindrome = ""
    palindromeLen = 0
    for i in range(word_length):
        left, right = i, i
        longestPalindrome, palindromeLen = identifyPalindrome(word, word_length, left, right, longestPalindrome, palindromeLen)
        left, right = i, i+1
        longestPalindrome, palindromeLen = identifyPalindrome(word, word_length, left, right, longestPalindrome, palindromeLen)
    
    return longestPalindrome
    
word = "gdgdababawnknwkw"
longestPalindrome = palindromicString(word)
print(f'The Longest Palindrome found in the given string `{word}` is: ', longestPalindrome)
