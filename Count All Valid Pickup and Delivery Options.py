class Solution:
    def countOrders(self, n: int) -> int:
        mod = pow(10, 9) + 7

        def traverse(index, spots):
            if index <= 0 or spots <= 0:
                return 1

            val = (spots * (spots-1))//2
            return val *  traverse(index-1, spots -2)

        return traverse(n, n*2) % mod
