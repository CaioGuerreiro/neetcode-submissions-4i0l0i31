class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stack = []
        word = []
        s = s.strip()

        for i in range(len(s)):
            stack.append(s[i])
        
        for i in range(len(s)):
            
            word.append(stack[-1])
            stack.pop()
            print(word)
            if stack and stack[-1] == " ":
                return len(word)
        return len(word)
        
