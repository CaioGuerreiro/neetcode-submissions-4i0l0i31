class Solution:
    def climbStairs(self, n: int) -> int:
        """
        versão usando backtracking
        eu pensei isso inicialmente
        complexidade de tempo = O(2^n)
        complexidade de espaço = O(n)
        """
        # def dfs(i):
        #     if i >= n:
        #         return i == n
            
        #     return dfs(i + 1) + dfs(i + 2)
        
        # return dfs(0)

        """
        versão otimizada
        complexidade de tempo = O(n)
        complexidade de espaço = O(1)

        """
        # one = 1
        # two = 1

        # for i in range(n - 1):
        #     temp = one
        #     one = one + two
        #     two = temp

        # return one

        """
        versão mais otimizada
        complexidade tempo = O(log n)
        complexidade espaço = O(1)
        """
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        n += 1
        return round((phi**n - psi**n) / sqrt5)


        