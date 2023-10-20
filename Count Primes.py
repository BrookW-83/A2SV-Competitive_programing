class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0    
        prime = [True] * (n)
        prime[0] = prime[1] = False

        count = 0
        i = 2
        while i * i < n:
            if prime[i] == True:
                j = i * i
                while j < n:
                    prime[j] = False
                    j += i
            if  i == 2:
                i += 1
            elif i > 2:
                i += 2

        for i in range(len(prime)):
            if prime[i] == True:
                count += 1

        return count

