from collections import Counter
import math
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return n

        param_counter = Counter()

        # Count every pair (i<j) by its exact integer line‐key (A,B,C)
        for i, (x1, y1) in enumerate(points[:-1]):
            for x2, y2 in points[i+1:]:
                A = y2 - y1
                B = x1 - x2
                C = x2*y1 - x1*y2

                # Divide out common factor
                g = gcd(gcd(abs(A), abs(B)), abs(C))
                if g:
                    A //= g
                    B //= g
                    C //= g

                # Fix sign so (A,B) is lexicographically non-negative
                if A < 0 or (A == 0 and B < 0):
                    A, B, C = -A, -B, -C

                param_counter[(A, B, C)] += 1

        # Find the maximum number of pairs on any single line
        max_pairs = max(param_counter.values(), default=0)

        # Invert k*(k−1)/2 = max_pairs  →  k = (1 + √(1 + 8·max_pairs)) / 2
        return int(round((1 + math.sqrt(1 + 8 * max_pairs)) / 2))


if __name__ == "__main__":
    sol = Solution()
    points = [[1, 1], [2, 2], [3, 3]]
    print(sol.maxPoints(points))

    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print(sol.maxPoints(points))
