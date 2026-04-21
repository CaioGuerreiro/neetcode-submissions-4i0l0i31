class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        
        #[1, 2, 3, 4, 5, 6, 7, 8, 9]
        #       m  r            
        while left <= right:
            mid = (left + right) // 2
            square = mid ** 2

            if square > num:
                right = mid - 1
            elif square < num:
                left = mid + 1
            elif square == num:
                return True
        return False 