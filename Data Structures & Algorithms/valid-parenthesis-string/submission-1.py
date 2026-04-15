class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        #time O(n) space O(n)
        for i, ch in enumerate(s):
            if ch == "(":
                left.append(i)
            elif ch == "*":
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()
        
        while left and star:
            if left.pop() > star.pop():
                return False
        return not left

"""
1. create 2 stacks called left and star
2. populate left with the number of (
3. populate star with the number of *
4. if ) appears pop from left or star
5. if ) appears and left and star are empty  return False
6. if has ( and star and has more ( than * return False
7. otherwise return not left

"""
        