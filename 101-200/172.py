class Solution:
    def trailingZeroes(self, n: int) -> int:
        # allocate one extra slot so we can use indices 1..n
        mem_fives = [0] * (n + 1)
        mem_twos = [0] * (n + 1)

        def count_factors(k: int, p: int, cache: list[int]) -> int:
            """Count exponent of prime p in k and memoise all intermediate k."""
            ans, path = 0, []
            while k % p == 0:
                path.append((k, ans))
                k //= p
                ans += 1
            for val, prefix in path:
                cache[val] = ans - prefix        # fill the cache correctly
            return ans

        twos = fives = 0
        for i in range(1, n + 1):
            twos += mem_twos[i] or count_factors(i, 2, mem_twos)
            fives += mem_fives[i] or count_factors(i, 5, mem_fives)
        return min(twos, fives)


if __name__ == "__main__":
    s = Solution()
    print(s.trailingZeroes(5))  # Output: 1
    print(s.trailingZeroes(10))  # Output: 2
    print(s.trailingZeroes(25))  # Output: 6
    print(s.trailingZeroes(100))  # Output: 24
    print(s.trailingZeroes(1000))  # Output: 249
