from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        n = len(digits)
        digit_letter_map = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        def backtrack(current_path, remaining_digits):
            if remaining_digits == 0:
                results.append(current_path)
                return

            next_letters_cand = digit_letter_map[int(
                digits[n - remaining_digits])]
            for idx, char in enumerate(next_letters_cand):
                backtrack(current_path+char, remaining_digits-1)

        backtrack('', n)
        return results


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
