class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        trans_matrix = [[-1]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            trans_matrix[i][0] = i

        for i in range(n+1):
            trans_matrix[0][i] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                phrase1 = word1[:i]
                phrase2 = word2[:j]
                if phrase1[-1] == phrase2[-1]:
                    trans_matrix[i][j] = trans_matrix[i-1][j-1]
                else:
                    trans_matrix[i][j] = min(
                        trans_matrix[i - 1][j] + 1,  # Deletion
                        trans_matrix[i][j - 1] + 1,  # Insertion
                        trans_matrix[i - 1][j - 1] + 1  # Substitution
                    )

        return trans_matrix[m][n]


if __name__ == "__main__":
    s = Solution()
    print(s.minDistance("horse", "ros"))
